import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PANEL_URL = os.getenv("PTERO_PANEL_URL")
API_KEY = os.getenv("PTERO_API_KEY")

if not PANEL_URL or not API_KEY:
    print("Error: Please set PTERO_PANEL_URL and PTERO_API_KEY in .env file.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_servers():
    """Fetch all servers accessible by the API key."""
    url = f"{PANEL_URL}/api/client"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching servers: {e}")
        return []

def trigger_backup(server_uuid, server_name):
    """Trigger a backup for a specific server."""
    url = f"{PANEL_URL}/api/client/servers/{server_uuid}/backups"
    try:
        response = requests.post(url, headers=HEADERS)
        response.raise_for_status()
        print(f"✅ Backup started for server: {server_name} ({server_uuid})")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to start backup for {server_name}: {e}")

def main():
    print("🚀 Starting Pterodactyl Backup Process...")
    servers = get_servers()
    
    if not servers:
        print("No servers found or API error.")
        return

    print(f"Found {len(servers)} servers.")
    
    for server in servers:
        attrs = server['attributes']
        uuid = attrs['identifier']
        name = attrs['name']
        print(f"Processing {name}...")
        trigger_backup(uuid, name)

    print("\n🎉 Backup process completed!")

if __name__ == "__main__":
    main()
