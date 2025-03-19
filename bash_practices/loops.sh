#!/bin/bash

# While loop checks for a condition and loop until the condition remains true.

echo "'while' loop"
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))
done

# For loop allows to execute statements a specific number of times.

echo "'for' loop"
for i in {1..5}
do
 echo $i
done
