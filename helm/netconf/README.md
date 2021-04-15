# Netconf Server

# How to deploy on lab

1. Copy files from helm/netconf to lab
 
     `scp -i <path to key file .pem> -r <path to>/netconf ubuntu@<RKE_NODE_IP>:<remote path to>/netconf  `
2. Log into the RKE

3. Update helm dependencies
    
    `cd ./netconf`
    `helm dependency update`

4. Install chart on your lab
    
    `helm install netconfserver ./netconf -f oom/kubernetes/registry.yaml`
    
# How to use netconf
    extarnal port to use netconf server is 30555
    
<https://gerrit.onap.org/r/gitweb?p=integration/simulators/nf-simulator/netconf-server.git;a=blob;f=README.md;h=a093c60336d1e60fd1c5378122c59944975030be;hb=HEAD>
    