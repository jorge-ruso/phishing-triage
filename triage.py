import sys
import re
from email import policy
from email.parser import BytesParser

def load_email(path):
    with open(path, "rb") as f:
        return BytesParser(policy=policy.default).parse(f)

def parse_headers(msg):
    return {
        "from": msg.get("From"),
        "reply_to": msg.get("Reply-To"),
        "return_path": msg.get("Return-Path"),
        "subject": msg.get("Subject"),
        "date": msg.get("Date"),
        "received": msg.get_all("Received", []),
    }

def check_auth(msg):
    auth = msg.get("Authentication-Results", "")
    results = {}
    for check in ["spf", "dkim", "dmarc"]:
        match = re.search(rf"{check}=(\w+)", auth)
        results[check] = match.group(1) if match else "none"
    return results

if __name__ == "__main__":
    msg = load_email(sys.argv[1])
    h = parse_headers(msg)
    for k, v in h.items():
        if k != "received":
            print(f"{k}: {v}")
    print(f"\nSaltos de servidor: {len(h['received'])}")
    print("\n--- Autenticación ---")
    auth = check_auth(msg)
    for k, v in auth.items():
        print(f"{k}: {v}")