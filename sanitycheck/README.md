### Run  test case ves client -> ves collector -> dmaap simulator

### Prerequisites
* Check your docker network ip:
```
ip a | grep docker0 | grep inet
```

If the IP address is different than 172.17.0.1/16:
inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0

You have to change the IP address in file events/vesAddressConfiguration.json
```
{
  "vesServerUrl": "http://<IP_Address>:8080/eventListener/v7"
}
```

If you want use event with http server files:
```
make upload-file-http-server
```
### 1. Build Projects
```
make start
```
### 2. Reconfigure ves url
```
make reconfigure-ves-url
```
### 2.1 Check dmaap sim
should return empty list 
```
make check-dmaap
```
### 3. Send one event
### 3.1 Send events:
```
make generate-event
```
send event with files from Http Server
```
generate-event-http-server
```
### 3.2 Check dmaap sim
should return list containing 1 event
```
make check-dmaap
```
### 4. Send few events:
### 4.1 Send events
this will send 4 event with interval 1 second
```
make generate-multiple-events
```
this event will send 2 events with files from Http Server with interval 5 second
```
make generate-multiple-events-http-server
```
### 4.2 Check dmaap sim
should return list containing 5 event (1 from point 3.1 and 4 from point 4.1)
```
make check-dmaap
```
### 5. Clear environment
```
make stop
```
