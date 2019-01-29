#https://leetcode.com/problems/valid-phone-numbers/
file="file.txt"
regex="^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
alternate="^\([0-9^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$"
while IFS= read -r line
do
    if [[ "$line" =~ $regex || "$line" =~ $alternate ]]
    then
        echo $line
    fi

done < "$file"
