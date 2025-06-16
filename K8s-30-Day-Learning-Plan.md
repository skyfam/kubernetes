#Kubernetes 30-Day Learning Plan (Markdown Checklist)


###  Week 1: Kubernetes Basics & Core Concepts

**Day 1**
- [ ] Understand Kubernetes architecture
- [ ] Install Minikube on your VM
- [ ] Start a basic cluster using Minikube
- [ ] Try: `minikube start`, `kubectl cluster-info`, `kubectl get nodes`

**Day 2**
- [ ] Learn `kubectl` basics: create, get, describe, delete
- [ ] Understand YAML manifest structure
- [ ] Deploy a Pod using a YAML file

**Day 3**
- [ ] Learn Deployments & ReplicaSets
- [ ] Create a Deployment for Nginx
- [ ] Scale up/down Pods using Deployment

**Day 4**
- [ ] Understand Namespaces
- [ ] Use labels and label selectors

**Day 5**
- [ ] Understand Kubernetes Services (ClusterIP, NodePort, LoadBalancer)
- [ ] Create and expose a NodePort service

**Day 6**
- [ ] Install NGINX Ingress Controller in Minikube
- [ ] Create basic Ingress rules
- [ ] Test route-based traffic

**Day 7**
- [ ] Review all core concepts
- [ ] Practice `kubectl` CLI commands
- [ ] Take a mock CKA quiz


###  Week 2: Configuration, Scheduling & Security

**Day 8**
- [ ] Create ConfigMaps
- [ ] Mount ConfigMap as environment variable and volume
- [ ] Create Secrets and mount them into Pods

**Day 9**
- [ ] Use environment variables in Pods
- [ ] Add Init Containers and understand their purpose

**Day 10**
- [ ] Set resource requests and limits
- [ ] Understand Pod QoS classes

**Day 11**
- [ ] Use nodeSelectors and affinity
- [ ] Apply taints and tolerations

**Day 12**
- [ ] Learn RBAC (Roles, ClusterRoles, Bindings)
- [ ] Create ServiceAccounts and bind roles

**Day 13**
- [ ] Apply Network Policies
- [ ] Restrict traffic between namespaces

**Day 14**
- [ ] Review YAMLs, security policies
- [ ] Take a mock test


###  Week 3: Storage, Logging & Troubleshooting

**Day 15**
- [ ] Learn Persistent Volumes (PVs) and Persistent Volume Claims (PVCs)
- [ ] Create a Pod with a PVC
- [ ] Enable dynamic provisioning

**Day 16**
- [ ] Learn StatefulSets and their use cases
- [ ] Create a Headless Service

**Day 17**
- [ ] Use `kubectl logs`, `exec`, `describe` for troubleshooting
- [ ] Add liveness and readiness probes

**Day 18**
- [ ] Simulate Pod failure and node crash
- [ ] Troubleshoot using `kubectl describe` and events

**Day 19**
- [ ] Use rollout strategies
- [ ] Pause, resume, undo rollouts

**Day 20**
- [ ] Create Jobs
- [ ] Schedule CronJobs

**Day 21**
- [ ] Review StatefulSets, Probes, CronJobs
- [ ] Practice case-based scenarios


###  Week 4: Advanced Topics & CKA Preparation

**Day 22**
- [ ] Take etcd snapshots
- [ ] Restore from etcd backup

**Day 23**
- [ ] Simulate Kubernetes upgrade
- [ ] Learn control plane vs kubelet upgrades

**Day 24**
- [ ] Install Prometheus & Grafana in Minikube
- [ ] Create basic alerts

**Day 25**
- [ ] Use `kubectl drain` and `cordon`
- [ ] Prune unused objects and dangling volumes

**Day 26**
- [ ] Backup manifests and secrets
- [ ] Recover lost resources manually

**Day 27**
- [ ] Create multi-container Pods (sidecars)
- [ ] Set up Horizontal Pod Autoscaler

**Day 28**
- [ ] Review entire CKA topics
- [ ] Finalize kubectl aliases and bash shortcuts


###  Week 5: 

**Day 29**
- [ ] Take a full-length mock exam (2 hrs)
- [ ] Review all mistakes and retry weak areas

**Day 30**
- [ ] Watch CKA exam strategy videos
- [ ] Export your cheatsheet and final notes
