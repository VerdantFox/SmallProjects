def get_int(statement, lower_bound, upper_bound):
    while True:
        try:
            integer = int(input(statement))
            if lower_bound <= integer <= upper_bound:
                break
            else:
                print("Please input an integer "
                      "between {} and {}.\n".format(lower_bound, upper_bound))
        except ValueError:
            print("Please input an integer "
                  "between {} and {}.\n".format(lower_bound, upper_bound))
    return integer


if __name__ == "__main__":

    variable_count = get_int("How many variables would you like to input? ",
                             1, 5,)

    variables = {}
    for i in range(variable_count):
        temp_var_name = input(
            "Give me a variable name for variable {}: ".format(i+1))
        temp_var_multiple = get_int("What multiple should {} "
                                    "appear on? (1-10) ".format(temp_var_name),
                                    1, 10)
        variables[temp_var_name] = temp_var_multiple

    count_to = get_int("What should I count up to? (1-1000 please) ", 1, 1000)

    multiplier = get_int("Count in multiples of what? (1-10) ", 1, 10)

    equalsNumber = False
    for i in range(multiplier, count_to + 1, multiplier):
        for variable in variables:
            if i % variables[variable] == 0:
                print(variable, end=" ")
                equalsNumber = True
        if equalsNumber is False:
            print(i)
        else:
            print()
        equalsNumber = False
