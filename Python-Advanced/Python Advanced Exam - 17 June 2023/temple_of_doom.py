# 1. Create deques for tools, substances and temple chalanges

from collections import deque

tools = deque([int(num) for num in input().split()])
substances = deque([int(num) for num in input().split()])
chalanges = deque([int(num) for num in input().split()])

# 2. Create a loop while chalanges/else "Harry found an ostracon, which is dated to the 6th century BCE."

while chalanges:

  # 3. Break loop if not tools or substances/print: "Harry is lost in the temple. Oblivion awaits him."
  
  if not tools or not substances:
    print("Harry is lost in the temple. Oblivion awaits him.")
    break

  # 4. Find the result from the multiplication of first tool and last substance(use popleft / pop)
  
  current_tool = tools.popleft()
  current_substance = substances.pop()
  multiplication = current_tool * current_substance

  # 5. Check if the multiplication is in chalanges:
  # 5.1 if it is remove all tool substance chalange

  if multiplication in chalanges:
    chalanges.remove(multiplication)
    
  else:
     # 5.2  else increase the value of the tool element by 1 and move the element to the back of the tools’ sequence.
    current_tool += 1
    tools.append(current_tool)
    
     # 5.3 Decrease the value of the substance element by 1 and return the element to the substance’s sequence. If the value of the substance element reaches 0, remove it from the sequence.
    current_substance -= 1

    if current_substance != 0:
      substances.append(current_substance)
      
else:
  print("Harry found an ostracon, which is dated to the 6th century BCE.")

# 6 print non empty sequences

if tools:
  print(f"Tools: {', '.join([str(num) for num in tools])}")

if substances:
  print(f"Substances: {', '.join([str(num) for num in substances])}")

if chalanges:
  print(f"Challenges: {', '.join([str(num) for num in chalanges])}")
