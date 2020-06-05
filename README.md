# cluster-api

simple server to expose pseudo rest api described by api.http file

api inspired from databricks api

data when starting are provided by cluster.list.json

## launch server manually

### install requirements

```
pip install -r requirements.txt
```

### launch the server

```
python server.py
```

## launch with docker

### build the docker image

```
docker build --tag <an_image_name> .
```

### run a conatainer

```
docker run --name <a_container_name> -p 8080:8080 <an_image_name>
```
  
## access to the server

go to: http://localhost:8080
