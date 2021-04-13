# Sanity check for NF simulator


## Build and run NF simulator

### 1. Build and start projects
**In order to start NF simulator for testing local images are required**:
- onap/org.onap.integration.nfsimulator.vesclient
- onap/org.onap.integration.nfsimulator.netconfserver
- onap/org.onap.integration.nfsimulator.avcnmanager
- onap/org.onap.integration.nfsimulator.pmhttpsserver

```
make start
```

### 2. Reconfigure ves url
if this command returns `curl: (56) Recv failure: Connection reset by peer`, 
it means VES-Client is not ready yet. Pleas try again after few seconds.
```
make reconfigure-ves-url
```
should return empty list 
```
make check-dmaap
```


## Run test case:
### ves-client -> ves-collector -> dmaap-simulator

### 1. Send one event
```
make generate-event
```
dmaap should return list containing 1 event
```
make check-dmaap
```
```
make clean-dmaap
```
### 2. Send one http event
```
generate-event-http-server
```
dmaap should return list containing 1 event
```
make check-dmaap
```
```
make clean-dmaap
```
### 3. Send few events:
this will send 4 event with interval 1 second
```
make generate-multiple-events
```
dmaap should return list containing 4 event,
if run least 4 seconds after  `generate-multiple-events`
```
make check-dmaap
```
```
make clean-dmaap
```
### 3. Send few Http events:
this event will send 2 events with files from Http Server with interval 5 second
```
make generate-multiple-events-http-server
```
dmaap should return list containing 2 event,
if run least 10 seconds after `generate-multiple-events-http-server`
```
make check-dmaap
```
```
make clean-dmaap
```


## Run test case:
### netconf-server -> kafka -> avcn-manager -> ves-client -> ves-collector -> dmaap-simulator

### 1. Change configuration of network model
This command will change configuration of test model. 
In case new configuration is same as old, no event will be generated.
In that case please change numeric values in file   
`./netconf/test_models/test-model.data.xml`
```
make change-config
```
dmaap should return list containing 3 event
```
make check-dmaap
```
```
make clean-dmaap
```


## Stop project and clear environment
```
make stop
```
