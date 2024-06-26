# Maxscale Docker-Compose Setup Documentation

## Introduction

This README.md file provides documentation for setting up and running Maxscale with Docker-Compose. 
Before starinng the project open the command line and you will need to install:
`-`  Docker. 
`-` Docker-Compose.
`-` Python . 
`-` mysql.connector

### Docker installation:
for a succesfful `installation` use the steps on this link: 
[https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04]

### Docker-Compose
Install a were version of Docker-compose follo this link:
[https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-20-04-quickstart]

During the tutorial use this command to update to the newest version of docker-compose instead of the shown in the tutorial:

```
 $ sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Follow the rest of the tutorial to complete the installation. 


### Python install:
Use this commands to install python3 that will be used to run the .py file in file inside maxscale.
```
 $ sudo apt update
 $ sudo apt -y upgrade
 $ python3 -V
```

```
Output
Python 3.10.2+
```
To manage software packages for Python, let’s install pip
```
$ sudo apt install -y python3-pip
$ pip3 install package_name
$ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### Install mysql.connector
to run the sql file in maxscale you will need to install mysql.connecter
```
$ pip3 install mysql-connector
```

## Running 

To run MaxScale with Docker Compose, follow these steps:

1. Forked the repository as instructed in github.
2. Make a directory  of you choosing with this commands

   ```
   mkdir [directory name ] example: mkdir final_370
   
   ```
then change directory 
  ``
  cd final_370 
  ``

3. clone the forked repository in the command line inside the expample directory by entering
 
```
$ git clone https://github.com/Maravillosa30/CNE370-maxscale-docker/
```

4.  Navigate to CNE370-maxscale directory and open maxcale.

5. while inside maxscale, open the maxscale.cnf.d folder and edit and save  the example.cnf file with this command:
  ```
  $ sudo nano example.cnf
  ```

after that edit and save the docker-compose.yml file with this command:
  ```
  $ sudo nano docker-compose
  ```

6. Run docker-compose following this command:

``` 
$ sudo docker-compose up -d
```

the container should be running some server

This command will allow to see a better formated table for your server:

```
$ docker-compose exec maxscale maxctrl list servers
```

A list of servers will shows such as this one 
![alt text](https://github.com/Maravillosa30/CNE370-maxscale-docker/blob/master/Serversimage.png)







 

