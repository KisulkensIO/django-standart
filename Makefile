.DEFAULT_GOAL=start

# Setup environment commands by specific shell (Powershell or Bash)
ifeq ($(OS),Windows_NT)
    COPY_ENV=xcopy .env.dist .env /D /I
    WSL=wsl
else
	COPY_ENV=cp -n .env.dist .env
endif

start:
	$(COPY_ENV)
	$(WSL) docker compose -f docker-compose.debug.yml up --build
.PHONY=start

stop:
	$(WSL) docker compose -f docker-compose.debug.yml down --rmi local --remove-orphans -v
.PHONY=stop
