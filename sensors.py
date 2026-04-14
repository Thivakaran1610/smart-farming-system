import random

def get_moisture():
    return random.randint(10, 90)

def get_temperature():
    return random.randint(20, 45)

def get_nutrients():
    return random.randint(1, 10)

def read_all_sensors():
    return {
        "moisture": get_moisture(),
        "temperature": get_temperature(),
        "nutrients": get_nutrients()
    }
