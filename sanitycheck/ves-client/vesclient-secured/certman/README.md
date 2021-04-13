## Fetching from AAF Certman
This readme describes how to run VES client with certificates fetched using AAF Certman

### Description

docker-compose.yml prepares VES client container for HTTPS communication with VES.

When docker-compose starts certs-init container fills connected volume with certificates, truststores, keystores, 
passwords etc. Next ves-client container starts and connects to the same volume. On startup it should read password
values from proper files and set them in system environment variables. With these variables and files in volume 
application is ready to work on HTTPS.

### Prerequisites

certs-init container works with external AAF on cloud. Due to that fact it must have set correct IPs to workers that
has access to AAF. In docker-compose.yml fields with mentioned IPs are:
    
    * aaf-locate.onap
    * aaf-cm.onap
    * aaf-service.onap

### Start

Run VES client:

```
make start-ves-client
```

### Send event

**ATTENTION**

``sanitycheck/events/eventToVes.json`` file which is request for sending event to VES must have correct ``vesServerURL`` 
field before sending event. 
IP of ``vesServerURL`` should be the same as given in docker-compose-certman.yml in ``aaf-locate.onap`` field.
To use secured connection remember about setting protocol to https:// and port to proper secured port of VES.

To send event from VES client to VES use this command from ``ne-simulator/sanitycheck`` directory:

````
make generate-event
````

Sample ``sanitycheck/events/eventToVes.json`` file content is:

```json
{
  "vesServerUrl": "https://10.183.35.177:30417/eventListener/v7",
  "event": {
    "event": {
      "commonEventHeader": {
        "version": "4.0.1",
        "vesEventListenerVersion": "7.0.1",
        "domain": "fault",
        "eventName": "Fault_Vscf:Acs-Ericcson_PilotNumberPoolExhaustion",
        "eventId": "fault0000245",
        "sequence": 1,
        "priority": "High",
        "reportingEntityId": "cc305d54-75b4-431b-adb2-eb6b9e541234",
        "reportingEntityName": "ibcx0001vm002oam001",
        "sourceId": "de305d54-75b4-431b-adb2-eb6b9e546014",
        "sourceName": "scfx0001vm002cap001",
        "nfVendorName": "Ericsson",
        "nfNamingCode": "scfx",
        "nfcNamingCode": "ssc",
        "startEpochMicrosec": 1413378172000000,
        "lastEpochMicrosec": 1413378172000000,
        "timeZoneOffset": "UTC-05:30"
      },
      "faultFields": {
        "faultFieldsVersion": "4.0",
        "alarmCondition": "PilotNumberPoolExhaustion",
        "eventSourceType": "other",
        "specificProblem": "Calls cannot complete - pilot numbers are unavailable",
        "eventSeverity": "CRITICAL",
        "vfStatus": "Active",
        "alarmAdditionalInformation": {
          "PilotNumberPoolSize": "1000"
        }
      }
    }
  }
}
```

### Stop
To remove VES client containers use:
```
make clean-ves-client
```
