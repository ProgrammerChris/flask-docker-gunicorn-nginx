# Flask in Docker (served by Gunicorn)

Simple boilerplate to get a flask app up and running in *Docker* using *Docker Compose* for easier scaling, and served with a *Gunicorn* HTTP server.
*The hot reload of flask in development mode it still working even if running in a Docker container. (Still detects changes to route.py and will reload server upon saving this file)*

## Tech used in this project:

- [Docker 2.0.0.3](https://github.com/docker) (Container magement system)
- [Docker-compose 1.23.2](https://github.com/docker/compose) (Container magement system)
- [Flask 1.0.2](http://flask.pocoo.org/) (Micro framework / web server)
- [Gunicorn 19.9.0](https://gunicorn.org/) (HTTP server)
- [Python 3.6.7](https://www.python.org/) (Language)
- [Python-dotenv 0.10.1](https://github.com/grauwoelfchen/flask-dotenv) (Easier environment control in .flaskenv)

## How to get up and running:

- git clone or download this repo.
- Download and install [Docker](https://www.docker.com/get-started)(*Docker-compose comes with docker desktop, so no need to install this individually*)
- Build and start the app: **docker-compose up --build**

The app is now running in development mode from your local ip at port 5000. Magic of docker!

To see the site, find your local ip, enter this in the browser and add port 5000. ex. *192.168.1.123:5000*

## How to change certain configs:
- To enable production mode, edit the **.flaskenv** file to say: **FLASK_ENV=production** (should not run flask directly in production mode, use a HTTP server for that, like *Gunicorn*. Look further down to see more.)
- To change port for the *flask app*: 
    - Locate the *Dockerfile* and replace the port number with the desired one.
    - Locate the *docker-compose* file and edit the port the flask app is to be run from inside the container. ex. *docker_port:new_flask_port*
- To change the prot on the *docker container*:
    - Locate *docker-compose* file and add new port. ex. *new_docker_port:flask_port*


## Running app in with [Gunicorn](https://gunicorn.org/) in Docker:
- Locate .flaskenv and replace *development* with *production*.
- Locate the *Dockerfile* and replace the *CMD* line with: CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]. (*run == run.py, app == "./app/"*)
  The app will then still be running on your local ip on port 5000 (ex. 192.168.1.123:5000), but with 4 working processes in Gunicorn in production mode.


# Disclamer❗️

This is by no means a "how to deploy and run a production website" kind of repo❗️
I take no responsibility for the use of this repo in production if choosen to do so❗️
There are no security in place for this app other than the built in stuff in the framworks, servers and containers❗️

Other than that, you are free to clone or make pull requests to this repo as you wish❗️

Happy coding 💻
