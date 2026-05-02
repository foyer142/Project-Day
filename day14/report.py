import api_client

def build_report(users: list[dict], github_info: dict) -> str:    
    return f"User total: {len(users)}\nGitHub status: {github_info['status_code']}\nGitHub content type: {github_info['content_type']}"

