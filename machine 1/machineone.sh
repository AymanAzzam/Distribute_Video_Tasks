if (( $(ps -eo comm,pid,etimes | awk '/^ZMQbg/ { print $2}' | wc -l) > 0 ))
then
	kill -9 $(ps -eo comm,pid,etimes | awk '/^ZMQbg/ { print $2}')
fi

#machine one shell script

#echo "starting Machine1 script "

n=$1
#echo "the number of Consumers is $n" 

directory=$2
#echo  "the directory is  $directory"

port_in=5557
port_out=5558
#ip of machine 2
host=$3

temp_port_in=$port_out

#echo "port_in is $port_in"
#echo "starting port_out is $port_out" 
 
python3 producer.py $directory &

for (( i=0; i<$n; i++))
do
	#echo "in the foor loop number " $i
	python3 stage1.py $port_in $port_out &
	if [ $(($i % 2))  -eq 1 ]
	then
		port_out=$(($port_out + 1))
	fi
done

./collector1.sh $n $temp_port_in 6000 $host &
