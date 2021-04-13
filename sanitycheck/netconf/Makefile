all: start

.PHONY: start

start:
	@echo "##### Start NETCONF server with AVCN manager #####"
	docker-compose up -d
	@echo "##### DONE #####"

stop:
	@echo "##### Stop NETCONF server with AVCN manager #####"
	docker-compose down
	@echo "##### DONE #####"

health-check:
	@echo "##### NETCONF simulator Health check #####\n"
	curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:6555/readiness

change-config:
	@echo "##### Trigger config change for model test-model #####"
	curl -X  POST http://localhost:6555/change_config/test-model -d @test_models/test-model.data.xml --header "Content-Type: application/xml"
	@echo "\n##### DONE #####"
