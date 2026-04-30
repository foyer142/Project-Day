
import requests

def fetch_url(url: str) -> dict:
    r = requests.get(url,timeout=10)
    info = {
    "status_code": r.status_code,
    "content_type": r.headers.get('content-type'),
    "preview": r.text[:100],
    }
    return info

def main():
    print(fetch_url('https://api.github.com'))

if __name__ == '__main__':
    main()