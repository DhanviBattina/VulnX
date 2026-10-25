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

```
2. Thne run these commands in the terminal 
   ```bash
   mkdir my-web-scanner
   cd VulnX
   mkdir src

## usage
``` bash
python3 src/scanner.py <target_url>
```
- Run this command in the terminal and paste the site that you want to check


## License
- This project is open source and free to use for educational purposes.
