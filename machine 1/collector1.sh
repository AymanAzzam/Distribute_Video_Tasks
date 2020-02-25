#!/bin/bash

n=$(((($1 + 1))/2))
socket1=$2
socket2=$3
ip=$4

for (( i=0; i<$n; i++))
do
	python collector1.py $socket1 $socket2 $ip &
	socket1=$(($socket1 + 1))
	socket2=$(($socket2 + 1))
done
