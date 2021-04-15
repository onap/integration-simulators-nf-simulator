# NF Simulator

An idea behind this simulator is to introduce application,
which supports ORAN defined O1 interface (reporting of NF events to Service Management Orchestrators).
Within the use-case, it is expected, that an NF configuration change, 
happening due to multiple reasons (network mechanism triggered change - e.g. discovery of neighbours) 
is reported to the network management system, using ONAP's VES REST events.
The simulator is expected to cover planned NF behaviour - 
receive the config change via a NetConf protocol and report that change 
(also potentially other related changes) to the network management system using ONAP`s VES event.


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
