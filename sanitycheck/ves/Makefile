all: start

.PHONY: start

start:
	@echo "##### Start VES with DMAAP simulator #####"
	docker-compose up -d
	@echo "##### DONE #####"

stop:
	@echo "##### Stop VES with DMAAP simulator #####"
	docker-compose down
	@echo "##### DONE #####"

health-check:
	@echo "##### Health check #####\n"

	@echo "##### DMAAP simulator is ready #####\n"
	curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:3904/events

	@echo "\n\n##### VES is ready #####\n"
	curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET GET http://localhost:8080/healthcheck
	@echo "\n\n##### DONE #####"

