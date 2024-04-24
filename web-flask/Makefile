.PHONY: compose-up
compose-up:
	@echo Starting docker compose
	@docker-compose -f tools/docker-compose.yml up -d

.PHONY: compose-down
compose-down:
	@echo Stopping docker compose
	@docker-compose -f tools/docker-compose.yml down

.PHONY: start-postgres
start-postgres: compose-up

.PHONY: stop-postgres  
stop-postgres: compose-down