# Read from the file file.txt and output the tenth line to stdout.
line_num=0
while a= read -r line
do 
    if test $line_num -eq  9
    then
        echo $line
    fi
    line_num=`expr $line_num + 1`
done < "file.txt"
if test $line_num -l
