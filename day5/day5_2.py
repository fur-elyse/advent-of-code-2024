from collections import defaultdict

def check_order(test_case):
    for orig_index in range(len(test_case)):
        if test_case[orig_index] not in after_dict:
            continue
        for after in after_dict[test_case[orig_index]]:
            if after in test_case and test_case.index(after) < orig_index:
                return False
    return True

def correct_order(test_case):
    for orig_index in range(len(test_case)):
        new_index = orig_index
        if test_case[orig_index] in after_dict:
            for after in after_dict[test_case[orig_index]]:
                if after in test_case and test_case.index(after) < orig_index:
                    new_index = min(new_index, test_case.index(after))
            test_case[orig_index], test_case[new_index] = test_case[new_index], test_case[orig_index]

total = 0
is_rule = True
after_dict = defaultdict(list)


with open("day5_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        line = line.strip()
        if len(line) < 1:
            is_rule = False
        else:
            if is_rule:
                before, after = list(map(int, line.split("|")))
                if before in after_dict:
                    after_dict[before].append(after)
                else:
                    after_dict[before] = [after]
                
            else:
                test_case = list(map(int, line.split(",")))
                result = check_order(test_case)
                if not result:
                    while not check_order(test_case):
                        correct_order(test_case)
                    total += test_case[len(test_case) // 2]
    print(total)