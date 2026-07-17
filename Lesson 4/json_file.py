#dumps() - python -> json-sroka (rabotaet so stokami)
#loads() - json -> python (rabotaet so strokami)
#dump() - save pyton object to [file].json (work with file)
#load() - save [file].json to python (work with file)
import json

user = {"username":"Egor",
        "age":30,
        "is_admin":True}

json_string = json.dumps(user)
print (json_string)
print(type(json_string))

user = json.loads(json_string)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
        "base_url":"https://api.example.com",
        "timeout": 10,
        "retries": 3
}

with open("config.json", "w", encoding = "utf-8") as file:
        json.dump(test_config, file, indent=2, ensure_ascii=False)

with open("config.json", "r", encoding = "utf-8") as file:
        loaded_config = json.load(file)

print()
print(loaded_config)
print(loaded_config["base_url"])