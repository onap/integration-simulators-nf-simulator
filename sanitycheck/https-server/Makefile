all: start

.PHONY: start

start:
	@echo "##### Start HTTPS server #####"
	docker-compose up -d
	@echo "##### DONE #####"

stop:
	@echo "##### Stop HTTPS server #####"
	docker-compose down
	@echo "##### DONE #####"

upload-file-http-server:
	@echo "##### Upload file to Http server #####"
	curl -F "uploaded_file=@./resources/E_VES_bulkPM_IF_3GPP_3_example_1.xml.gz" -u demo:demo123456! http://localhost:32080/upload.php
	@echo "\n##### DONE #####"

generate-event-http-server:
	@echo "##### Trigger VES client to generate event with Http Server #####"
	curl -X  POST http://localhost:5000/simulator/event -d @events/eventToVesWithHttpServer.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"

generate-multiple-events-http-server:
	@echo "\n##### Trigger VES client to generate multiple events with http server#####"
	curl -X  POST http://localhost:5000/simulator/start -d @events/fewEventsToVesWithHttpServer.json --header "Content-Type: application/json"
	@echo "\n##### DONE #####"
