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
  message_sender, message_receiver, message_content = message.split()
  
  email = Email(message_sender, message_receiver, message_content)
  emails.append(email)

  message = input()

indexes = [int(index) for index in input().split(", ")]

for index in range(len(emails)):
  current_email = emails[index]
  if index in indexes:
    current_email.is_sent = True
  print(current_email.get_info())
  
