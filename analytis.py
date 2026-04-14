def analyze_data(data):
    alerts = []

    if data["temperature"] > 35:
        alerts.append("High Temperature")

    if data["nutrients"] < 4:
        alerts.append("Low Nutrients")

    if not alerts:
        return "All conditions normal"

    return ", ".join(alerts)
