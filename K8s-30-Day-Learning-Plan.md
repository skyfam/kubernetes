# 30-Day Kubernetes Expert Plan – Notion-Style Checklist

## Week 1: Kubernetes Basics & Core Concepts

### Day 1 Introduction to Kubernetes
- [ ] Understand Kubernetes architecture: Master, Nodes, API Server, etcd, Scheduler, Kubelet, Kube-proxy.
- [ ] Install Minikube (if not already done).
- [ ] Start a basic cluster using Minikube.
- [ ] K8s Concepts Overview
- [ ] Try: minikube start, kubectl cluster-info, kubectl get nodes

### Day 2 Kubernetes Objects & CLI Basics
- [ ] Learn kubectl basics: create, get, describe, delete
- [ ] Understand YAML manifest structure.
- [ ] Deploy your first Pod using a YAML file.
- [ ] Kubectl Cheat Sheet [https://kubernetes.io/docs/reference/kubectl/quick-reference/]
- [ ] Practice: kubectl apply -f pod.yaml, kubectl delete pod <name>

### Day 3 Deployments & ReplicaSets
- [ ] Learn the purpose of Deployments & ReplicaSets.
- [ ] Create a Deployment for Nginx.
- [ ] Scale up/down Pods using Deployment.
- [ ] Deployments [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/]
- [ ] kubectl scale deployment nginx --replicas=3

### Day 4 Namespaces, Labels & Selectors
- [ ] Learn about Namespaces and how to isolate workloads.
- [ ] Practice labels and label selectors.
- [ ] Namespaces [https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/]
- [ ] kubectl get pods --namespace=kube-system, kubectl get pods -l app=nginx

### Day 5 Services: ClusterIP, NodePort, LoadBalancer
- [ ] Understand Kubernetes Services & DNS
- [ ] Create and expose a service using NodePort
- [ ] K8s Services [https://kubernetes.io/docs/concepts/services-networking/service/]
- [ ] kubectl expose deployment nginx --type=NodePort --port=80

### Day 6 Ingress Controller Basics
- [ ] Install Ingress Controller in Minikube
- [ ] Create basic Ingress resources
- [ ] Ingress Resources [https://kubernetes.io/docs/concepts/services-networking/ingress/]
- [ ] Practice accessing apps via Ingress path rules

### Day 7 Review & Quiz
- [ ] Review all core concepts from Week 1
- [ ] Take a mock test from:
  CKA Practice Exam [https://medium.com/@karani_ph/certified-kubernetes-administrator-cka-practice-exam-with-well-explained-answers-2aa1e56383bd]
- [ ] Practice creating and deleting Deployments, Services

