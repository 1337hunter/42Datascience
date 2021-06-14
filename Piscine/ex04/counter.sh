cp ../ex03/hh_positions.csv ./
tail -n +2 ./hh_positions.csv  | awk -F ',' 'BEGIN {
	arr["Junior"] = 0
	arr["Middle"] = 0
	arr["Senior"] = 0
}
{
	str = ""
	if ($3 ~ /Junior/)
		arr["Junior"] += 1
	if ($3 ~ /Middle/)
		arr["Middle"] += 1
	if ($3 ~ /Senior/)
		arr["Senior"] += 1
}
END {
	n = asorti(arr, sorted)
	print "\"name\",\"count\"" > "hh_uniq_positions.csv"
	for (i = n; i > 0; i--)
		print "\"" sorted[i] "\"," arr[sorted[i]] > "hh_uniq_positions.csv"

}' OFS=,
rm hh_positions.csv
