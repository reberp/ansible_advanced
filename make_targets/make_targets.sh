#!/bin/bash
#lil helper for making a few containers that I can run ansible against
echo "Creating $1 targets"
for ((i = 1 ; i <= $1; i++));
do
  # echo "$i"
  container_id=$(docker run -it -d ubuntu_22_ssh)
  ip=$(docker inspect -f'{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container_id)
  echo "target$i ansible_host=$ip ansible_ssh_pass=pat"
done
