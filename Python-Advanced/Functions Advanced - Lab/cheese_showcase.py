def sorting_cheeses(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for name, values in sorted_list:
        result += name + "\n"
        sorted_values = sorted(values, reverse=True)

        for value in [str(el) for el in sorted_values]:
            result += value + "\n"

    return result
