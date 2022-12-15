# Obsidian
My home media server setup and configuration

Each of the following directories contain a `.env` file and a docker compose file. Configure the env file and deploy each on a seperate docker instance.
```
docker-media
docker-monitoring
``` 

Find services available at the following:
| Url | Service |
|---|---|
| http://docker-monitoring:9000 | portainer |
| http://docker-monitoring:3000 | grafana |
| http://docker-monitoring:8086 | influxdb |
| http://docker-media:8686 | lidarr |
