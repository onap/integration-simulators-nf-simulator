# Nf-simulator

# How to deploy on lab

1. Copy files from helm/ves-client to lab
 
     `scp -i <path to key file .pem> -r <path to helm/> ubuntu@<RKE_NODE_IP>:<remote path to>/nf-simulator  `
2. Log into the RKE

3. Update helm dependencies

    WARNING: Before this step make sure, that in subproject folders "charts" folders are empty
    
    `cd ./nf-simulator`
    `helm dependency update nf-simulator`

4. Install chart on your lab
    
    `helm install nf nf-simulator/nf-simulator/ -f oom/kubernetes/registry.yaml`
    
# How to use nf-simulator
1. Try to send message:

    `<config xmlns="http://onap.org/pnf-simulator">
      <itemValue1>4265</itemValue1>
      <itemValue2>87</itemValue2>
    </config> `
    
    to http://<WORKER_ID_NODE>:30555/change_config/pnf-simulator
2. List all your pods
3. Check logs in netconf (you should see information that configuration has changed)
    `kubectl get logs <netconf pod name>`
4. Check logs in avcn-manager (you have to wait couple of minutes, and you should see information about sending new config to ves-client)
    `kubectl get logs <avcn-manager pod name>`
5. Check logs in ves-client (you should see logs about trying to send a new message to ves)
    `kubectl get logs <ves-client pod name>`   
    
    
 