cp ../ex01/hh.csv ./
head -n 1 hh.csv > hh_sorted.csv
tail -n +2 hh.csv | sort -t ',' -k2,2 -k1,1r >> hh_sorted.csv
rm -rf hh.csv
