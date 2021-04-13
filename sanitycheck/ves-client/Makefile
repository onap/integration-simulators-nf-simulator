all: start

.PHONY: start

start:
	@echo "##### start (dmaap sim,ves,ves-client sim) #####"
	make -C ../../ves-client start
	@echo "##### DONE #####"

stop:
	@echo "##### Stop (dmaap sim,ves,ves-client sim)  #####"
	make -C ../../ves-client stop
	@echo "##### DONE #####"

reconfigure-ves-url:
	@echo "##### Change VES address configuration in VES client#####"
	curl -X  PUT http://localhost:5000/simulator/config -d @events/vesAddressConfiguration.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-event:
	@echo "##### Trigger VES client to generate event #####"
	curl -X  POST http://localhost:5000/simulator/event -d @events/eventToVes.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-multiple-events:
	@echo "\n##### Trigger VES client to generate multiple events #####"
	curl -X  POST http://localhost:5000/simulator/start -d @events/fewEventsToVes.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"
