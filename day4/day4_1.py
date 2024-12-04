import re

xmas = "XMAS"
pattern = r"(?={0})|(?={1})".format(xmas, xmas[::-1])
pattern_match = 0

word_search_arr = []
with open("day4_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        # get horizontal matches
        pattern_match += len(re.findall(pattern, line))
        
        # store each character into a list to represent it as a list of list
        word_search_arr.append(list(line.strip()))


# get vertical matches
word_search_arr_transpose = list(zip(*word_search_arr))
for i in word_search_arr_transpose:
    line = "".join(i)
    pattern_match += len(re.findall(pattern, line))

# get diagonal matches
# flatten the list
word_search_arr_flat = [i for line in word_search_arr for i in line]

row_count = len(word_search_arr)
col_count = len(word_search_arr_transpose)
total_count = row_count*col_count

# get the positions from the diagonal combinations
diag_1 = [[row for row in range(col, total_count, col_count+1)] for col in range(row_count, total_count-col_count, col_count)] + [[row for row in range(col, total_count, col_count+1)][:row_count-col] for col in range(0, row_count-1)]
diag_2 = [[row for row in range(col, 0, -col_count+1)] for col in range(row_count, total_count-col_count, col_count)] + [[row for row in range(col, 0, -col_count+1)][:row_count-i] for i, col in enumerate(range(total_count-col_count, total_count-1))]

# get any matching patterns for the diagonal strings
for positions in diag_1:
    line = "".join(map(lambda i: word_search_arr_flat[i], positions))
    pattern_match += len(re.findall(pattern, line))

for positions in diag_2:
    line = "".join(map(lambda i: word_search_arr_flat[i], positions))
    pattern_match += len(re.findall(pattern, line))

print(pattern_match)