# Flask in Docker (served with Gunicorn through Nginx)

Simple boilerplate to get a flask app up and running in *Docker* using *Docker Compose* for easier scaling, and served with a *Gunicorn* HTTP server.
*The hot reload of flask in development mode it still working even if running in a Docker container. (Still detects changes to route.py and will reload server upon saving this file)*

## Tech used in this project:

- [Docker 2.0.0.3](https://github.com/docker) (Container magement system)
- [Docker-compose 1.23.2](https://github.com/docker/compose) (Container magement system)
- [Flask 1.0.2](http://flask.pocoo.org/) (Micro framework)
- [Gunicorn 19.9.0](https://gunicorn.org/) (Application server)
- [Nginx 1.15.8](https://www.nginx.com/)
- [Python 3.6.7](https://www.python.org/) (Language)
- [Python-dotenv 0.10.1](https://github.com/grauwoelfchen/flask-dotenv) (Easier environment control in .flaskenv)

## How to get up and running:

- git clone or download this repo.
- Download and install [Docker](https://www.docker.com/get-started)(*Docker-compose comes with docker desktop, so no need to install this individually*)
- Build and start the app: **docker-compose up --build -d** (-d to run in background use *docker-compose down* to stop)

The app is now running in development mode from your local ip at port 5000. Magic of docker! But not through Nginx!

To see the site, find your local ip, enter this in the browser and add port 5000. ex. *192.168.1.123:5000*

To see the site served through the Nginx proxy go to your local ip:8080. ex. *192.168.1.123:8080*

## How to change certain configs:
- To enable production mode, edit the **.flaskenv** file to say: **FLASK_ENV=production** (should not run flask directly in production mode by itself, use an HTTP server to serve the app. See further down)
- To change port for the *flask app*: 
    - Locate the *Dockerfile* and replace the port number with the desired one.
    - Locate the *docker-compose.yml* file and edit the port the flask app is to be run from inside the container. ex. *docker_port:new_flask_port*
- To change the port on the *docker container*:
    - Locate *docker-compose.yml* file and add new port. ex. *new_docker_port:flask_port*
- To change the port of the Nginx proxy, locate the *docker-compose.yml* and change the forwarding. ex. *new_port:80*

# Disclamer❗️

I am NOT a professional devops engineer, developer or alike❗️ Take this repo with a grain of salt.

This is by no means a "how to deploy and run a production website" kind of repo❗️
I take no responsibility for the use of this repo in production if choosen to do so❗️
There are no security in place for this app other than the built in stuff in the framworks, servers and containers❗️

Other than that, you are free to clone or make pull requests to this repo as you wish❗️

Happy coding 💻
