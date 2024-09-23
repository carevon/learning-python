# CONTRIBUTING

## How to run the Dockerfile locally

-- Build the image 
```
docker build -t flask-smorest-api .
```

-- Run the container locally
```
docker run -dp 5005:5000 flask-smorest-api
```

-- Run docker compose to create both web and database services
```
docker compose up -d --build --force-recreate --no-deps
```

-- Run the rq worker
```
docker run -w /app flask-smorest-api sh -c "rq worker -u REDIS_URL_HERE emails"
```

Ater deplyoying the three containers, access the application through the localhost:5000/swagger-ui to check the endpoints documentation
