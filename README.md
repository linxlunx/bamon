# BAMON                    

BAMON is basic crud mongodb web service. The purpose of this project is that we can do all basic crud function dynamically in mongodb via web service. Tested in Ubuntu 16.04 & Ubuntu 18.04.

## REQUIREMENTS

### WITH DOCKER
- docker
- docker-compose

### WITHOUT DOCKER
- mongodb >= 3
- python >= 2.5

## INSTALLATION

### WITH DOCKER
```
$ docker-compose up --build
```

### WITHOUT DOCKER

## Install Mongodb
[Install Mongodb](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

## Install Dependencies
``` 
$ cd mongoapi/api
$ pip install -r requirements.txt
```

## Run Server
```
$ python index.py
```

### FEATURES

[INSERT DATA](#INSERT DATA)
[LIST DATA](#LIST DATA)
[GET SINGLE DATA](#GET SINGLE DATA)
[EDIT DATA](#EDIT DATA)
[DELETE DATA](#DELETE DATA)

## INSERT DATA

METHOD: POST

URL: http://[host]:[port]/[collection]/insert

Params: data
```
$ curl -d 'data={"name": "Robert", "country": "Germany"}' http://localhost:5000/users/insert
{
  "collection": "users", 
  "data": {
    "_id": "5b8f72adbffae1000b8f5c44", 
    "country": "Germany", 
    "name": "Robert"
  }
}
```

## LIST DATA

METHOD: GET

URL: http://[host]:[port]/[collection]
```
$ curl http://localhost:5000/users
{
  "collection": "users", 
  "data": [
    {
      "_id": "5b8f72adbffae1000b8f5c44", 
      "country": "Germany", 
      "name": "Robert"
    }, 
    {
      "_id": "5b8f72d4bffae1000b8f5c45", 
      "country": "Indonesia", 
      "name": "Anna"
    }
  ]
}
```
We can also filter with query string by field name. If the field is `name`, it will be using regex.
```
curl http://localhost:5000/users?name=An
{
  "collection": "users", 
  "data": [
    {
      "_id": "5b8f72d4bffae1000b8f5c45", 
      "country": "Indonesia", 
      "name": "Anna"
    }
  ]
}
```
Besides parameter `name`, other search paramaters will be match the document where the value of a field equals the specified value. You can also mix the parameters with multiple query string arguments.
```
$ curl http://localhost:5000/users?country=Indonesia
{
  "collection": "users", 
  "data": [
    {
      "_id": "5b8f72d4bffae1000b8f5c45", 
      "country": "Indonesia", 
      "name": "Anna"
    }
  ]
}
```
## GET SINGLE DATA

METHOD: GET

URL: http://[host]:[port]/[collection]/[id]
```
$ curl http://localhost:5000/users/5b8f72d4bffae1000b8f5c45
{
  "collection": "users", 
  "data": {
    "_id": "5b8f72d4bffae1000b8f5c45", 
    "country": "Indonesia", 
    "name": "Anna"
  }, 
  "id": "5b8f72d4bffae1000b8f5c45"
}
```
## EDIT DATA

METHOD: POST

URL: http://[host]:[port]/[collection]/[id]/edit

Params: data
```
$ curl -d 'data={"name": "Anni"}' http://localhost:5000/users/5b8f72d4bffae1000b8f5c45/edit
{
  "collection": "users", 
  "data": {
    "_id": "5b8f72d4bffae1000b8f5c45", 
    "country": "Indonesia", 
    "name": "Anni"
  }
}
```
## DELETE DATA

METHOD: GET

URL: http://[host]:[port]/[collection]/[id]/delete
```
$ curl http://localhost:5000/users/5b8f72d4bffae1000b8f5c45/delete
{
  "_id": "5b8f72d4bffae1000b8f5c45", 
  "collection": "users", 
  "status": "deleted"
}
```

## LICENSE
BSD / MIT