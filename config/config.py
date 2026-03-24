import os

URLS = {
    "dev": "https://dev.example.com",
    "qa": "https://aim.qa.spdigital.sg/",
    "prod": "https://example.com"
}

ENV = os.getenv("ENV", "qa").lower()

if ENV not in URLS:
    raise ValueError(f"Environment '{ENV}' is not supported. Supported environments are: {', '.join(URLS.keys())}")

BASE_URL = URLS[ENV]