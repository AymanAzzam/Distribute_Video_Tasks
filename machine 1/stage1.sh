n=$1
port_in=$2
port_out=$3

for (( i=0; i<n; i++))
do
	echo "in the foor loop number " $i
	python stage1.py $port_in $port_out	
	if [ $(($i % 2))  -eq 0  -a $(($i -ne 0))]
	then
		port_out=$(($port_out + 1))
	fi
done