#!/bin/sh
echo "starting..."
ids=$(docker ps -q)
for id in $ids
    do
    echo "$id"
    sudo docker kill $id
    done
