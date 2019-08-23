## Build
```
docker build --build-arg arch=$(dpkg --print-architecture) -t jiesu/git-repo-list:$(date +%Y%m%d%H%M)-$(dpkg --print-architecture) .
```

## Run
```
docker run -d -v /path/to/repos:/repos -p 8888:8888 --name git-repo-list jiesu/git-repo-list:<version>
```

## REST Call
```
curl http://<hostname>:8888
```

