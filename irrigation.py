from config import MOISTURE_THRESHOLD

def control_irrigation(data):
    if data["moisture"] < MOISTURE_THRESHOLD:
        return "Irrigation ON"
    else:
        return "Irrigation OFF"
