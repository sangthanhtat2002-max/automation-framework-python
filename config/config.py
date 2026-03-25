import os

URLS = {
    "dev": "https://dev.example.com",
    "qa": "https://www.saucedemo.com",
    "prod": "https://example.com"
}

ENV = os.getenv("ENV", "qa").lower()

if ENV not in URLS:
    raise ValueError(f"Environment '{ENV}' is not supported. Supported environments are: {', '.join(URLS.keys())}")

BASE_URL = URLS[ENV]