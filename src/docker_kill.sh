#!/bin/sh
echo "starting..."
ids=$(docker ps -q)
for id in $ids
    do
    echo "$id"
    docker kill $id
    done
