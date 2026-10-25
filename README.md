## 👽 VulnX
# Web Vulnerability Scanner

A Python-based security tool designed to scan websites for basic security vulnerabilities, missing headers, and SSL/TLS configuration issues.

## Features

- **Header Analysis:** Checks for missing security headers like HSTS, CSP, and X-Frame-Options.
- **SSL/TLS Check:** Validates if the website is using HTTPS and checks for certificate validity.
- **Parameter Detection:** Identifies URL parameters that could be targeted for injection attacks.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Install the required Python library:
 ```bash
 pip3 install requests
