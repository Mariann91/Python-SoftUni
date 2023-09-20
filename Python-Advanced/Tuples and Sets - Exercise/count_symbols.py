text = list(input())

count_symbols = {}
      
for symbol in text:

  count_symbols[symbol] = text.count(symbol)

for symbol in sorted(count_symbols):
  print(f"{symbol}: {count_symbols[symbol]} time/s")
