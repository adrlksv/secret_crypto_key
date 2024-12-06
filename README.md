# Generate Secret Key

[<img align="left" alt="Python" width="40px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"/>][github]
![JWT](https://img.shields.io/badge/dynamic/toml?url=%3Csvg%20role%3D%22img%22%20viewBox%3D%220%200%2024%2024%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Ctitle%3EJSON%20Web%20Tokens%3C%2Ftitle%3E%3Cpath%20d%3D%22M10.2%200v6.456L12%208.928l1.8-2.472V0zm3.6%206.456v3.072l2.904-.96L20.52%203.36l-2.928-2.136zm2.904%202.112l-1.8%202.496%202.928.936%206.144-1.992-1.128-3.432zM17.832%2012l-2.928.936%201.8%202.496%206.144%201.992%201.128-3.432zm-1.128%203.432l-2.904-.96v3.072l3.792%205.232%202.928-2.136zM13.8%2017.544L12%2015.072l-1.8%202.472V24h3.6zm-3.6%200v-3.072l-2.904.96L3.48%2020.64l2.928%202.136zm-2.904-2.112l1.8-2.496L6.168%2012%20.024%2013.992l1.128%203.432zM6.168%2012l2.928-.936-1.8-2.496-6.144-1.992-1.128%203.432zm1.128-3.432l2.904.96V6.456L6.408%201.224%203.48%203.36Z%22%2F%3E%3C%2Fsvg%3E)



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
```bash
pipx ensurepath
```
Next, restart the terminal

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


