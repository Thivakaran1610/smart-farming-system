from sensors import read_all_sensors
from irrigation import control_irrigation
from analytics import analyze_data
from cloud import send_to_cloud
import time

def main():
    print("Smart Farming System Started...\n")

    for _ in range(10):
        data = read_all_sensors()

        print("Sensor Data:", data)

        irrigation_status = control_irrigation(data)
        print("Irrigation:", irrigation_status)

        analysis = analyze_data(data)
        print("Analysis:", analysis)

        send_to_cloud(data)

        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    main()
