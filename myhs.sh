#!/bin/bash
echo "Using:"
echo $1
echo $2
echo $3
echo $4
hadoop fs -rm -r -f $4
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files $1,$2 -mapper "$1" -reducer "$2" -input $3 -output $4