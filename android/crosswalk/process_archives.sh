#!/bin/bash

new_root_dir=/media/work/tarballs_crosswalk/all
root_dir=$PWD

while read line
do
    ( echo $line | grep ^Downloading: > /dev/null 2>&1 ) || continue
    line=$(echo $line | awk -F 'Downloading:' '{print $2}')
    directory=$(echo $line | awk -F ' -> ' '{print $1}')
    tarball=$(echo $line | awk -F ' -> ' '{print $2}')
    url=$(echo $line | awk -F ' -> ' '{print $3}')
    echo "[$directory] -> [$url] -> [$tarball]"

#   cd "$root_dir"
#   mkdir -p "$directory"
#   cd "$directory"
#   wget "$url"

    cd $root_dir
    cd $directory
    echo Inflating $directory/$tarball
    tar zxf $tarball

#   mkdir -p $new_root_dir/$directory
#   echo "Moving [$directory/$tarball] -> [$new_root_dir/$directory/]"
#   cp $directory/$tarball $new_root_dir/$directory/
done < ./downloader.log.2
