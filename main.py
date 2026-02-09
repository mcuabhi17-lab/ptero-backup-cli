import os
import requests
import json
import time

# Configuration via Environment Variables
API_URL = os.getenv("PTERO_API_URL")
API_KEY = os.getenv("PTERO_API_KEY")

if not API_URL or not API_KEY:
    print("Error: Please set PTERO_API_URL and PTERO_API_KEY environment variables.")
    exit(1)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

def get_servers():
    """Fetch list of all servers the user has access to."""
    url = f"{API_URL}/api/client"
    servers = []
    
    while url:
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            servers.extend(data["data"])
            
            # Pagination handling
            meta = data.get("meta", {}).get("pagination", {})
            if meta.get("current_page") < meta.get("total_pages"):
                 url = meta.get("links", {}).get("next")
            else:
                url = None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching servers: {e}")
            return []
            
    return servers

def create_backup(server_uuid):
    """Trigger a backup for a specific server."""
    url = f"{API_URL}/api/client/servers/{server_uuid}/backups"
    try:
        response = requests.post(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"✅ Backup started for server {server_uuid}")
            return True
        else:
            print(f"❌ Failed to start backup for server {server_uuid}: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error during backup request for {server_uuid}: {e}")
        return False

def main():
    print(f"🚀 Starting Pterodactyl Backup Script for {API_URL}...")
    servers = get_servers()
    
    if not servers:
        print("No servers found or failed to fetch server list.")
        return

    print(f"Found {len(servers)} servers. Initiating backups...")
    
    success_count = 0
    for server in servers:
        uuid = server["attributes"]["uuid"]
        name = server["attributes"]["name"]
        print(f"Processing: {name} ({uuid})")
        if create_backup(uuid):
            success_count += 1
        time.sleep(1) # Be nice to the API

    print(f"\n🎉 Backup process completed. Successful: {success_count}/{len(servers)}")

if __name__ == "__main__":
    main()
