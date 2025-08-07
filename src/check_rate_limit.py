import requests
from pathlib import Path

# Caminho do token
token_path = Path(__file__).parent.parent / 'secrets' / 'github_token.txt'
with open(token_path, 'r') as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}"
}

# Query para verificar o rate limit
query = """
query {
  rateLimit {
    limit
    remaining
    resetAt
    used
  }
}
"""

response = requests.post(
    'https://api.github.com/graphql',
    headers=headers,
    json={'query': query}
)

if response.status_code == 200:
    data = response.json()
    print("✅ Rate limit info:")
    print(f"Limite total: {data['data']['rateLimit']['limit']}")
    print(f"Requisições restantes: {data['data']['rateLimit']['remaining']}")
    print(f"Reset em: {data['data']['rateLimit']['resetAt']}")
else:
    print("❌ Erro ao verificar rate limit:", response.status_code)
    print(response.text)