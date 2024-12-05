# Generate Secret Key

![Python](https://img.shields.io/badge/dynamic/toml?url=%3Csvg%20role%3D%22img%22%20viewBox%3D%220%200%2024%2024%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Ctitle%3EPython%3C%2Ftitle%3E%3Cpath%20d%3D%22M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02%201.27.05zm-6.3%201.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09%203.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14%201.04.05%201.23-.06%201.23-.16%201.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01%202.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47%2014.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z%22%2F%3E%3C%2Fsvg%3E)
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


