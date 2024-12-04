def validate_report(report):
    asc_report = sorted(report)
    desc_report = sorted(report, reverse=True)

    if report == asc_report or report == desc_report:
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i-1])
            if not (1 <= diff <= 3):
                return 0
        ## if it passes all conditions
        return 1
    else:
        return 0

results = []

with open("day2_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        line = line.strip()
        orig_report = list(map(int, line.split()))
        del_report = orig_report[:] ## make a copy of the original list for deletion

        for i in range(len(orig_report)):
            del_report.pop(i) ## delete 1 thing from the list based on index
            result = validate_report(del_report)
            if result == 1:
                results.append(result)
                break
            del_report = orig_report[:] ## reset the list back to the original state

print(sum(results))
