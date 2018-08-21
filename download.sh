#!/bin/bash

for i in $(cat $1)
do
				youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 $i
done
