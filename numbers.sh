#!/bin/bash

# This automation will tell if the number is positive, negative or zero.

echo "Please enter a number:"
read num

if [ $num > 0 ]; then
 echo "$num is positive"

 elif [ $num < 0 ]; then
  echo "$num is negative"

 else
  echo "$num is zero"
fi

