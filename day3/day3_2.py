import re
import math


def multiply_values(mul_formulae):
    digits = re.sub("[^0-9,]","", mul_formulae)
    digits_split = digits.split(",")
    digits_list = list(map(int, digits_split))
    return math.prod(digits_list)


lines = []
with open("day3_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        lines.append(line.strip())
    
# join lines into 1 flat list
lines = ''.join(lines)

# extract all the do(), don't, mul(/d,/d) patterns
pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"
mul_lines = re.findall(pattern, lines)

values = []
do_multiplication = True

# over each matched pattern multiply the values if it's mul
for i in mul_lines:
    if i == "don't()":
        do_multiplication = False
    elif i == "do()":
        do_multiplication = True
    else:
        if do_multiplication:
            values.append(multiply_values(i))

total_value = sum(values)
print(total_value)