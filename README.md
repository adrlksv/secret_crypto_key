# Generate Secret Key

![Python](https://img.shields.io/badge/Python_3.10-blue?logo=python&logoColor=yellow)

This script generates a cryptographically secure random secret key. It is particularly useful for creating API keys, session tokens, or other cryptographic secrets that need to be secure and URL-safe.

## Features

- Generates a random secret key of a specified length.
- Encodes the key in a URL-safe Base64 format.
- Removes unnecessary padding (`=`) from the encoded string for cleaner output.

---

## Installation

You can install and use this script globally as a terminal command without cloning the repository.

### 1. **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.6 or higher
- `pipx` (recommended for global installation of Python CLI tools)

If `pipx` is not installed, you can install it via `pip`:
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### 2. **Install the script**
Install the script directly from its GitHub repository using `pipx`:
```bash
pipx install git+https://github.com/adrlksv/secret_crypto_key.git
```
If you prefer using `pip`, you can install it globally (though `pipx` is recommended fo CLI tools):
```bash
pip install git+https://github.com/adrlksv/secret_crypto_key.git
```

## Usage
After installation, you can use the `generate-secret-key` command directly from the terminal.

## Basic Command
To generate a secret key with the default lenght (32 bytes), run:
```bash
generate-secret-key
```

## Specifying Key Length
You can specify the desired length of the key (in bytes) using the `--length` or `-l` option:
```bash
generate-secret-key --length 64
```
or
```bash
generate-secret-key -l 64
```

## Example Output
```plaintext
Generated secret key: h9KdmjQfOAmnN8rlWmcRoIBoLR75d5TkyXUZ0NtycFE
```

## Command-Line Options
- `-l`, `--length`:
    (Optional) Thr length of the secret key in bytes. Default is `32`.
    Example: `--length 64` generates a 64-byte key.

## How It Works
1. The script uses Python's `secrets` module to generate cryptographically secure random bytes.
2. These bytes are encoded using Base64 in URL-safe format with `base64.urlsafe_b64encode`.
3. The encoded string is stripped of padding characters (`=`) for a cleaner result.

## Troubleshooting
If you encounter any issues:
- Ensure Python 3.6+ is installed.
- Verify `pipx` is installed and properly configured.
- Check your internet connection when installing from Github.


