from setuptools import setup

setup(
    name="generate-secret-key",
    version="1.0.0",
    py_modules=["generate_secret_key"],
    package_dir={"": "."},
    entry_points={
        "console_scripts": [
            "generate-secret-key=generate_secret_key:main",
        ],
    },
    description="A script to generate cryptographically secure secret keys.",
    author="adrlksv",
    author_email="Qwerty123Andrey@bk.ru",
    url="https://github.com/adrlksv/secret_crypto_key",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
