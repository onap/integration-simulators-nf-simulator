## Fetching certificates from OOM CertService (CMPv2)
This readme describes how to run VES client with certificates fetched using OOM CertService (CMPv2) 

### Description

Using Makefile in this directory following can be achieved:

* Setup environment for VES client, i.e.:
    * Create certificates that will be used for internal communication between CertService and CertService Clients.
      Generated internal certificates should be present in `resources/certs` directory.
    * Start and configure EJBCA
    * Start and configure AAF Cert Service.
    * Run Cert Service Clients to fetch certificates for VES and VES client. Certificates will be stored for the
      components in `resources/certservice-client/client-volume-for-ves`
      and `resources/certservice-client/client-volume-for-vesclient` accordingly.
    * Start VES and DMaaP Simulator. Fetched certificates will be mounted to VES.

* Start VES client. Fetched certificates will be mounted to VES client.
* Clean up.

### Prerequisites
##### VES collector local deployment prerequisites

By default, the image of VES from Nexus supports only HTTP communication. A local image with enabled HTTPS must be build
to use local VES as VES client destination.

1. Pull VES repository
2. In `<VES_PROJECT_ROOT>/etc/collector.properties` file set field `auth.method=certBasicAuth`
3. Build a local image: `mvn clean install docker:build` from VES project root directory.

Local VES deployment uses also DMaaP simulator. Its image should be built locally as well.
1. Go to `sanitycheck/dmaap-simulator` directory
2. Run: `make build`

### Setup environment
To set up whole environment for VES client, i.e.:
- deploy and configure EJBCA
- deploy Cert Service
- fetch certificates for VES and VES client using Cert Service clients
- run DMaaP Simulator
- run VES with fetched certificates

execute:
````
make setup-env
````
Note that this command setups whole environment besides VES client itself. 

## Run VES client
To run VES client execute:
````
make start-ves-client
````
VES client starts together with the http server.
This command starts VES client with certificates fetched using CertService (certificates are fetched in the previous
step)

### Send event


Configure VES client to use proper VES URL by executing this command from ``nf-simulator/sanitycheck`` directory:

  TIP: edit vesAddressConfigure.json and set "vesServerUrl": "https://ves:8443/eventListener/v7"

```
make reconfigure-ves-url
```

Send an event from VES client to VES by executing this command from ``nf-simulator/sanitycheck`` directory:
```
make generate-event
```

### Restart VES client

To restart only VES client execute:
```
make restart-ves-client
```

### Clean up
To clean all generated certificates, remove VES client, CertService, EJBCA, VES and DMaaP Simulator containers:
```
make clean-all
```
