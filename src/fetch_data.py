import requests
import json
from pathlib import Path
import time

# Configurações
token_path = Path(__file__).parent.parent / 'secrets' / 'github_token.txt'
with open(token_path, 'r') as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}"
}

# Carrega a query do arquivo
query_path = Path(__file__).parent / 'query.graphql'
with open(query_path, 'r') as f:
    query_template = f.read()

def fetch_all_repos():
    all_repos = []
    cursor = None
    has_next_page = True
    attempt = 0
    max_attempts = 3
    
    while has_next_page and attempt < max_attempts:
        try:
            print(f"⏳ Buscando lote (cursor: {cursor})...")
            
            # Prepara as variáveis para a query
            variables = {"cursor": cursor} if cursor else {}
            
            response = requests.post(
                'https://api.github.com/graphql',
                headers=headers,
                json={
                    'query': query_template,
                    'variables': variables
                },
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

            if 'errors' in data:
                print("❌ Erro GraphQL:")
                for error in data['errors']:
                    print(f"- {error['message']}")
                attempt += 1
                time.sleep(5)
                continue

            search_data = data['data']['search']
            all_repos.extend(search_data['nodes'])
            has_next_page = search_data['pageInfo']['hasNextPage']
            cursor = search_data['pageInfo']['endCursor']
            attempt = 0
            
            time.sleep(2)  # Intervalo entre requisições

        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na requisição (tentativa {attempt + 1}/{max_attempts}):")
            print(f"- Tipo: {type(e).__name__}")
            print(f"- Detalhes: {str(e)}")
            attempt += 1
            time.sleep(5)

    return all_repos

if __name__ == "__main__":
    print("Iniciando coleta de dados...")
    repos = fetch_all_repos()
    output_path = Path(__file__).parent.parent / 'data' / 'repos_100.json'
    output_path.parent.mkdir(exist_ok=True, parents=True)

    with open(output_path, 'w') as f:
        json.dump({"nodes": repos}, f, indent=2)

    print(f"✅ Total de repositórios salvos: {len(repos)}")
    print(f"📂 Arquivo salvo em: {output_path}")