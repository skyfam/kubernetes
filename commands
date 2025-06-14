<!-- Kubernetes Cluster (e.g., Minikube) is Not Running
If you're using Minikube or a local cluster, the cluster might be stopped. -->
minikube status
<!-- If it's not running, start it: -->
minikube start


<!-- Wrong or Corrupted kubeconfig
kubectl might be pointing to an outdated or broken kubeconfig context.
List available contexts: -->
kubectl config get-contexts
<!-- Switch to the correct one: -->
kubectl config use-context <your-context>
<!-- Or regenerate it with: -->
minikube update-context



<!-- Diagnose the Error
Run the following command to see why the pod is failing: -->
kubectl describe pod nginx-depl-68c944fcbc-9swmd
<!-- Then also get logs: -->
kubectl logs nginx-depl-68c944fcbc-9swmd




<!-- Pod Clean-up
If you want to be sure everything is clean and running fresh, you can delete and recreate the pod: -->
kubectl delete pod nginx-depl-68c944fcbc-9swmd


<!-- Identify the Deployment -->
kubectl get deployments

<!-- Delete the Deployment (and all its pods) -->
kubectl delete deployment nginx-depl

<!-- If You Only Want to Delete the Pod Once (For Testing)
You could scale the Deployment to 0 before deleting the pod: -->
kubectl scale deployment nginx-depl --replicas=0
kubectl delete pod <pod-name>