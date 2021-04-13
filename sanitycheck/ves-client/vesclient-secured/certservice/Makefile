default:
	@echo "There is no default target. Use: make <specific_target>"

setup-env: --start-certservice-and-ejbca --run-certservice-clients --start-local-secured-ves

start-ves-client:
	docker-compose -f docker-compose-vesclient.yml up

restart-ves-client: --clean-ves-client start-ves-client

clean-all: --clean-ves-client --clean-env


--start-certservice-and-ejbca: --create-certservice-internal-certs --start-certservice-ejbca-containers --configure-ejbca

--start-certservice-ejbca-containers:
	docker-compose -f docker-compose-certservice-ejbca.yml up -d

--create-certservice-internal-certs:
	make -C resources/certs all

--configure-ejbca: --wait-for-ejbca --run-ejbca-script

--wait-for-ejbca:
	@echo 'Waiting for EJBCA... It may take a minute or two'
	until docker container inspect oomcert-ejbca | grep '"Status": "healthy"'; do sleep 3; done

--run-ejbca-script:
	docker exec oomcert-ejbca /opt/primekey/scripts/ejbca-configuration.sh

--run-certservice-clients: --create-client-volumes
	docker-compose -f docker-compose-certservice-clients.yml up -d
	@echo 'Waiting for client certifiactes...'
	@until ls -1 ./resources/certservice-client/client-volume-for-vesclient | grep "store" 1>/dev/null; do sleep 3; done
	@until ls -1 ./resources/certservice-client/client-volume-for-ves | grep "store" 1>/dev/null; do sleep 3; done
	@until ls -1 ./resources/certservice-client/client-volume-for-httpserver | grep "store" 1>/dev/null; do sleep 3; done

--create-client-volumes:
	mkdir -p ./resources/certservice-client/client-volume-for-vesclient  -m 777
	mkdir -p ./resources/certservice-client/client-volume-for-ves -m 777
	mkdir -p ./resources/certservice-client/client-volume-for-httpserver -m 777

--start-local-secured-ves:
	docker-compose -f docker-compose-ves-dmaap.yml up

--clean-ves-client:
	docker-compose -f docker-compose-vesclient.yml down
	rm -rf ./resources/certservice-client/client-volume-for-vesclient || true
	rm -rf ./resources/certservice-client/client-volume-for-httpserver || true


--clean-env:
	docker-compose -f docker-compose-ves-dmaap.yml down
	docker-compose -f docker-compose-certservice-clients.yml down
	rm -rf ./resources/certservice-client/client-volume-for-vesclient || true
	rm -rf ./resources/certservice-client/client-volume-for-ves || true
	rm -rf ./resources/certservice-client/client-volume-for-httpserver || true
	docker-compose -f docker-compose-certservice-ejbca.yml down
	make -C resources/certs clear
