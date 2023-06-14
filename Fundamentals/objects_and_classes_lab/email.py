class Email:
  def __init__(self, sender, receiver, content):
    self.sender = sender
    self.receiver = receiver
    self.content = content
    self.is_sent = False

  def send(self):
    self.is_sent = True

  def get_info(self):
    return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
    
message = input()

emails = []
while message != "Stop":
  message = message.split()
  message_sender = message[0]
  message_receiver = message[1]
  message_content = message[2]

  current_email = Email(message_sender, message_receiver, message_content)
  emails.append(current_email)

  message = input()

indexes = [int(num) for num in input().split(", ")]

for i in range(len(emails)):
  if i in indexes:
    emails[i].is_sent = True

for email in emails:
  print(email.get_info())
  
