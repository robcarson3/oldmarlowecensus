# Example Cron Job to Run Deploy Script every 5 minutes
# */5 * * * * cd /root/bookcensus && ./git_redeploy.sh
set -o errexit

# try to pull from github
git_status="$(git pull origin main)"
echo $git_status

if [[ $git_status == *"Updating"* ]]; then
  echo "Updating App and redeploying"
elif [[ $git_status == *"Already up-to-date."* ]]; then
  echo "Up-to-date with git repository"
  exit
else
  echo "Unable to pull new version from git"
  echo $git_status
  exit
fi

# build new docker image
docker_build="$(docker-compose -f production.yml build)"

if [[ $docker_build == *"Successfully built"* ]]; then
  echo "docker successfully built"
else
  echo "error building docker container"
  echo "$docker_build"
  exit
fi

# bring down old container
docker_down="$(docker-compose -f production.yml down)"

# run new container
docker_up="$(docker-compose -f production.yml up)"
