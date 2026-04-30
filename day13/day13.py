
import requests



def get_github_status() -> int:
    response = requests.get("https://api.github.com", timeout=10)
    return response.status_code


def main() -> None:
    status_code = get_github_status()
    print(f"GitHub API status code: {status_code}")


if __name__ == "__main__":
    main()
