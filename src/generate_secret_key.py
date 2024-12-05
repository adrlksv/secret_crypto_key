#!/usr/bin/env python3
import secrets
import base64
import argparse
import sys

def generate_secret_key(length_bytes: int = 32) -> str:
    """Generates a cryptographically secure random secret key.

    Args:
        length_bytes: The desired length of the key in bytes (default is 32 bytes).

    Returns:
        A URL-safe Base64 encoded string representation of the secret key.

    Raises:
        ValueError: If length_bytes is not positive.
    """
    if length_bytes <= 0:
        raise ValueError("length_bytes must be a positive integer")

    random_bytes = secrets.token_bytes(length_bytes)
    return base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure secret key.")
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=32,
        help="Length of the key in bytes (default: 32)."
    )
    args = parser.parse_args()

    try:
        secret_key = generate_secret_key(args.length)
        print(f"Generated secret key: {secret_key}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
