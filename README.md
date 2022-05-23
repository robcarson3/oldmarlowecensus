# Marlowe Census

## Prerequisites

You need to having the following programs setup on your system before
trying to install/run this project.

1. Python3
2. Docker ([Installation](https://docs.docker.com/get-docker/))
3. Git



## Local Installation
1. Clone the repo from Github.
```bash
git clone https://github.com/robcarson3/marlowecensus.git
```

2. Change into the project directory
```bash
cd marlowecensus
```

3. Generate environment variable .env files by running the following command.
```bash
python manage.py envs_generator.py
```

4. Build the docker container
```bash
docker-compose -f local.yml build
```

5. After the docker container is done building, spin up the container
```bash
docker-compose -f local.yml up
```

6. (Optional) Skip this step if you do not want to import data from a database backup. Open a new terminal window and 
navigate to the project directory and run the following command.

```bash
docker exec -it marlowecensus_django_1 python3 manage.py loaddata dump.json 
```

7. Open a browser window and navigate to [http://0.0.0.0:8000](http://0.0.0.0:8000)

8. To stop running the docker container, press "CTRL + C"


## Local Development

### Run Commands on Docker Containers
Open a new terminal window and navigate to the project directory. Enter the command below to create a django superuser.
```bash
docker exec -it marlowcensus_django_1 python manage.py createsuperuser
```

You can replace the "marlowcensus_django_1" with a different container.
You can replace "python manage.py createsuperuser" with any other command you might want to run on the specified container.

## Reclaim Hosting

### Deploy Process
There is a cronjob set to run every 5 minutes that checks github to see if there are any revisions and if there are, it 
will build a new container, spin down the old one and spin up the new one. 

The cronjob can be disabled if you want deploy new builds manually. It is located in ```/var/spool/cron/root```. Just 
delete ```*/5 * * * * cd /root/bookcensus && ./git_redeploy.sh``` and save the file to disable the cronjob. 

The ```git_redeploy.sh``` script can still be used to manually redeploy the app. To do so, move into the project 
directory and enter ``` ./git_redeploy.sh``` in the command line.   


## Other

### Commonly Used Commands
Open the Django Shell
```bash
docker exec -it marlowcensus_django_1 python3 manage.py shell
```

Export the Database to a JSON file. Change "db_dump" to whatever you would like to name the file. Make sure you do not
unintentionally overwrite an existing export.
```bash
docker exec -it marlowcensus_django_1 python3 manage.py dumpdata db_dump.json
```

Import the Database from a JSON file export
```bash
docker exec -it marlowcensus_django_1 python3 manage.py loaddata dump.json
```

### Resources

#### Git / Github
- [Github Tutorial for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Oh Shit, Git!?!](https://ohshitgit.com/) When you mess something up with git and need to undo changes

#### Docker
- [Docker Simplified: A Hands-On Guide for Absolute Beginners](https://www.freecodecamp.org/news/docker-simplified-96639a35ff36/)
- [Docker Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)

#### Django
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Django Cheatsheet](https://dev.to/ericchapman/my-beloved-django-cheat-sheet-2056)
- [Django Template Language](https://docs.djangoproject.com/en/3.2/ref/templates/language/)

#### HTML / CSS
- [HTML Cheatsheet](https://web.stanford.edu/group/csp/cs21/htmlcheatsheet.pdf)
- [CSS Cheatsheet](https://adam-marsden.co.uk/css-cheat-sheet)
- [Bootstrap 4 Docs](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

#### Cron
- [Cron Cheatsheet](https://devhints.io/cron)

#### Bash Scripting / Command Line
- [Bash Scripting Cheatsheet](https://devhints.io/bash)
