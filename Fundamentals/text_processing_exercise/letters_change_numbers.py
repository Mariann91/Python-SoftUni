lower_case_alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
upper_case_alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]

string_list = input().split()

result = []

for string in string_list:
  first_letter = string[0]
  number = int(''.join([num for num in string if num.isdigit()]))
  last_letter = string[-1]
  current_result = number
  
  if first_letter.isupper(): 
    divider = upper_case_alphabet.index(first_letter) + 1
    current_result = number / divider
  else:
    multiplier = lower_case_alphabet.index(first_letter) + 1
    current_result = number * multiplier
  
  if last_letter.isupper():
    subtracter = upper_case_alphabet.index(last_letter) + 1
    current_result = current_result - subtracter
  else:
    adder = lower_case_alphabet.index(last_letter) + 1
    current_result = current_result + adder

  result.append(current_result)

print(f"{sum(result):.2f}")
