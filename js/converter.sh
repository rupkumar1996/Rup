#!/bin/bash
i=0
lines=`wc -l < $1`
echo "const shooppableItems = ["
while read line || [[ -n "$line" ]]; do
	let "i++"
	IFS=',' read -r -a array <<< "$line"
	if [ ${#array[@]} -ne 4 ]
	then 
		echo "Illegal number of columns in row $i"
	else
		echo -e "\t{"
		echo -e "\t\tid: \"$i\","
		echo -e "\t\timage: \"${array[0]}\","
		echo -e "\t\tprice: \"${array[1]}\","
		echo -e "\t\tname: \"${array[2]}\","
		echo -e "\t\tmerchantName: \"${array[3]}\","
		# echo ${some:0:${#some}-1}
		some=${array[4]}
		echo -e "\t\tviewproductUrl: \"${some:0:${#some}-1}\"";


		if [ $i -ne $lines ]
		then
			echo -e "\t},"
		else
		 	echo -e "\t}"
		fi
	fi
done < "$1"
echo ']'