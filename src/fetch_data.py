import requests
import json
import csv
from pathlib import Path
import time


token_path = Path(__file__).parent.parent / 'secrets' / 'github_token.txt'
with open(token_path, 'r') as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}"
}

# Carrega a query 
query_path = Path(__file__).parent / 'query.graphql'
with open(query_path, 'r') as f:
    query_template = f.read()

def fetch_1000_repos():
    all_repos = []
    cursor = None
    total_repos = 0
    
    while total_repos < 1000:  
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
                print("❌ Erro GraphQL:", data['errors'])
                break
            
            search_data = data['data']['search']
            batch = search_data['nodes']
            all_repos.extend(batch)
            total_repos += len(batch)
            
            print(f"✅ Lote de {len(batch)} repositórios. Total: {total_repos}/1000")
            
            if not search_data['pageInfo']['hasNextPage'] or total_repos >= 1000:
                break
            
            cursor = search_data['pageInfo']['endCursor']
            time.sleep(2) 
            
        except Exception as e:
            print(f"❌ Erro: {e}")
            break
    
    return all_repos[:1000] 

def save_to_csv(repos, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
 
        writer.writerow([
            "name", "owner", "createdAt", "updatedAt", "primaryLanguage",
            "mergedPRs", "releases", "openIssues", "closedIssues", "stars"
        ])
        
        for repo in repos:
            writer.writerow([
                repo["name"],
                repo["owner"]["login"],
                repo["createdAt"],
                repo["updatedAt"],
                repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else "None",
                repo["pullRequests"]["totalCount"],
                repo["releases"]["totalCount"],
                repo["issues"]["totalCount"],
                repo["issuesClosed"]["totalCount"],
                repo["stargazerCount"]
            ])

if __name__ == "__main__":
    repos = fetch_1000_repos()
    
    # Salva em JSON 
    json_path = Path(__file__).parent.parent / 'data' / 'repos_1000.json'
    json_path.parent.mkdir(exist_ok=True)
    with open(json_path, 'w') as f:
        json.dump({"nodes": repos}, f, indent=2)
    
    # Salva em CSV 
    csv_path = Path(__file__).parent.parent / 'data' / 'repos_1000.csv'
    save_to_csv(repos, csv_path)
    
    print(f"🚀 Total coletado: {len(repos)} repositórios")
    print(f"📂 CSV salvo em: {csv_path}")