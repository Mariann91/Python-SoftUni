countries = input().split(", ")
capitals = input().split(", ")

final_dic = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in final_dic.items():
    print(f"{country} -> {capital}")
  
