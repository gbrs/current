#!/bin/bash


while true
do
  read var1
  if [[ $var1 == exit ]]; then
    echo bye
    break
  elif [[ $var1 =~ ^[0-9]+$ ]]; then
    read var2 var3
    if [[ $var2 == + ]]; then
      #echo 5
      #read var4
      let ans=$var1+$var3
      echo $ans
      continue
    fi
  else
    echo error
    break
  fi

    #"+", "-", "*", "/", "%", "**"
    #gcd $var1 $var2
    #313788397 2546698687
    #echo GCD is $answer
    #read var1 var2
done
