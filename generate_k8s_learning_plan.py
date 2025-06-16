# Kubernetes 30-Day Learning Plan Markdown Generator

weeks = {
    1: "Kubernetes Basics & Core Concepts",
    2: "Configuration, Scheduling & Security",
    3: "Storage, Logging & Troubleshooting",
    4: "Advanced Topics & CKA Preparation",
    5: "",
    6: "",
    7: ""
}

daily_tasks = {
    1: ["Understand Kubernetes architecture", "Install Minikube on your VM", "Start a basic cluster using Minikube", "Try: `minikube start`, `kubectl cluster-info`, `kubectl get nodes`"],
    2: ["Learn `kubectl` basics: create, get, describe, delete", "Understand YAML manifest structure", "Deploy a Pod using a YAML file"],
    3: ["Learn Deployments & ReplicaSets", "Create a Deployment for Nginx", "Scale up/down Pods using Deployment"],
    4: ["Understand Namespaces", "Use labels and label selectors"],
    5: ["Understand Kubernetes Services (ClusterIP, NodePort, LoadBalancer)", "Create and expose a NodePort service"],
    6: ["Install NGINX Ingress Controller in Minikube", "Create basic Ingress rules", "Test route-based traffic"],
    7: ["Review all core concepts", "Practice `kubectl` CLI commands", "Take a mock CKA quiz"],
    8: ["Create ConfigMaps", "Mount ConfigMap as environment variable and volume", "Create Secrets and mount them into Pods"],
    9: ["Use environment variables in Pods", "Add Init Containers and understand their purpose"],
    10: ["Set resource requests and limits", "Understand Pod QoS classes"],
    11: ["Use nodeSelectors and affinity", "Apply taints and tolerations"],
    12: ["Learn RBAC (Roles, ClusterRoles, Bindings)", "Create ServiceAccounts and bind roles"],
    13: ["Apply Network Policies", "Restrict traffic between namespaces"],
    14: ["Review YAMLs, security policies", "Take a mock test"],
    15: ["Learn Persistent Volumes (PVs) and Persistent Volume Claims (PVCs)", "Create a Pod with a PVC", "Enable dynamic provisioning"],
    16: ["Learn StatefulSets and their use cases", "Create a Headless Service"],
    17: ["Use `kubectl logs`, `exec`, `describe` for troubleshooting", "Add liveness and readiness probes"],
    18: ["Simulate Pod failure and node crash", "Troubleshoot using `kubectl describe` and events"],
    19: ["Use rollout strategies", "Pause, resume, undo rollouts"],
    20: ["Create Jobs", "Schedule CronJobs"],
    21: ["Review StatefulSets, Probes, CronJobs", "Practice case-based scenarios"],
    22: ["Take etcd snapshots", "Restore from etcd backup"],
    23: ["Simulate Kubernetes upgrade", "Learn control plane vs kubelet upgrades"],
    24: ["Install Prometheus & Grafana in Minikube", "Create basic alerts"],
    25: ["Use `kubectl drain` and `cordon`", "Prune unused objects and dangling volumes"],
    26: ["Backup manifests and secrets", "Recover lost resources manually"],
    27: ["Create multi-container Pods (sidecars)", "Set up Horizontal Pod Autoscaler"],
    28: ["Review entire CKA topics", "Finalize kubectl aliases and bash shortcuts"],
    29: ["Take a full-length mock exam (2 hrs)", "Review all mistakes and retry weak areas"],
    30: ["Watch CKA exam strategy videos", "Export your cheatsheet and final notes"]
}

lines = ["#Kubernetes 30-Day Learning Plan (Markdown Checklist)\n"]

for day in range(1, 31):
    week_number = (day - 1) // 7 + 1
    if day == 1 or (day - 1) % 7 == 0:
        lines.append(f"\n###  Week {week_number}: {weeks[week_number]}\n")
    lines.append(f"**Day {day}**")
    for task in daily_tasks[day]:
        lines.append(f"- [ ] {task}")
    lines.append("")

with open("K8s-30-Day-Learning-Plan.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Markdown file 'K8s-30-Day-Learning-Plan.md' has been created.")
