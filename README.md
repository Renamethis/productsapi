# Products API
Test task web application represents product managing system. App provides the API interface with 5 endpoints to interact with the products database. The application developed considerig Didenok-openapi.yaml OpenAPI specification.
## Tech
- Flask
- Pytest
- SQLAlchemy
- MySQL DBMS
- Celery task queue
- Redis DBMS
- Docker
## Deploy
Build and run docker containers:
```bash
docker-compose up -d --remove-orphans --build
```
Stop and remove docker containers:
```bash
docker-compose down --remove-orphans
```
Check all running containers:
```bash
docker ps -a
```
Check logs of docker-container:
```bash
docker logs --tail {amount of last rows} --follow --timestamps {container_name}
```
## Deploy
To execute test in docker container run:
```bash
docker exec -it flask python3 -m pytest tests
```
## Usage
To use the API, use Postman or Insomnia and make requests according to the given specification in the Didenok-openapi.yaml file. Route API adress: http://localhost:5000/