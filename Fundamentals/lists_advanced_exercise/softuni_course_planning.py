def check_lesson(input_list, name):
    if name in input_list:
        return True
    return False


lessons = input().split(", ")

command = input()

while command != "course start":
    command = command.split(":")
    command_word = command[0]

    if command_word == "Add":
        lesson = command[1]
        if not check_lesson(lessons, lesson):
            lessons.append(lesson)

    elif command_word == "Insert":
        lesson = command[1]
        insert_index = int(command[2])
        if not check_lesson(lessons, lesson):
            lessons.insert(insert_index, lesson)

    elif command_word == "Remove":
        lesson = command[1]

        if check_lesson(lessons, lesson):
            lessons.remove(lesson)
            exercise_name = f"{lesson}-Exercise"
            if exercise_name in lessons:
                lessons.remove(exercise_name)

    elif command_word == "Swap":
        first_lesson = command[1]
        second_lesson = command[2]
        if check_lesson(lessons, first_lesson) and check_lesson(lessons, second_lesson):
            first_lesson_index = lessons.index(first_lesson)
            second_lesson_index = lessons.index(second_lesson)
            lessons[first_lesson_index], lessons[second_lesson_index] = \
                lessons[second_lesson_index], lessons[first_lesson_index]

            first_exercise_name = f"{first_lesson}-Exercise"
            second_exercise_name = f"{second_lesson}-Exercise"

            if first_exercise_name in lessons and lessons.index(first_exercise_name) != lessons.index(first_lesson) + 1:
                lessons.remove(first_exercise_name)
                lessons.insert(lessons.index(first_lesson) + 1, first_exercise_name)

            if second_exercise_name in lessons and lessons.index(second_exercise_name)\
                    != lessons.index(second_lesson) + 1:
                lessons.remove(second_exercise_name)
                lessons.insert(lessons.index(second_lesson) + 1, second_exercise_name)

    elif command_word == "Exercise":
        lesson = command[1]
        exercise_name = f"{lesson}-Exercise"

        if check_lesson(lessons, lesson):
            lesson_index = lessons.index(lesson)
            lessons.insert(lesson_index + 1, exercise_name)

        else:
            lessons.append(lesson)
            lessons.append(exercise_name)

    command = input()

for position in range(1, len(lessons) + 1):
    print(f"{position}.{lessons[position - 1]}")
