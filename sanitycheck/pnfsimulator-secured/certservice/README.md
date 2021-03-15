## Fetching certificates from OOM CertService (CMPv2)
This readme describes how to run PNF Simulator with certificates fetched using OOM CertService (CMPv2) 

### Description

Using Makefile in this directory following can be achieved:

* Setup environment for PNF Simulator, i.e.:
    * Create certificates that will be used for internal communication between CertService and CertService Clients.
      Generated internal certificates should be present in `resources/certs` directory.
    * Start and configure EJBCA
    * Start and configure AAF Cert Service.
    * Run Cert Service Clients to fetch certificates for VES and PNF Simulator. Certificates will be stored for the
      components in `resources/certservice-client/client-volume-for-ves`
      and `resources/certservice-client/client-volume-for-pnfsim` accordingly.
    * Start VES and DMaaP Simulator. Fetched certificates will be mounted to VES.

* Start PNF Simulator. Fetched certificates will be mounted to PNF Simulator.
* Clean up.

### Prerequisites
##### VES collector local deployment prerequisites

By default, the image of VES from Nexus supports only HTTP communication. A local image with enabled HTTPS must be build
to use local VES as PNF simulator destination.

1. Pull VES repository
2. In `<VES_PROJECT_ROOT>/etc/collector.properties` file set field `auth.method=certBasicAuth`
3. Build a local image: `mvn clean install docker:build` from VES project root directory.

Local VES deployment uses also DMaaP simulator. Its image should be built locally as well.
1. Go to `sanitycheck/dmaap-simulator` directory
2. Run: `make build`

### Setup environment
To set up whole environment for PNF Simulator, i.e.:
- deploy and configure EJBCA
- deploy Cert Service
- fetch certificates for VES and PNF Simulator using Cert Service clients
- run DMaaP Simulator
- run VES with fetched certificates

execute:
````
make setup-env
````
Note that this command setups whole environment besides PNF Simulator itself. 

## Run PNF Simulator
To run PNF Simulator execute:
````
make start-pnfsim
````
PNF Simulator starts together with the http server.
This command starts PNF Simulator with certificates fetched using CertService (certificates are fetched in the previous
step)

### Send event

Configure PNF simulator to use proper VES URL by executing this command from ``pnf-simulator/sanitycheck`` directory:
```
make reconfigure-ves-url
```

Send an event from PNF simulator to VES by executing this command from ``pnf-simulator/sanitycheck`` directory:
```
make generate-event
```

### Restart PNF Simulator

To restart only PNF Simulator execute:
```
make restart-pnfsim
```

### Clean up
To clean all generated certificates, remove PNF Simulator, CertService, EJBCA, VES and DMaaP Simulator containers:
```
make clean-all
```
