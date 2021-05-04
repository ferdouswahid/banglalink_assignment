### Run Task C
1. open cmd 
2. goto the directory of code till Task-C. Please change the path accordingly.

```bash 
cd /banglalink_assignment/set-1/Task-C
ls
```


3. make sure you have docker

```
docker -v
```
4. run the docker container
```
docker-compose up -d
docker-compose ps
```


5. then call the url from browser or any http client to get response from docker container.
   
    production server url: `http://localhost:85/`   
    dev server url: `http://localhost:5011/`


