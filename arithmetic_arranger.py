def arithmetic_arranger(problems, show_answers):
    arranged_problems = []
    answers = []
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        components = problem.split()
        if len(components) != 3 or components[1] not in ["+", "-"]:
            return "Error: Invalid problem format."
        if (
            not components[0].isdigit()
            or not components[2].isdigit()
            or len(components[0]) > 4
            or len(components[2]) > 4
        ):
            return "Error: Numbers invalid."
        max_length = max(len(components[0]), len(components[2]))
        arranged_problem = ""
        if max_length == len(components[0]):
            arranged_problem += components[0].rjust(max_length + 2)
        else:
            arranged_problem += (
                " " * (max_length - len(components[0]) + 2) + components[0]
            )
        arranged_problem += "    "
        arranged_problem += components[1] + " " + components[2].rjust(max_length)
        arranged_problems.append(arranged_problem)
        if show_answers:
            if components[1] == "+":
                answer = str(int(components[0]) + int(components[2])).rjust(
                    max_length + 2
                )
            else:
                answer = str(int(components[0]) - int(components[2])).rjust(
                    max_length + 2
                )
            answers.append(answer)
        if show_answers:
            arranged_output = (
                "\n".join(arranged_problems)
                + "\n"
                + "-" * (max_length + 2)
                + "    "
                + "\n".join(answers)
            )
        else:
            arranged_output = "\n".join(arranged_problems)
    return arranged_output


problems = ["32 + 698", "3801 - 2", "45 + 43", "132 + 49"]
print(arithmetic_arranger(problems, True))
