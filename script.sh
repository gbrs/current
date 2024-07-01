#!/bin/bash


while true
do
  read var1 var2 var3
  if [[ $var1 == exit ]]; then
    echo bye
    break
  elif [[ $var1 =~ ^[0-9]+$ ]]; then
    #read var2 var3
    if [[ $var2 = ** || $var2 = * || $var2 = + || $var2 = - || $var2 = / || $var2 = % ]]; then
      #echo 5
      #read var4
      let "ans=$var1 $var2 $var3"
      echo $ans
      continue
    else
      echo error
      break
    fi
  else
    echo error
    break
  fi
done
