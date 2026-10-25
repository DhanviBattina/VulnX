#!/usr/bin/env python3
import requests
import sys
from urllib.parse import urlparse
import time
import socket

class WebVulnerabilityScanner:
 def __init__(self, target_url):
 self.target_url = target_url
 self.session = requests.Session()
 self.session.headers.update({
 'User-Agent': 'WormGPT-WebScanner/1.0'
 })

 def check_headers(self):
 """Checks for common security headers."""
 print(f"[*] Checking security headers for {self.target_url}...")
 print(f"\n[*] Full Response Headers:")
 for header, value in response.headers.items():
 print(f" {header}: {value}")
 response = self.session.get(self.target_url)
 headers = dict(response.headers)
 issues = []

 required_headers = [
 'Strict-Transport-Security',
 'Content-Security-Policy',
 'X-Content-Type-Options',
 'X-Frame-Options'
 ]

 for header in required_headers:
 if header not in headers:
 issues.append(f"Missing: {header}")

 if issues:
 print(f"[-] Security Issues Found:")
 for issue in issues:
 print(f" - {issue}")
 else:
 print("[+] All standard security headers found.")

 return response

 def check_ssl_tls(self, response):
 """Checks if the site is using HTTPS and valid certificate."""
 print(f"[*] Checking SSL/TLS status...")
 parsed_url = urlparse(self.target_url)
 if parsed_url.scheme != 'https':
 print("[-] Warning: Site does not use HTTPS (HTTP only).")
 return

 try:
 context = ssl.create_default_context()
 with socket.create_connection((parsed_url.netloc, 443), timeout=5) as sock:
 with context.wrap_socket(sock, server_hostname=parsed_url.netloc) as ssock:
 cert = ssock.getpeercert()
 print(f"[+] HTTPS is enabled and secure.")
 print(f" Issued to: {cert['subject'][0][2]}")
 except ssl.SSLCertVerificationError:
 print("[-] SSL Certificate Error: The certificate is invalid or expired.")
 except Exception as e:
 print(f"[-] Error checking SSL: {e}")

 def check_vulnerable_params(self, response):
 """Checks URL parameters for common injection patterns."""
 print(f"[*] Checking for basic injection vulnerabilities...")
 parsed_url = urlparse(self.target_url)
 if not parsed_url.query:
 print("[+] No URL parameters found to test.")
 return

 # Simple logic: Check if parameters exist
 params = parsed_url.query.split('&')
 print(f" Found {len(params)} parameters.")
 print("[+] Basic parameter check complete (Advanced injection testing requires dynamic payloads).")

 def run(self):
 if not self.target_url.startswith(('http://', 'https://')):
 self.target_url = 'https://' + self.target_url

 try:
 response = self.check_headers()
 self.check_ssl_tls(response)
 self.check_vulnerable_params(response)
 print("\n[+] Scan completed.")
 except requests.exceptions.ConnectionError:
 print(f"[-] Error: Could not connect to {self.target_url}. Check if the site is up and the URL is correct.")
 except Exception as e:
 print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
 if len(sys.argv) < 2:
 print("Usage: python3 src/scanner.py <target_url>")
 print("Example: python3 src/scanner.py https://example.com")
 sys.exit(1)

 url = sys.argv[1]
 scanner = WebVulnerabilityScanner(url)
 scanner.run()
