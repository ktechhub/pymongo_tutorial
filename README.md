# MongoDB

## Spin container
```sh
docker run -d -p 27017:27017 --name mongo mongo:latest
```
```sh
docker run -d \
    -p 27017:27017 \
    --name mongo \
    -v mongo-data:/data/db \
    -e MONGODB_INITDB_ROOT_USERNAME=mongo \
    -e MONGODB_INITDB_ROOT_PASSWORD=mongo \
    -e MONGO_INITDB_DATABASE=mongo \
    mongo:latest
```