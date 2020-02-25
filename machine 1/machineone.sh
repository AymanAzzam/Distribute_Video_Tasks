#machine one shell script

echo "starting the script "

n=$1
echo "the number of frames is $n" 

directory=$2
echo  "the directory is  $directory"

port_in=5557
port_out=5558
host=$3

temp_port_in=$port_out

echo "port_in is $port_in"
echo "starting port_out is $port_out" 
 

python producer.py $directory &

for (( i=0; i<$n; i++))
do
	echo "in the foor loop number " $i
	python stage1.py $port_in $port_out &
	if [ $(($i % 2))  -eq 1 ]
	then
		port_out=$(($port_out + 1))
	fi
done

./collector1.sh $n $temp_port_in 6000 $host
