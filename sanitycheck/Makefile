all: start

.PHONY: start

build:
	@echo "##### build (dmaap sim) #####"
	make -C dmaap-simulator build
	@echo "##### DONE #####"

start: build
	@echo "##### start (dmaap sim,ves,pnf sim) #####"
	make -C ves start
	make -C ../ves-client start
	@echo "##### DONE #####"

stop:
	@echo "##### Stop (dmaap sim,ves,pnf sim)  #####"
	make -C ves stop
	make -C ../ves-client stop
	@echo "##### DONE #####"

upload-file-http-server:
	@echo "##### Upload file to Http server #####"
	curl -F "uploaded_file=@./resources/E_VES_bulkPM_IF_3GPP_3_example_1.xml.gz" -u demo:demo123456! http://localhost:32080/upload.php
	@echo "\n##### DONE #####"

generate-event:
	@echo "##### Trigger PNF Simulator to generate event #####"
	curl -X  POST http://localhost:5000/simulator/event -d @events/eventToVes.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-event-http-server:
	@echo "##### Trigger PNF Simulator to generate event with Http Server #####"
	curl -X  POST http://localhost:5000/simulator/event -d @events/eventToVesWithHttpServer.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

reconfigure-ves-url:
	@echo "##### Change VES address configuration in PNF Simulator #####"
	curl -X  PUT http://localhost:5000/simulator/config -d @events/vesAddressConfiguration.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-multiple-events:
	@echo "\n##### Trigger PNF Simulator to generate multiple events #####"
	curl -X  POST http://localhost:5000/simulator/start -d @events/fewEventsToVes.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-multiple-events-http-server:
	@echo "\n##### Trigger PNF Simulator to generate multiple events with http server#####"
	curl -X  POST http://localhost:5000/simulator/start -d @events/fewEventsToVesWithHttpServer.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

check-dmaap:
	@echo "##### Check dmaap simulator for collected events #####"
	make -C dmaap-simulator get-data
	@echo "\n##### DONE #####"
