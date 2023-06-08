lessons = input().split(", ")

lesson = input()

while lesson != "course start":
    lesson = lesson.split(":")
    command = lesson[0]

    if command == "Add":
        lesson_name = lesson[1]
        if lesson_name not in lessons:
            lessons.append(lesson_name)

    elif command == "Insert":
        lesson_name = lesson[1]
        lesson_index = int(lesson[2])
        if lesson_name not in lessons:
            lessons.insert(lesson_index, lesson_name)

    elif command == "Remove":
        lesson_name = lesson[1]
        if lesson_name in lessons:
            lessons.remove(lesson_name)

    elif command == "Swap":
        lesson1_name = lesson[1]
        lesson2_name = lesson[2]
        lesson1_name_index = lessons.index(lesson1_name)
        lesson2_name_index = lessons.index(lesson2_name)
        if lesson1_name in lessons and lesson2_name in lessons:
            swap_help = lessons[lesson1_name_index]
            lessons[lesson1_name_index] = lessons[lesson2_name_index]
            lessons[lesson2_name_index] = swap_help

            

    else:
        lesson_name = lesson[1]
        if lesson_name in lessons:
            exercise_index = lessons.index(lesson_name) + 1
            lessons.insert(exercise_index, f"{lesson_name}-Exercise")
        else:
            lessons.append(lesson_name)
            lessons.append(f"{lesson_name}-Exercise")

    print(lessons)
    lesson = input()


#Data Types, Objects, Lists

#Arrays, Lists, Methods
