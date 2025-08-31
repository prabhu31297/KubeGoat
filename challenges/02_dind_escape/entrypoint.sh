#!/bin/sh
set -e

dockerd &

until docker info >/dev/null 2>&1; do
  sleep 1
done


docker volume create kg_flag >/dev/null
docker run --rm -v kg_flag:/mnt alpine sh -lc 'echo "FLAG{dind_docker_exposed_privilege}" > /mnt/flag.txt'



python3 /app/app.py