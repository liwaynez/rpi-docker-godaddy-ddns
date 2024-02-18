#!/bin/sh
echo "Trying to kill docker processes..."
ids=$(docker ps -q)
for id in $ids
    do
    echo "$id"
    sudo docker kill $id
    done
