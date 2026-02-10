# Pterodactyl Backup CLI 🚀

A simple but powerful CLI tool to automate server backups for your Pterodactyl panel. Perfect for daily cron jobs or one-off backups.

## Features

- **Automated Backups:** Trigger backups for all accessible servers with a single command.
- **Easy Setup:** Uses a simple `.env` file for configuration.
- **Error Handling:** Graceful error messages if something goes wrong.

## Requirements

- Python 3.8+
- Pterodactyl Panel API Key (Client API)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mcuabhi17-lab/ptero-backup-cli.git
   cd ptero-backup-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   ```env
   PTERO_PANEL_URL=https://your-panel.com
   PTERO_API_KEY=ptlc_YOUR_API_KEY
   ```

## Usage

Run the script:

```bash
python backup.py
```

## Contributing

Feel free to open issues or pull requests if you want to add features like specific server targeting or custom backup names!

## License

MIT License
