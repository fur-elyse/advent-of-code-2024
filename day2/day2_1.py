def validate_report(report):
    asc_report = sorted(report)
    desc_report = sorted(report, reverse=True)

    if report == asc_report or report == desc_report:
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i-1])
            if 1 <= diff <= 3:
                pass
            else:
                return 0
            
        return 1
    else:
        return 0

results = []

with open("day2_input.txt", "r", encoding="utf-8") as txt_file:
    for line in txt_file:
        line = line.strip()
        report = list(map(int, line.split()))
        result = validate_report(report)
        results.append(result)

print(sum(results))