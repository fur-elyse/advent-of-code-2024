from collections import defaultdict

def check_order(test_case):
    for i in range(len(test_case)):
        if test_case[i] not in after_dict:
            continue
        for after in after_dict[test_case[i]]:
            if after in test_case and test_case.index(after) < i:
                return False
    return True

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
                if result:
                    total += test_case[len(test_case) // 2]
    print(total)