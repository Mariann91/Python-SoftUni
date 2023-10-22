def students_credits(*args):
    credits_dict = {}
    total_credits = 0
    result = ""

    for current_course in args:
        course, course_credits, max_points, points = [int(el) if el.isdigit() else el for el in current_course.split("-")]
        current_credits = points / max_points * course_credits
        credits_dict[course] = current_credits
        total_credits += current_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma."

    sorted_credits_dict = sorted(credits_dict.items(), key=lambda kvp: (kvp[1]), reverse=True)

    for item in sorted_credits_dict:
        result += f"\n{item[0]} - {item[1]:.1f}"

    return result
  
