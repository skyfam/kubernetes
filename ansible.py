from zipfile import ZipFile
import os

project_name = "k8s-ansible"
folders = [
    f"{project_name}/playbooks",
    f"{project_name}/group_vars",
    f"{project_name}/templates"
]
files = {
    f"{project_name}/inventory.ini": """
[master]
192.168.56.10 ansible_user=ubuntu

[workers]
192.168.56.11 ansible_user=ubuntu
192.168.56.12 ansible_user=ubuntu

[all:vars]
ansible_python_interpreter=/usr/bin/python3
""",
    f"{project_name}/group_vars/all.yaml": """
kube_version: "1.28.0"
pod_network_cidr: "192.168.0.0/16"
""",
    f"{project_name}/playbooks/pre-req.yaml": """
- name: Install prerequisites
  hosts: all
  become: yes
  tasks:
    - name: Update apt cache
      apt: update_cache=yes
""",
    f"{project_name}/playbooks/install-k8s.yaml": """
- name: Install Kubernetes components
  hosts: all
  become: yes
  tasks:
    - name: Install required packages
      apt:
        name: ['curl', 'apt-transport-https', 'ca-certificates', 'software-properties-common']
        state: present
        update_cache: yes

    - name: Add Kubernetes repository
      apt_repository:
        repo: deb http://apt.kubernetes.io/ kubernetes-xenial main
        state: present

    - name: Install kubelet, kubeadm, kubectl
      apt:
        name: ['kubelet', 'kubeadm', 'kubectl']
        state: present
        update_cache: yes
""",
    f"{project_name}/playbooks/init-master.yaml": """
- name: Initialize Kubernetes Master
  hosts: master
  become: yes
  tasks:
    - name: Initialize kubeadm
      shell: |
        kubeadm init --apiserver-advertise-address={{ ansible_host }} \
                     --pod-network-cidr=192.168.0.0/16
      register: kubeadm_output
      changed_when: "'kubeadm join' in kubeadm_output.stdout"

    - name: Copy kubeconfig to user
      shell: |
        mkdir -p $HOME/.kube
        cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        chown $(id -u):$(id -g) $HOME/.kube/config

    - name: Save join command
      shell: kubeadm token create --print-join-command
      register: join_cmd
      delegate_to: localhost
      changed_when: false

    - name: Set join command for later use
      set_fact:
        join_command: "{{ join_cmd.stdout }}"
""",
    f"{project_name}/playbooks/join-workers.yaml": """
- name: Join worker nodes to cluster
  hosts: workers
  become: yes
  tasks:
    - name: Join the node
      shell: "{{ hostvars['192.168.56.10'].join_command }} --ignore-preflight-errors=all"
""",
    f"{project_name}/playbooks/deploy-cni.yaml": """
- name: Apply Calico CNI Plugin
  hosts: master
  become: yes
  tasks:
    - name: Apply Calico manifest
      shell: kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml
"""
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content.strip())

zip_filename = f"{project_name}.zip"
with ZipFile(zip_filename, "w") as zipf:
    for folder_name, _, filenames in os.walk(project_name):
        for filename in filenames:
            filepath = os.path.join(folder_name, filename)
            zipf.write(filepath)

print(f"Created: {zip_filename}")
