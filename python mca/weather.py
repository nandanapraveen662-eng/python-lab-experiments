import json

data = '''
{
    "cities": [
        {
            "name": "Kollam",
            "temperature": 30,
            "humidity": 75
        },
        {
            "name": "Kochi",
            "temperature": 32,
            "humidity": 70
        },
        {
            "name": "Trivandrum",
            "temperature": 29,
            "humidity": 80
        }
    ]
}
'''

weather = json.loads(data)

print("WEATHER REPORT")

for city in weather["cities"]:
    print("\nCity:", city["name"])
    print("Temperature:", city["temperature"], "°C")
    print("Humidity:", city["humidity"], "%")