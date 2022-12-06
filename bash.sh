# задания из https://stepik.org/course/73/syllabus

3.2.1
#!/bin/bash
echo "Arguments are: \$1=$1 \$2=$2"

3.3.1
#!/bin/bash
case $1 in
    0)
        echo "No students"
        ;;
    1)
        echo "1 student"
        ;;
    2)
        echo "$1 students"
        ;;
    3)
        echo "$1 students"
        ;;
    4)
        echo "$1 students"
        ;;
    *)
        echo "A lot of students"
        ;;
esac

3.3.2
#!/bin/bash
while [ 0==0 ]
do
    echo "enter your name:"

    read name
    if [ -z $name ]
    then break
    fi
    echo "enter your age:"

    read age
    if [ $age -eq 0 ]
    then break
    fi

    if [[ $age -le 16 ]]
    then group='child'
    elif [[ $age -le 25 ]]
    then group='youth'
    else group='adult'
    fi

    echo "$name, your group is $group"
done

echo "bye"


3.4.1
#!/bin/bash
qcd()
{
    if [[ ($1 -eq $2) ]] || [[ ($1 -eq 0) ]]
    then
        answer=$2
    else
        let "temp = $2 % $1"
        qcd $temp $1
    fi
}


read var1 var2
while [[ -n $var1 ]]
do
    qcd $var1 $var2
    #313788397 2546698687
    echo GCD is $answer
    read var1 var2
done

echo bye



