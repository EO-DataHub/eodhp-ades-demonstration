import requests
import jwt
import secrets

workspace = ''
ades_job_id = ''
workspace_token = ''
path_to_file = f'processing-results/cat_{ades_job_id}.json'
ades_output_url = f"https://{workspace}.workspaces.test.eodhp.eco-ke-staging.com/files/eodhp-test-workspaces1/{path_to_file}"
user_block_store_url = f'https://{workspace}.workspaces.test.eodhp.eco-ke-staging.com/files/workspaces/{path_to_file}'


def get_outputs_token(url: str, token: str):
    """Test sending a request with token in Authorization header."""
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.headers)
    print("--------------------")
    print(response.text)

def get_outputs_range(url: str, token: str):
    """Test sending a request with token in Authorization header and Range header."""
    # Send request with token in Authorization header and Range header
    headers = {
        'Authorization': f'Bearer {token}',
        'Range': 'bytes=4-8'  # Request specific bytes of the file
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.headers)
    print("--------------------")
    print(response.content)

def get_outputs_cookie(url: str, token: str):
    """Test sending a request with token in a cookie."""
    cookies = {'session': token}
    response = requests.get(url, cookies=cookies)
    print(response.status_code)
    print(response.text)

def generate_token():
    """Generate a JWT token with a secret key."""
    # Generate a secret key
    secret_key = secrets.token_hex(16)
    # Define a payload
    payload = {'key': 'value'}
    # Encode the payload into a token
    new_token = jwt.encode(payload, secret_key, algorithm='HS256')
    token_str = new_token.decode('utf-8')
    print(f'Secret Key: {secret_key}')
    print(f'Token: {token_str}')

if __name__ == '__main__':
    get_outputs_token(ades_output_url, workspace_token)
