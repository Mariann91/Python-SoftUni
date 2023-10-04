def age_assignment(*args, **kwargs):
  age_info = {}
  
  for name in args:
    first_letter = name[0]

    if first_letter in kwargs:
      age_info[name] = kwargs[first_letter]

    sorted_list = sorted(age_info.items(), key=lambda  kvp: kvp[0])

  output = ""

  for item in sorted_list:
    output += f"{item[0]} is {item[1]} years old." + "\n"

  return output
