from collections import defaultdict

left_arr = []
right_arr = []

with open("day1_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        line = line.strip()
        columns = line.split("   ")
        left_arr.append(int(columns[0]))
        right_arr.append(int(columns[1]))


freq_dict = defaultdict(int)
for i in right_arr:
    freq_dict[i] += 1

similarity_score_arr = []

for i in left_arr:
    if i in freq_dict:
        similarity_score_arr.append(i * freq_dict[i])

sim_score = sum(similarity_score_arr)
print(sim_score)