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