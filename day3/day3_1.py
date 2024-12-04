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

# extract all the mul(/d,/d) patterns
pattern = r"mul\(\d+,\d+\)*"
mul_lines = re.findall(pattern, lines)

# get the multiplied values of the matched patterns and get the summation of the multiplied values
multiplied_list = list(map(multiply_values, mul_lines))
total_multiplied = sum(multiplied_list)
print(total_multiplied)