#!/bin/bash
sm=1
for i in {1..1800}
do
  let "sm+=1"
  sleep 2
done
echo $sm
