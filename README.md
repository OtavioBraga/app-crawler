# App Crawler - #vanhackathon #appsamurai

This application was made for a chalenge on vanhackathon. The main goal is to extract information from App Store charts on available some countries and display the ranking for the user. Due the short time for the coding, only the extractor for AppStore has been implemented. 

The AppStore class can do the following actions:
 - Get the top 100's paid apps
 - Get the top 100's free apps
 - Get info from a app 
 - Get the global ranking from app

## Instalation guide

To install and test this application, you'l need just two dependencies:
 - Docker
 - Docker compose
#### Installing Docker and Docker compose

It's recommended to folow the guide for installing Docker and Docker compose directly on the site:
 - **Docker** https://docs.docker.com/engine/installation/
 - **Docker compose** https://docs.docker.com/compose/install/

### Running the application

Once you have installed Docker and Docker compose, just clone this repo and cd into the folder. Inside the folder, just enter the following command on bash.

```bash
docker-compose up
```

**Wait until Docker finish his processes and head to http://0.0.0.0:5000**
