#!/bin/bash

new_root_dir=/media/work/chromium/tarballs
root_dir=$PWD
while read line
do
    ( echo $line | grep ^Downloading: > /dev/null 2>&1 ) || continue
    line=$(echo $line | awk -F 'Downloading:' '{print $2}')
    directory=$(echo $line | awk -F ' -> ' '{print $1}')
    url=$(echo $line | awk -F ' -> ' '{print $2}')
    tarball=$(echo $line | awk -F ' -> ' '{print $3}')
    echo "[$directory] -> [$url]"

    cd "$root_dir"
    mkdir -p "$directory"
    cd "$directory"
#   wget "$url"
#   echo Inflating $PWD/$tarball
#   tar zxf $tarball
    mkdir -p $new_root_dir/$directory
    echo "Moving [$PWD/$tarball] -> [$new_root_dir/$directory/]"
    mv $PWD/$tarball $new_root_dir/$directory/
done < ./list.txt
