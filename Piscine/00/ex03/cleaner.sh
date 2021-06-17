cp ../ex02/hh_sorted.csv ./
head -n 1 ./hh_sorted.csv > hh_positions.csv
tail -n +2 ./hh_sorted.csv | awk -F ',' '{
	str = ""
	if ($3 ~ /Junior/)
		str = "\"Junior"
	if ($3 ~ /Middle/)
		str = (str == "" ? "\"Middle" : (str "/Middle"))
	if ($3 ~ /Senior/)
		str = (str == "" ?  "\"Senior" : (str "/Senior"))
	if (str != "")
		$3 = str "\""
	else
		$3 = "\"-\""
} 1' OFS=, >> hh_positions.csv;

#paste <(awk -F ',' '{print $3}' ../ex02/hh_sorted.csv ) <( awk -F ',' '{print $3}' hh_positions.csv);

rm hh_sorted.csv
