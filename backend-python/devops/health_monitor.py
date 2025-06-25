# devops/health_monitor.py

import requests
import subprocess
import time

# List of services to monitor
services = {
    "backend-python": "http://localhost:8000/health",
    "spring-api": "http://localhost:8080/actuator/health"
}

def is_healthy(url):
    try:
        response = requests.get(url, timeout=2)
        return response.status_code == 200 and response.json().get("status") == "ok"
    except Exception:
        return False

def restart_container(container_name):
    print(f"🔁 Restarting {container_name}...")
    subprocess.run(["docker", "restart", container_name])

def monitor_services():
    while True:
        for name, url in services.items():
            if not is_healthy(url):
                print(f"❌ {name} is down. Attempting to restart.")
                restart_container(name)
            else:
                print(f"✅ {name} is healthy.")
        time.sleep(10)  # Monitor every 10 seconds

if __name__ == "__main__":
    monitor_services()
