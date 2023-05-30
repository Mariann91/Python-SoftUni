interval = int(input())
START = 97
end = START + interval

for chr1 in range(START, end):
  for chr2 in range(START, end):
    for chr3 in range(START, end):
      print(f"{chr(chr1)}{chr(chr2)}{chr(chr3)}")
      
