import requests
import json
from pathlib import Path
import time

token_path = Path(__file__).parent.parent / 'secrets' / 'github_token.txt'
with open(token_path, 'r') as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}"
}

query_path = Path(__file__).parent / 'query.graphql'
with open(query_path, 'r') as f:
    query_template = f.read()

def fetch_100_repos():
    all_repos = []
    cursor = None
    total_repos = 0
    
    while total_repos < 100:
        try:
            variables = {"cursor": cursor} if cursor else {}
            
            response = requests.post(
                'https://api.github.com/graphql',
                headers=headers,
                json={'query': query_template, 'variables': variables},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            if 'errors' in data:
                print("Erro GraphQL:", data['errors'])
                break
            
            search_data = data['data']['search']
            batch = search_data['nodes']
            all_repos.extend(batch)
            total_repos += len(batch)
            
            if total_repos >= 100 or not search_data['pageInfo']['hasNextPage']:
                break
                
            cursor = search_data['pageInfo']['endCursor']
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            break

    return all_repos[:100]

if __name__ == "__main__":
    repos = fetch_100_repos()
    output_path = Path(__file__).parent.parent / 'data' / 'repos_100.json'
    output_path.parent.mkdir(exist_ok=True, parents=True)

    with open(output_path, 'w') as f:
        json.dump({"nodes": repos}, f, indent=2)

    print(f"Total coletado: {len(repos)} repositórios")
    print(f"Salvo em: {output_path}")