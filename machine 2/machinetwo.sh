if (( $(ps -eo comm,pid,etimes | awk '/^ZMQbg/ { print $2}' | wc -l) > 0 ))
then
	#kill -9 $(ps -eo comm,pid,etimes | awk '/^ZMQbg/ {if ($3 > 300) { print $2}}')
	kill -9 $(ps -eo comm,pid,etimes | awk '/^ZMQbg/ { print $2}')
fi



# number of consumers 
n=$1
novertwo=$(((($1 + 1))/2))
# ip of machine 1
ip=$2

socket1_stage2=6000
socket2_stage2=$(($socket1_stage2 + $novertwo))
echo "socket stage is initially $socket2_stage2"

for (( i=1; i<=$n; i++))
do
	python3 stage2.py $socket1_stage2 $socket2_stage2 $ip &
	if [ $(($i % 2))  -eq 0 ]
	then
		socket1_stage2=$(($socket1_stage2 + 1))
	fi
done

python3 collector2.py $socket2_stage2 &
