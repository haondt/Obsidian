# Obsidian
My home media server setup and configuration

Each of the following directories contain a `.env` file and a docker compose file. Configure the env file and deploy each on a seperate docker instance.
```
docker-media
docker-monitoring
docker-media-watcher
```

Find services available at the following:
| Url | Service |
|---|---|
| http://docker-media:8686 | lidarr |
| http://docker-media:9696 | prowlarr |
| http://docker-media-watcher:8181 | tautulli |
| http://docker-monitoring:9000 | portainer |
| http://docker-monitoring:3000 | grafana |
| http://docker-monitoring:8086 | influxdb |
| http://docker-monitoring:9090 | prometheus |
| http://docker-selfhosted:8080 | firefly-iii |
| http://docker-selfhosted:8081 | firefly-iii data importer |
