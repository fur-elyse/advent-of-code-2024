def compute_equation(value, numbers):
    if numbers[0] > value:
        return False
    if len(numbers) == 1 and numbers[0] == value:
        return True
    if (compute_equation(value, [numbers[0] + numbers[1]] + numbers[2:])):
        return True
    if (compute_equation(value, [numbers[0] * numbers[1]] + numbers[2:])):
        return True
    if (compute_equation(value, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])):
        return True
    return False


calibration_result = 0

with open("day7_input.txt") as r:
    for line in r:
        value, raw_equation = line.strip().split(": ")
        value = int(value)
        equation = list(map(int, raw_equation.split(" ")))
        print(value, equation)
        if compute_equation(value, equation):
            calibration_result += value
print(calibration_result)