# nf-simulator

# How to deploy on lab

1. Copy files from helm/ directory to lab
 
     `scp -i <path to key file .pem> -r <path to>/helm ubuntu@<RKE_NODE_IP>:<remote path to>/helm  `
2. Log into the RKE

3. Update helm dependencies
    
    `cd ./helm/nf-simulator`
    `helm dependency update`

4. Install chart on your lab
    
    `helm install nf-simulator ./nf-simulator -f oom/kubernetes/registry.yaml`
    
