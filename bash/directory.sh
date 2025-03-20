#! /bin/bash
 
# I'm going to create an echo showing today's date.

echo "Today is " `date`

echo -e "\n enter the path to directory:"
read the_path

echo -e "\n your path has the following files and folders: "
ls $the_path

