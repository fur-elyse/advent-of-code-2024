import re

xmas = "MAS"
pattern = r"(?={0})|(?={1})".format(xmas, xmas[::-1])
pattern_match = 0

word_search_arr = []
with open("day4_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        # store each character into a list to represent it as a list of list
        word_search_arr.append(list(line.strip()))

# get diagonal matches
# flatten the list
word_search_arr_flat = [i for line in word_search_arr for i in line]

row_count = len(word_search_arr)
col_count = len(word_search_arr[0])
total_count = row_count*col_count

# get the positions from the diagonal combinations
diag_1 = [[row for row in range(col, total_count, col_count+1)] for col in range(row_count, total_count-col_count, col_count)][::-1] + [[row for row in range(col, total_count, col_count+1)][:row_count-col] for col in range(0, row_count-1)]
diag_2 = [[row for row in range(col, 0, -col_count+1)] for col in range(row_count, total_count-col_count, col_count)] + [[row for row in range(col, 0, -col_count+1)][:row_count-i] for i, col in enumerate(range(total_count-col_count, total_count-1))]


def get_a_coordinates(lines):
    results = []
    
    for positions in lines:
        # get the string of the line based on the positions and find any matching patterns
        line = "".join(word_search_arr_flat[i] for i in positions)
        matches = [m.start(0) for m in re.finditer(pattern, line)]
        
        # get the coordinates of a for those that did match
        coordinates = [(positions[m + 1] % col_count, positions[m + 1] // col_count) for m in matches if m + 1 < len(positions)]
        
        if len(coordinates) > 0:
            results.append(coordinates)
    
    return results

# flatten the list so it can be converted into a set
diag_1_coordinates = [i for line in get_a_coordinates(diag_1) for i in line]
diag_2_coordinates = [i for line in get_a_coordinates(diag_2) for i in line]

print(len(set(diag_1_coordinates) & set(diag_2_coordinates)))
