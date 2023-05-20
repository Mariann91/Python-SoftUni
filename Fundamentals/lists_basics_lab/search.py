interval, key_word = int(input()), input()

all_courses = [input() for _ in range(interval)]
key_word_list = [course for course in all_courses if key_word in course]
print(f"{all_courses}\n{key_word_list}")
