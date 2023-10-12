def gather_credits(number_of_credits, *args):
  credits = 0
  courses = []
  
  for course_name, course_credits in args:
    if credits >= number_of_credits:
       break
       
    if course_name in courses:
      continue
      
    courses.append(course_name)
    credits += course_credits
    
  if credits >= number_of_credits:
    return f"""Enrollment finished! Maximum credits: {credits}.
Courses: {', '.join(sorted(courses))}"""
  else:
    return f"You need to enroll in more courses! You have to gather {number_of_credits - credits} credits more."
