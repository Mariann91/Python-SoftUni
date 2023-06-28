article = input()
content = input()

comments = []

comment = input()
while comment != "end of comments":
  comments.append(comment)
  comment = input()

print(f"<h1>\n    {article}\n</h1>")
print(f"<article>\n    {content}\n</article>")

for comment in comments:
  print(f"<div>\n    {comment}\n</div>")
  
