#!/bin/bash
clear

dir=""

cur_dir=$(pwd)
echo "Your current Directory is $cur_dir"
if [ "$HOME" != "$cur_dir" ]
	then 
        echo "You are not  your home directory"
	else 
        echo "You are c in your home directory"
fi

#Start Loop
while [ "$dir" = "" ]
do
	echo -n "Please give the file name to be short-cutted: "
	read shortcut

	dir=$(sudo find ~ -name "$shortcut")
	if [ "$dir" = "" ]
	    then 
            echo "The file does not exist"
	    else
            echo "The file exists"	
    fi
done

ln -s "$dir" -t $HOME/Desktop
links=$(sudo find . -type l -print | wc -l)
echo  "Number of Symbolic Links in the current directory: $links"
echo "These are all of the Symbolic Links/Shortcuts in the current directory:"
sudo find . -type l
echo "These are all of the locations the Symbolic Links/Shortcuts are attached too:"
readlink -f *
