#!/bin/sh


tail -n +2 ../ex03/hh_positions.csv | awk -F ',' 'BEGIN {
	date=""
}
{
	split($2, arr, "T")
	temp_date = substr(arr[1], 2)

	if (date != temp_date)
	{
		date = temp_date
		print "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > date
	}
	print $0 > date
}'

