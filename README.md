# Pterodactyl Backup CLI

A lightweight Python script to automate server backups via the Pterodactyl API.

## Features
- **Automated**: Automatically fetches all servers you have access to.
- **Error Handling**: Skips offline or inaccessible servers gracefully.
- **Configurable**: Uses environment variables for API credentials.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mcuabhi17-lab/ptero-backup-cli.git
cd ptero-backup-cli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Set your environment variables:
```bash
export PTERO_API_URL="https://your-pterodactyl-panel.com"
export PTERO_API_KEY="ptlc_your_client_api_key_here"
```

2. Run the script:
```bash
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
