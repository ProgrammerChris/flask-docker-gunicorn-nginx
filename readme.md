# Flask in Docker (served with Gunicorn through Nginx)

Simple boilerplate to get a flask app up and running in *Docker* using *Docker Compose*, and served with a *Gunicorn* HTTP server through *Nginx* proxy. No HTTPS or HTTP/2 (yet).
*The hot reload of flask in development mode it still working even if running in a Docker container, served with Gunicorn through Nginx. (Still detects changes to route.py and will reload server upon saving this file)*

## Tech used in this project:

- [Docker 2.0.0.3](https://github.com/docker) (Container magement system)
- [Docker-compose 1.23.2](https://github.com/docker/compose) (Container magement system)
- [Flask 1.0.2](http://flask.pocoo.org/) (Micro framework)
- [Gunicorn 19.9.0](https://gunicorn.org/) (Application server)
- [Nginx 1.15.8](https://www.nginx.com/)
- [Python 3.6.7](https://www.python.org/) (Language)
- [Python-dotenv 0.10.1](https://github.com/grauwoelfchen/flask-dotenv) (Easier environment control in .flaskenv)

## How to get up and running in development mode:

- git clone or download this repo.
- Download and install [Docker](https://www.docker.com/get-started)(*Docker-compose comes with docker desktop, so no need to install this individually*)
- Build and start the app: **docker-compose up --build -d** (-d to run in background use *docker-compose down* to stop)

The app is now running in development mode from your local ip. ex. *192.168.1.123*

## To run in production mode:
- Edit the **.flaskenv** file to say: **FLASK_ENV=production**
- Remove the *--reload* from the run command in the *docker-compose.yml*

The app is now running in production mode from your local ip. ex. *192.168.1.123*

You can now choose to deploy to a server if you like.

# Disclamer❗️

I am NOT a professional devops engineer, developer or alike❗️ Take this repo with a grain of salt.

This is by no means a "how to deploy and run a production website" kind of repo❗️
I take no responsibility for the use of this repo in production if choosen to do so❗️
There are no security in place for this app other than the built in stuff in the framworks, servers and containers❗️

Other than that, you are free to clone or make pull requests to this repo as you wish❗️

Happy coding 💻
