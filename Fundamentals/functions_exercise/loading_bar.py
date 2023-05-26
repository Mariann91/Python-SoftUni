def loading(percent):
    percent_times = percent // 10
    loading_bar = ["."] * 10

    for i in range(percent_times):
        loading_bar[i] = "%"

    if loading_bar.count("%") < 10:
        return f"{percent}% [{''.join(loading_bar)}]\nStill loading..."
    else:
        return f"{percent}% Complete!\n[{''.join(loading_bar)}]"


loading_percent = int(input())
print(loading(loading_percent))
