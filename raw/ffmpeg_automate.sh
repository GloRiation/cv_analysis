#!bin/bash

csv_file="../ffmpeg_automate_filename.csv"

while IFS= read -r line; do
	echo "$line"
	eval "$line"
done < $csv_file	
