list=$(ls)
touch hh_positions.csv
echo '"id","created_at","name","has_test","alternate_url"' > hh_positions.csv
for i in $list
do
	match=$(echo $i | sed -n '/^[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]/p')
	if [ ! -z $match ]
	then
		tail -n +2 $match >> hh_positions.csv
	fi
done
