import socket
import platform
import requests

def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data["status"] == "success":
        return data["country"], data["regionName"], data["city"]
    else:
        return "Unknown", "Unknown", "Unknown"

def get_info():
    # Get IP address
    ip = socket.gethostbyname(socket.gethostname())

    # Get location
    country, region, city = get_location(ip)

    # Get computer information
    computer_info = platform.uname()

    return {
        "IP": ip,
        "Location": {
            "Country": country,
            "Region": region,
            "City": city
        },
        "Computer Info": {
            "System": computer_info.system,
            "Node": computer_info.node,
            "Release": computer_info.release,
            "Version": computer_info.version,
            "Machine": computer_info.machine,
            "Processor": computer_info.processor
        }
    }

# Export the function as getInfo
getInfo = get_info
