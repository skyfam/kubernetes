# Kubernetes Master & Agent nodes automation
## Prerequisites
```
VirtualBox Setup
2+ Ubuntu VMs (1 master, 1+ workers)
Static or bridged networking (e.g., 192.168.56.10, .11, .12)
Passwordless SSH access from Ansible control host to all nodes
```

## Directory Structure
```
k8s-ansible/
├── inventory.ini
├── group_vars/
│   └── all.yaml
├── playbooks/
│   ├── pre-req.yaml
│   ├── install-k8s.yaml
│   ├── init-master.yaml
│   ├── join-workers.yaml
│   └── deploy-cni.yaml
└── templates/
    └── kubeadm-config.yaml.j2
```

## Run the Playbooks in Order
```
ansible-playbook -i inventory.ini playbooks/pre-req.yaml
ansible-playbook -i inventory.ini playbooks/install-k8s.yaml
ansible-playbook -i inventory.ini playbooks/init-master.yaml
ansible-playbook -i inventory.ini playbooks/join-workers.yaml
ansible-playbook -i inventory.ini playbooks/deploy-cni.yaml
```