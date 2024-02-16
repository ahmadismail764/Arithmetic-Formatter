def arithmetic_arranger(problems, show_answers):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_line = []
    second_line = []
    dashed_line = []
    answer_line = []
    for problem in problems:
        components = problem.split()
        if len(components) != 3 or components[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        operand1, operator, operand2 = components[0], components[1], components[2]
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(operand1) == len(operand2):
            first_line.append(" " * 2 + operand1)
            second_line.append(operator + " " + operand2)
            dashed_line.append("-" * (len(operand1) + 2))
        elif len(operand1) > len(operand2):
            first_line.append(" " * 2 + operand1)
            second_line.append(
                operator + (" " * (len(operand1) - len(operand2) + 1)) + operand2
            )
            dashed_line.append("-" * (len(operand1) + 2))
        else:
            first_line.append(" " * (len(operand2) - len(operand1) + 2) + operand1)
            second_line.append(operator + " " + operand2)
            dashed_line.append("-" * (len(operand2) + 2))
        answer = (
            str(int(operand1) + int(operand2))
            if operator == "+"
            else str(int(operand1) - int(operand2))
        )
        answer_line.append(
            " " * (max(len(operand1), len(operand2)) - len(answer) + 2) + answer
        )
    for item in first_line:
        print(item, end=" " * 4)
    print()
    for item in second_line:
        print(item, end=" " * 4)
    print()
    for item in dashed_line:
        print(item, end=" " * 4)
    print()
    if show_answers:
        for item in answer_line:
            print(item, end=" " * 4)
