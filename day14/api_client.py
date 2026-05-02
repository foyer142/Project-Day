import requests

def get_github_status() -> dict:
    r = requests.get('https://api.github.com',timeout=10)
    response_dict = {
        'status_code' : r.status_code,
        'content_type' : r.headers.get('content-type')
    }
    return response_dict
