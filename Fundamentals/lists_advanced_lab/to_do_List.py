to_do_list = [0] * 10

task = input()

while task != "End":
    task = task.split("-")
    importance = int(task[0])
    index = importance - 1
    to_do_list[index] = task[1]
    task = input()

print([task for task in to_do_list if task != 0])
