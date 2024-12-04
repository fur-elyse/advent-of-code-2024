left_arr = []
right_arr = []
abs_diff_arr = []

with open("day1_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        line = line.strip()
        columns = line.split("   ")
        left_arr.append(int(columns[0]))
        right_arr.append(int(columns[1]))

left_arr.sort()
right_arr.sort()

for i in range(len(left_arr)):
    diff = abs(left_arr[i] - right_arr[i])
    abs_diff_arr.append(diff)

total_abs_diff = sum(abs_diff_arr)
print(total_abs_diff)