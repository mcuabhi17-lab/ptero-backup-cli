# Pterodactyl Backup CLI Tool

A simple Python CLI tool to automate Pterodactyl server backups using the Client API.

## Features

- **Backup All Servers**: Backups all servers accessible with your API key in one go.
- **Backup Specific Server**: Target a specific server by its UUID.
- **List Servers**: Quickly see available servers.
- **Naming**: Optionally name your backups.

## Usage

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Script:**

    **List Servers:**
    ```bash
    python ptero_backup.py --url https://panel.yourhost.com --key YOUR_API_KEY --list
    ```

    **Backup All Servers:**
    ```bash
    python ptero_backup.py --url https://panel.yourhost.com --key YOUR_API_KEY
    ```

    **Backup Specific Server:**
    ```bash
    python ptero_backup.py --url https://panel.yourhost.com --key YOUR_API_KEY --server SERVER_UUID --name "Weekly Backup"
    ```

## Requirements

- Python 3.x
- `requests` library

## License

MIT License.
