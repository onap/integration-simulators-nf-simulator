all: build

.PHONY: build

build:
	@echo "##### Build dmaap simulator image #####"
	docker build . -t dmaap-simulator
	@echo "##### DONE #####"

start:
	@echo "##### Start dmaap simulator #####"
	docker run -d -p 3904:3904 --name dmaap-simulator dmaap-simulator
	@echo "##### DONE #####"

stop:
	@echo "##### Stop dmaap simulator #####"
	docker rm -f dmaap-simulator
	@echo "##### DONE #####"

get-data:
	@echo "##### Get data fetched by dmaap-simulator #####\n"
	curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:3904/events
	@echo "\n\n##### DONE #####"
