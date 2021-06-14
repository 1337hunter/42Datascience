cp ../ex00/hh.json ./
jq -r -f ./filter.jq hh.json > hh.csv
rm ./hh.json
