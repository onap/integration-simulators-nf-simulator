all: start

.PHONY: start

build:
	@echo "##### build (dmaap sim) #####"
	make -C dmaap-simulator build
	@echo "##### DONE #####"

start: build
	@echo "##### Starting #####"
	make -C ./ves-client start
	make -C ves start
	make -C ./https-server start
	make -C ./netconf start
	@echo "##### DONE #####"

stop:
	@echo "##### Stoping #####"
	make -C ves stop
	make -C ./https-server stop
	make -C ./netconf stop
	make -C ./ves-client stop
	docker network rm nf-simulator-network
	@echo "##### DONE #####"


# ves client
reconfigure-ves-url:
	make -C ./ves-client reconfigure-ves-url

generate-event:
	make -C ./ves-client generate-event

generate-multiple-events:
	make -C ./ves-client generate-multiple-events


# http server
upload-file-http-server:
	make -C ./https-server upload-file-http-server

generate-event-http-server:
	make -C ./https-server generate-event-http-server

generate-multiple-events-http-server:
	make -C ./https-server generate-multiple-events-http-server


# netconf server
change-config:
	make -C ./netconf change-config


# dmaap
check-dmaap:
	@echo "##### Check dmaap simulator for collected events #####"
	make -C dmaap-simulator get-data
	@echo "\n##### DONE #####"

clean-dmaap:
	@echo "##### Check dmaap simulator for collected events #####"
	make -C dmaap-simulator clean-data
	@echo "\n##### DONE #####"
