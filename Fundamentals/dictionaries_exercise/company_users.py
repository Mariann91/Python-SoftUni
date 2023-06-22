companies_info = {}

while True:
  info = input()

  if info == "End":
    break
  
  company_name, employer_id = info.split(" -> ")

  if company_name not in companies_info:
    companies_info[company_name] = []

  if employer_id in companies_info.get(company_name):
    continue

  companies_info[company_name].append(employer_id)

for company_name, employeers_ids in companies_info.items():
  print(company_name)
  [print(f"-- {id}") for id in employeers_ids]
  
