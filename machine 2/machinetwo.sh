n=$1
novertwo=$(((($1 + 1))/2))

socket1_collect=5558
echo "socket 1 is initially $socket1_collect"

socket2_collect=$(((($socket1_collect)) + (($novertwo))))
echo "socket 2 is initially $socket2_collect"

socket2_collect_temp=$socket2_collect

for (( i=0; i<$novertwo; i++))
do
	python collector1.py $socket1_collect $socket2_collect &
	socket1_collect=$(($socket1_collect + 1))
	socket2_collect=$(($socket2_collect + 1))
done

socket1_stage2=$socket2_collect_temp
socket2_stage2=$(((($socket1_stage2)) + (($novertwo))))
echo "socket stage is initially $socket2_stage2"

for (( i=1; i<=n; i++))
do
	python stage2.py $socket1_stage2 $socket2_stage2	&
	if [ $(($i % 2))  -eq 0 ]
	then
		socket1_stage2=$(($socket1_stage2 + 1))
	fi
done

python collector2.py $socket2_stage2
