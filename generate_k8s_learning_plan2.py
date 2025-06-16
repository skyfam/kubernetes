# Kubernetes 30-Day Learning Plan Markdown Generator
plan = {
    "Week 1: Kubernetes Basics & Core Concepts": [
        ("Day 1 Introduction to Kubernetes", [
            "Understand Kubernetes architecture: Master, Nodes, API Server, etcd, Scheduler, Kubelet, Kube-proxy.",
            "Install Minikube (if not already done).",
            "Start a basic cluster using Minikube.",
            "K8s Concepts Overview",
            "Try: minikube start, kubectl cluster-info, kubectl get nodes"
        ]),
        ("Day 2 Kubernetes Objects & CLI Basics", [
            "Learn kubectl basics: create, get, describe, delete",
            "Understand YAML manifest structure.",
            "Deploy your first Pod using a YAML file.",
            "Kubectl Cheat Sheet [https://kubernetes.io/docs/reference/kubectl/quick-reference/]",
            "Practice: kubectl apply -f pod.yaml, kubectl delete pod <name>"
        ]),
        ("Day 3 Deployments & ReplicaSets", [
            "Learn the purpose of Deployments & ReplicaSets.",
            "Create a Deployment for Nginx.",
            "Scale up/down Pods using Deployment.",
            "Deployments [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/]",
            "kubectl scale deployment nginx --replicas=3"
        ]),
        ("Day 4 Namespaces, Labels & Selectors", [
            "Learn about Namespaces and how to isolate workloads.",
            "Practice labels and label selectors.",
            "Namespaces [https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/]",
            "kubectl get pods --namespace=kube-system, kubectl get pods -l app=nginx"
        ]),
        ("Day 5 Services: ClusterIP, NodePort, LoadBalancer", [
            "Understand Kubernetes Services & DNS",
            "Create and expose a service using NodePort",
            "K8s Services [https://kubernetes.io/docs/concepts/services-networking/service/]",
            "kubectl expose deployment nginx --type=NodePort --port=80"
        ]),
        ("Day 6 Ingress Controller Basics", [
            "Install Ingress Controller in Minikube",
            "Create basic Ingress resources",
            "Ingress Resources [https://kubernetes.io/docs/concepts/services-networking/ingress/]",
            "Practice accessing apps via Ingress path rules"
        ]),
        ("Day 7 Review & Quiz", [
            "Review all core concepts from Week 1",
            "Take a mock test from:\n  CKA Practice Exam [https://medium.com/@karani_ph/certified-kubernetes-administrator-cka-practice-exam-with-well-explained-answers-2aa1e56383bd]",
            "Practice creating and deleting Deployments, Services"
        ])
    ],
    "Week 2: Configuration, Scheduling & Security": [
        ("Day 8 ConfigMaps & Secrets", [
            "Learn to create ConfigMaps & mount as env/volume",
            "Create Secrets & inject as env variables",
            "ConfigMaps [https://kubernetes.io/docs/concepts/configuration/configmap/]",
            "kubectl create configmap, kubectl create secret generic"
        ]),
        ("Day 9 Environment Variables & Init Containers", [
            "Understand environment injection in containers",
            "Use init containers for pre-tasks",
            "Write a pod spec with initContainer that pings a service before main container starts"
        ]),
        ("Day 10 Resource Limits & QoS Classes", [
            "Set CPU/memory requests & limits",
            "Observe QoS classifications",
            "Resource Management [https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/]"
        ]),
        ("Day 11 Node Affinity, Taints & Tolerations", [
            "Understand how Kubernetes schedules Pods to Nodes",
            "Use nodeSelectors, affinity, taints/tolerations",
            "Practice assigning workloads to specific nodes"
        ]),
        ("Day 12 RBAC & ServiceAccounts", [
            "Learn about ClusterRole, RoleBinding, ServiceAccounts",
            "Create RBAC policies for a specific namespace",
            "RBAC [https://kubernetes.io/docs/reference/access-authn-authz/rbac/]"
        ]),
        ("Day 13 Network Policies", [
            "Apply network policies to restrict pod communication",
            "Try allowing only frontend → backend communication"
        ]),
        ("Day 14 Weekly Review", [
            "Take quizzes from CKA Mock Tests [https://github.com/dgkanatsios/CKAD-exercises]",
            "Review logs, RBAC policies, pod scheduling",
            "Watch Kelsey Hightower’s Kubernetes The Hard Way [https://github.com/kelseyhightower/kubernetes-the-hard-way]"
        ])
    ],
    "Week 3: Storage, Logging & Troubleshooting": [
        ("Day 15 Volumes, PV & PVC", [
            "Learn PersistentVolumes, PersistentVolumeClaims",
            "Practice dynamic volume provisioning",
            "K8s Volumes [https://kubernetes.io/docs/concepts/storage/volumes/]"
        ]),
        ("Day 16 StatefulSets & Headless Services", [
            "Understand StatefulSets for stateful apps like MongoDB",
            "Create a headless service",
            "Create a StatefulSet with volume claim templates"
        ]),
        ("Day 17 Logs & Probes", [
            "Explore kubectl logs, exec, describe",
            "Add readiness & liveness probes",
            "Probes [https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/]"
        ]),
        ("Day 18 Debugging & Troubleshooting Pods", [
            "Diagnose container restarts, image pull failures, scheduling issues",
            "Use kubectl describe, logs, and events",
            "Simulate common issues and resolve"
        ]),
        ("Day 19 Managing Deployments & Rollbacks", [
            "Practice kubectl rollout, history, undo",
            "Simulate a failed rollout and rollback"
        ]),
        ("Day 20 Job & CronJobs", [
            "Create batch jobs and scheduled tasks using CronJobs",
            "Jobs [https://kubernetes.io/docs/concepts/workloads/controllers/job/]"
        ]),
        ("Day 21 Weekly Recap", [
            "Practice StatefulSets, Rollouts, Debugging",
            "Take CKA Mock Exams (if you’ve access) [https://killer.sh/cka]"
        ])
    ],
    "Week 4: Advanced Topics & Final Prep": [
        ("Day 22 etcd Backup & Restore", [
            "Take an etcd backup using etcdctl",
            "Restore etcd snapshot on control plane",
            "etcd Backup [https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/]"
        ]),
        ("Day 23 Upgrading Kubernetes Cluster", [
            "Practice upgrading the control plane and kubelet",
            "Understand version skew policies"
        ]),
        ("Day 24 Monitoring & Metrics", [
            "Install Prometheus & Grafana in Minikube",
            "Expose dashboards and set alerts"
        ]),
        ("Day 25 Cluster Maintenance", [
            "Drain & cordon nodes",
            "Rotate certificates",
            "Prune unused resources"
        ]),
        ("Day 26 Backup & Disaster Recovery", [
            "Backup critical manifests and secrets",
            "Simulate node/pod failure and recover"
        ]),
        ("Day 27 Production-Grade Scenarios", [
            "Implement a multi-container pod",
            "Setup HPA (Horizontal Pod Autoscaler)"
        ]),
        ("Day 28 Final Review", [
            "Review all CKA topics",
            "Practice all imperative commands",
            "Finalize your bookmarks to K8s docs [https://kubernetes.io/docs/home/]"
        ]),
        ("Day 29 Mock Exam Day", [
            "Time-boxed mock exam (2 hours)",
            "Identify weak areas and note improvements"
        ]),
        ("Day 30 Exam Strategy & Confidence Boost", [
            "Review bookmarks, aliases",
            "Practice switching between questions",
            "Watch CKA Tips from Experts (YouTube)"
        ])
    ]
}

# Generate the markdown content
output = "# 30-Day Kubernetes Expert Plan – Notion-Style Checklist\n\n"

for week, days in plan.items():
    output += f"## {week}\n\n"
    for day_title, tasks in days:
        output += f"### {day_title}\n"
        for task in tasks:
            output += f"- [ ] {task}\n"
        output += "\n"

# Write to markdown file
with open("K8s-30-Day-Learning-Plan.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Checklist saved to 'K8s-30-Day-Learning-Plan.md'")
