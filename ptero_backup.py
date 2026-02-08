import argparse
import requests
import json
import time

def list_servers(api_url, api_key):
    """Lists all servers accessible with the API key."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url = f"{api_url}/api/client"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        servers = response.json().get('data', [])
        return servers
    except requests.exceptions.RequestException as e:
        print(f"Error listing servers: {e}")
        return []

def create_backup(api_url, api_key, server_uuid, backup_name=None):
    """Creates a backup for a specific server."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url = f"{api_url}/api/client/servers/{server_uuid}/backups"
    
    data = {}
    if backup_name:
        data['name'] = backup_name

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        backup_data = response.json().get('attributes', {})
        print(f"✅ Backup started for server {server_uuid}. Backup UUID: {backup_data.get('uuid')}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Error creating backup for {server_uuid}: {e}")
        try:
            print(f"Response: {response.text}")
        except:
            pass
        return False

def main():
    parser = argparse.ArgumentParser(description="Pterodactyl Backup CLI Tool")
    parser.add_argument("--url", required=True, help="Pterodactyl Panel URL (e.g., https://panel.example.com)")
    parser.add_argument("--key", required=True, help="Client API Key")
    parser.add_argument("--server", help="Server UUID to backup (optional, if omitted, backups all servers)")
    parser.add_argument("--list", action="store_true", help="List available servers and exit")
    parser.add_argument("--name", help="Name for the backup (optional)")

    args = parser.parse_args()

    api_url = args.url.rstrip('/')
    api_key = args.key

    if args.list:
        servers = list_servers(api_url, api_key)
        print(f"Found {len(servers)} servers:")
        for s in servers:
            attr = s['attributes']
            print(f"- {attr['name']} ({attr['identifier']})")
        return

    if args.server:
        create_backup(api_url, api_key, args.server, args.name)
    else:
        servers = list_servers(api_url, api_key)
        print(f"Starting backup for {len(servers)} servers...")
        for s in servers:
            uuid = s['attributes']['identifier']
            name = s['attributes']['name']
            print(f"Processing {name} ({uuid})...")
            create_backup(api_url, api_key, uuid, args.name)
            time.sleep(1) # Be nice to the API

if __name__ == "__main__":
    main()
