#!/bin/sh
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
sudo docker build -t echo/envoy -f ./envoy.Dockerfile .
sudo docker run -d -p 8080:8080 -p 9901:9901 echo/envoy
sleep 1
sudo docker ps -a
