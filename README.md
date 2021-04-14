# NF Simulator

Goal of this project is to simulate `Network Function`. 


## Simulator components
This simulator is consist of projects (components):
- avcn-manager
- netconf-server
- pm-https-server
- ves-client

Each of these projects can be developed, build and run independently.
Nonetheless, in order to achieve goal of this simulator, 
these components needs to be connected and interact.

### Components interaction flow
*netconf-server -> Message Queue (Kafka) -> avcn-server -> ves-client -> ves*

Above flow shows how components are connected with each other.
The goal of that connected components is to propagate information
about network element configuration change (netconf server) to ONAP (ves).

More examples and use cases are shown in `sanitycheck` directory.

For more details about each project see *README* files in projects directories.


## Starting and Testing simulator

To start whole system (simulator) locally docker compose is needed.
Description on how to do that, with all needed docker-compose files,
is located in `sanitycheck` directory.
This directory contains also description of **test scenarios**.
All that descriptions are located in *README* file.


## Simulator CLI

This simulator has also CLI that can be used to communicate with running components.
Description on how to use this tool is located in `simulator-cli` directory.
