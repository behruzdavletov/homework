import json

data = {
    "Model":"gentra", "Rang":"Qora", "Yil":2022, "Narh":32000
}
data_json = json.dumps(data, indent=2)
print(data_json)


talaba_json = """{"ism":"Hasan", "familiya":"Husanov", "tyil":2000}"""
talaba_json1 = json.loads(talaba_json)
print(talaba_json1["ism"])
print(talaba_json1["familiya"])

with open("data.json", "w") as f:
    json.dump(data_json, f)

with open("talaba.json", "w") as q:
    json.dump(talaba_json, q)



studetnts_json = """
{"student": [
    {"id": "01", "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"},
    {"id": "02", "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"},
    {"id": "03", "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}
]}
"""
talaba = json.loads(studetnts_json)
for student in talaba["student"]:
    ism = student["name"]
    familiya = student["lastname"]
    kurs = student["year"]
    fakultet = student["faculty"]
    print(f"{ism} {familiya}, {kurs}-kurs,  {fakultet} talabasi")