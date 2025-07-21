These are the steps to follow and set-up a example app to test out and play around with a kubernetes cluster locally.

### Prerequisite [Machine setup]
1. Install [Podman](https://podman.io/docs/installation).  
    It a container tool's like docker desktop.
2. Install minikkuber extention for podman. [Link](https://podman-desktop.io/docs/minikube/installing-extension).  
    **Optional**: install native CLI for minikube if you want to run minikube commands directly from terminal. [Link](https://podman-desktop.io/docs/minikube/installing)
3. Create a local kubernetes cluster using minikube. [Link](https://podman-desktop.io/docs/minikube/creating-a-minikube-cluster).  
**Note:** Follow the default values, using `podman` driver and `cri-o` runtime.  
Verify the cluster using podman UI. [Link](https://podman-desktop.io/docs/minikube/working-with-your-local-minikube-cluster)
4. Install helmfile. [Official docs](https://helmfile.readthedocs.io/en/latest/#installation).   
Ubuntu, install via snap docs: [Link](https://snapcraft.io/install/helmfile-snap/ubuntu).  
Run this command: ``` sudo snap install helmfile-snap ```


### Setup Code
1. Build the code container:
Run this command
```podman build -f Dockerfile -t deploy-sample:latest```
OR:
Use the podman UI: [Link]https://podman-desktop.io/docs/containers/images/building-an-image.   
**Note:** For the name use `deploy-sample`
2. Push image to minikube. [Link](https://podman-desktop.io/docs/minikube/pushing-aben-image-to-minikube).  
This will be replaced with push to cloud specific container repository (ECR/GCR/GHCR\Docker Hub) later, for local we follow this step.
3. Sync the helmfile to deploy istio services and the app automatically.   
Run the following command: ```helmfile -f .deploy/helmfile.yaml sync```.  
It should give an output similar to this:
```
UPDATED RELEASES:
NAME            NAMESPACE       CHART             VERSION   DURATION
deploy-sample   deploy-sample   ./deploy-sample   0.1.0           0s
istio-base      istio-system    istio/base        1.26.2          2s
istiod          istio-system    istio/istiod      1.26.2          1s
```

3.1 **(Optional)** Check deployed images using helm:

Check in istio-system namespace: ```helm ls -n istio-system```.  
Output:
```
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
istio-base      istio-system    4               2025-07-21 00:40:53.742073 +0530 IST    deployed        base-1.26.2     1.26.2     
istiod          istio-system    4               2025-07-21 00:40:56.617779 +0530 IST    deployed        istiod-1.26.2   1.26.2
```
Check in deploy-sample namespace: ```helm ls -n deploy-sample```.  
Output:
```
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
deploy-sample   deploy-sample   4               2025-07-21 00:40:52.620737 +0530 IST    deployed        deploy-sample-0.1.0     1.16.0   
```
From her you can look at the pods and service logs from the podman UI.

For now this is the progress.


### TODO:
Set up ingress gateway to route traffic from outside world to services and monitoring
And set up Mesh for internal traffic routing.