unzip:
	cd input; unzip \*.zip
	cd input/2015; unzip \*.zip

output/weather.csv:
	mkdir -p output
	bpython src/process.py
output/station.csv: output/weather.csv
output/status.csv: output/weather.csv
output/trip.csv: output/weather.csv

working/no_header/station.csv: output/station.csv
	mkdir -p working/no_header
	tail +2 $^ > $@

working/no_header/status.csv: output/status.csv
	mkdir -p working/no_header
	tail +2 $^ > $@

working/no_header/trip.csv: output/trip.csv
	mkdir -p working/no_header
	tail +2 $^ > $@

working/no_header/weather.csv: output/weather.csv
	mkdir -p working/no_header
	tail +2 $^ > $@

output/database.sqlite: working/no_header/station.csv working/no_header/status.csv working/no_header/trip.csv working/no_header/weather.csv
	-rm output/database.sqlite
	sqlite3 -echo $@ < src/import.sql
db: output/database.sqlite

output/hashes.txt: output/database.sqlite
	-rm output/hashes.txt
	echo "Current git commit:" >> output/hashes.txt
	git rev-parse HEAD >> output/hashes.txt
	echo "\nCurrent input/ouput md5 hashes:" >> output/hashes.txt
	md5 output/*.csv >> output/hashes.txt
	md5 output/*.sqlite >> output/hashes.txt
	md5 input/*.zip >> output/hashes.txt
	md5 input/201402_babs_open_data/* >> output/hashes.txt
	md5 input/201408_babs_open_data/* >> output/hashes.txt
	md5 input/2015/* >> output/hashes.txt
hashes: output/hashes.txt

release: output/hashes.txt
	cp -r output bay-area-bike-share
	zip -r -X output/bay-area-bike-share-`date -u +'%Y-%m-%d-%H-%M-%S'` bay-area-bike-share/*
	rm -rf bay-area-bike-share

all: release

clean:
	rm -rf working
	rm -rf output
