import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pathlib import Path

# Configuração para gráficos
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

def load_data():
    """Carrega e prepara os dados"""
    data_path = Path(__file__).parent.parent / 'data' / 'repos_1000.csv'
    df = pd.read_csv(data_path)
    
    # Prepara dados calculados
    hoje = datetime.now()
    df['createdAt'] = pd.to_datetime(df['createdAt']).dt.tz_localize(None)
    df['updatedAt'] = pd.to_datetime(df['updatedAt']).dt.tz_localize(None)
    df['idade_anos'] = (hoje - df['createdAt']).dt.days / 365.25
    df['dias_desde_atualizacao'] = (hoje - df['updatedAt']).dt.days
    df['total_issues'] = df['openIssues'] + df['closedIssues']
    df['percentual_issues_fechadas'] = (df['closedIssues'] / df['total_issues'] * 100).fillna(0)
    
    return df

def gerar_graficos(df):
    """Gera todos os gráficos das RQs"""
    output_path = Path(__file__).parent.parent / 'graficos'
    output_path.mkdir(exist_ok=True)
    
    # RQ01: Idade dos repositórios
    plt.figure(figsize=(10, 6))
    plt.hist(df['idade_anos'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.axvline(df['idade_anos'].median(), color='red', linestyle='--', linewidth=2, 
                label=f'Mediana: {df["idade_anos"].median():.1f} anos')
    plt.xlabel('Idade do Repositório (anos)')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ01: Distribuição da Idade dos Repositórios Populares')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq01_idade_repositorios.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ02: Pull Requests
    plt.figure(figsize=(10, 6))
    plt.hist(df['mergedPRs'], bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.axvline(df['mergedPRs'].median(), color='red', linestyle='--', linewidth=2,
                label=f'Mediana: {df["mergedPRs"].median():.0f} PRs')
    plt.xlabel('Número de Pull Requests Aceitas')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ02: Distribuição de Pull Requests Aceitas')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq02_pull_requests.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ03: Releases
    plt.figure(figsize=(10, 6))
    plt.hist(df['releases'], bins=50, alpha=0.7, color='orange', edgecolor='black')
    plt.axvline(df['releases'].median(), color='red', linestyle='--', linewidth=2,
                label=f'Mediana: {df["releases"].median():.0f} releases')
    plt.xlabel('Número de Releases')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ03: Distribuição do Número de Releases')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq03_releases.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ04: Frequência de atualização
    plt.figure(figsize=(10, 6))
    plt.hist(df['dias_desde_atualizacao'], bins=50, alpha=0.7, color='purple', edgecolor='black')
    plt.axvline(df['dias_desde_atualizacao'].median(), color='red', linestyle='--', linewidth=2,
                label=f'Mediana: {df["dias_desde_atualizacao"].median():.0f} dias')
    plt.xlabel('Dias Desde a Última Atualização')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ04: Distribuição do Tempo Desde Última Atualização')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq04_atualizacao.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ05: Linguagens (Pizza)
    linguagens = df['primaryLanguage'].value_counts()
    plt.figure(figsize=(12, 8))
    top_linguagens = linguagens.head(15)
    colors = plt.cm.Set3(np.linspace(0, 1, len(top_linguagens)))
    plt.pie(top_linguagens.values, labels=top_linguagens.index, autopct='%1.1f%%', colors=colors)
    plt.title('RQ05: Distribuição das Linguagens de Programação (Top 15)')
    plt.savefig(output_path / 'rq05_linguagens.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ05: Linguagens (Barras)
    plt.figure(figsize=(12, 6))
    top_10 = linguagens.head(10)
    plt.bar(range(len(top_10)), top_10.values, color='steelblue')
    plt.xlabel('Linguagens de Programação')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ05: Top 10 Linguagens mais Populares')
    plt.xticks(range(len(top_10)), top_10.index, rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq05_linguagens_bar.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ06: Issues fechadas
    df_com_issues = df[df['total_issues'] > 0]
    plt.figure(figsize=(10, 6))
    plt.hist(df_com_issues['percentual_issues_fechadas'], bins=30, alpha=0.7, color='coral', edgecolor='black')
    plt.axvline(df_com_issues['percentual_issues_fechadas'].median(), color='red', linestyle='--', linewidth=2,
                label=f'Mediana: {df_com_issues["percentual_issues_fechadas"].median():.1f}%')
    plt.xlabel('Percentual de Issues Fechadas (%)')
    plt.ylabel('Número de Repositórios')
    plt.title('RQ06: Distribuição do Percentual de Issues Fechadas')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_path / 'rq06_issues_fechadas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ07: Comparação por linguagem
    top_linguagens_list = df['primaryLanguage'].value_counts().head(10).index.tolist()
    df_populares = df[df['primaryLanguage'].isin(top_linguagens_list)]
    df_outras = df[~df['primaryLanguage'].isin(top_linguagens_list)]
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('RQ07: Comparação entre Linguagens Populares vs Outras', fontsize=16, fontweight='bold')
    
    categorias = ['Linguagens\nPopulares', 'Outras\nLinguagens']
    
    # Pull Requests
    prs_dados = [df_populares['mergedPRs'].median(), df_outras['mergedPRs'].median()]
    bars1 = axes[0,0].bar(categorias, prs_dados, color=['#2E86AB', '#A23B72'], alpha=0.8)
    axes[0,0].set_title('Pull Requests Aceitas (Mediana)')
    axes[0,0].set_ylabel('Número de PRs')
    axes[0,0].grid(True, alpha=0.3)
    for bar, valor in zip(bars1, prs_dados):
        axes[0,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                      f'{valor:.0f}', ha='center', va='bottom', fontweight='bold')
    
    # Releases
    rel_dados = [df_populares['releases'].median(), df_outras['releases'].median()]
    bars2 = axes[0,1].bar(categorias, rel_dados, color=['#F18F01', '#C73E1D'], alpha=0.8)
    axes[0,1].set_title('Número de Releases (Mediana)')
    axes[0,1].set_ylabel('Número de Releases')
    axes[0,1].grid(True, alpha=0.3)
    for bar, valor in zip(bars2, rel_dados):
        axes[0,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                      f'{valor:.0f}', ha='center', va='bottom', fontweight='bold')
    
    # Atualização
    upd_dados = [df_populares['dias_desde_atualizacao'].median(), df_outras['dias_desde_atualizacao'].median()]
    bars3 = axes[1,0].bar(categorias, upd_dados, color=['#3C6E71', '#70A288'], alpha=0.8)
    axes[1,0].set_title('Dias desde Última Atualização (Mediana)')
    axes[1,0].set_ylabel('Dias')
    axes[1,0].grid(True, alpha=0.3)
    for bar, valor in zip(bars3, upd_dados):
        axes[1,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                      f'{valor:.0f}', ha='center', va='bottom', fontweight='bold')
    
    # Diferenças percentuais
    metricas_nomes = ['PRs', 'Releases', 'Atualização']
    diferencas = [
        ((prs_dados[0] - prs_dados[1]) / prs_dados[1] * 100) if prs_dados[1] > 0 else 0,
        100 if rel_dados[1] == 0 else ((rel_dados[0] - rel_dados[1]) / rel_dados[1] * 100),
        ((upd_dados[0] - upd_dados[1]) / upd_dados[1] * 100) if upd_dados[1] > 0 else 0
    ]
    
    colors = ['green' if d > 0 else 'red' if d < 0 else 'gray' for d in diferencas]
    bars4 = axes[1,1].bar(metricas_nomes, diferencas, color=colors, alpha=0.8)
    axes[1,1].set_title('Vantagem das Linguagens Populares (%)')
    axes[1,1].set_ylabel('Diferença Percentual (%)')
    axes[1,1].axhline(y=0, color='black', linestyle='-', alpha=0.5)
    axes[1,1].grid(True, alpha=0.3)
    for bar, valor in zip(bars4, diferencas):
        axes[1,1].text(bar.get_x() + bar.get_width()/2, 
                      bar.get_height() + (5 if valor >= 0 else -15),
                      f'{valor:+.1f}%', ha='center', va='bottom' if valor >= 0 else 'top', 
                      fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path / 'rq07_comparacao_linguagens.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # RQ07: Métricas por linguagem individual
    stats_por_linguagem = []
    for linguagem in top_linguagens_list:
        df_lang = df[df['primaryLanguage'] == linguagem]
        stats = {
            'Linguagem': linguagem,
            'PRs': df_lang['mergedPRs'].median(),
            'Releases': df_lang['releases'].median(),
            'Dias': df_lang['dias_desde_atualizacao'].median()
        }
        stats_por_linguagem.append(stats)
    
    df_stats = pd.DataFrame(stats_por_linguagem)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # PRs por linguagem
    df_sorted_prs = df_stats.sort_values('PRs', ascending=True)
    axes[0].barh(df_sorted_prs['Linguagem'], df_sorted_prs['PRs'], color='skyblue')
    axes[0].set_xlabel('Pull Requests Aceitas (Mediana)')
    axes[0].set_title('PRs por Linguagem')
    axes[0].grid(True, alpha=0.3)
    
    # Releases por linguagem
    df_sorted_rel = df_stats.sort_values('Releases', ascending=True)
    axes[1].barh(df_sorted_rel['Linguagem'], df_sorted_rel['Releases'], color='lightgreen')
    axes[1].set_xlabel('Número de Releases (Mediana)')
    axes[1].set_title('Releases por Linguagem')
    axes[1].grid(True, alpha=0.3)
    
    # Atualização por linguagem
    df_sorted_upd = df_stats.sort_values('Dias', ascending=False)
    axes[2].barh(df_sorted_upd['Linguagem'], df_sorted_upd['Dias'], color='orange')
    axes[2].set_xlabel('Dias desde Última Atualização (Mediana)')
    axes[2].set_title('Atualização por Linguagem')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path / 'rq07_metricas_por_linguagem.png', dpi=300, bbox_inches='tight')
    plt.close()

def mostrar_estatisticas(df):
    """Mostra as estatísticas principais de cada RQ"""
    print("\n" + "="*60)
    print("📊 ESTATÍSTICAS DOS REPOSITÓRIOS POPULARES")
    print("="*60)
    
    # RQ01: Idade
    print("\n🕐 RQ01: Maturidade dos Repositórios")
    print("-" * 40)
    idade_stats = df['idade_anos'].describe()
    print(f"Mediana: {df['idade_anos'].median():.1f} anos")
    print(f"Média: {df['idade_anos'].mean():.1f} anos")
    print(f"Mínimo: {df['idade_anos'].min():.1f} anos")
    print(f"Máximo: {df['idade_anos'].max():.1f} anos")
    
    # RQ02: Pull Requests
    print("\n🔄 RQ02: Contribuição Externa (Pull Requests)")
    print("-" * 40)
    print(f"Mediana: {df['mergedPRs'].median():.0f} PRs")
    print(f"Média: {df['mergedPRs'].mean():.0f} PRs")
    print(f"Mínimo: {df['mergedPRs'].min():.0f} PRs")
    print(f"Máximo: {df['mergedPRs'].max():.0f} PRs")
    
    # RQ03: Releases
    print("\n🚀 RQ03: Frequência de Releases")
    print("-" * 40)
    print(f"Mediana: {df['releases'].median():.0f} releases")
    print(f"Média: {df['releases'].mean():.0f} releases")
    print(f"Mínimo: {df['releases'].min():.0f} releases")
    print(f"Máximo: {df['releases'].max():.0f} releases")
    
    # RQ04: Atualização
    print("\n📅 RQ04: Frequência de Atualização")
    print("-" * 40)
    print(f"Mediana: {df['dias_desde_atualizacao'].median():.0f} dias")
    print(f"Média: {df['dias_desde_atualizacao'].mean():.0f} dias")
    print(f"Mínimo: {df['dias_desde_atualizacao'].min():.0f} dias")
    print(f"Máximo: {df['dias_desde_atualizacao'].max():.0f} dias")
    
    # RQ05: Linguagens (Top 10)
    print("\n💻 RQ05: Linguagens Mais Populares (Top 10)")
    print("-" * 40)
    linguagens = df['primaryLanguage'].value_counts().head(10)
    for i, (lang, count) in enumerate(linguagens.items(), 1):
        print(f"{i:2d}. {lang}: {count} repos ({count/len(df)*100:.1f}%)")
    
    # RQ06: Issues fechadas
    df_com_issues = df[df['total_issues'] > 0]
    print("\n🐛 RQ06: Percentual de Issues Fechadas")
    print("-" * 40)
    print(f"Mediana: {df_com_issues['percentual_issues_fechadas'].median():.1f}%")
    print(f"Média: {df_com_issues['percentual_issues_fechadas'].mean():.1f}%")
    print(f"Mínimo: {df_com_issues['percentual_issues_fechadas'].min():.1f}%")
    print(f"Máximo: {df_com_issues['percentual_issues_fechadas'].max():.1f}%")
    print(f"Repositórios analisados: {len(df_com_issues)} de {len(df)}")
    
    # RQ07: Comparação por linguagem
    print("\n🔄 RQ07: Linguagens Populares vs Outras")
    print("-" * 40)
    top_linguagens = df['primaryLanguage'].value_counts().head(10).index.tolist()
    df_populares = df[df['primaryLanguage'].isin(top_linguagens)]
    df_outras = df[~df['primaryLanguage'].isin(top_linguagens)]
    
    print(f"Linguagens Populares: {len(df_populares)} repositórios")
    print(f"Outras Linguagens: {len(df_outras)} repositórios")
    print()
    print("Pull Requests (Mediana):")
    print(f"  Populares: {df_populares['mergedPRs'].median():.0f} PRs")
    print(f"  Outras: {df_outras['mergedPRs'].median():.0f} PRs")
    print("Releases (Mediana):")
    print(f"  Populares: {df_populares['releases'].median():.0f} releases")
    print(f"  Outras: {df_outras['releases'].median():.0f} releases")
    print("Releases (Média):")
    print(f"  Populares: {df_populares['releases'].mean():.1f} releases")
    print(f"  Outras: {df_outras['releases'].mean():.1f} releases")
    print("Dias desde atualização (Mediana):")
    print(f"  Populares: {df_populares['dias_desde_atualizacao'].median():.0f} dias")
    print(f"  Outras: {df_outras['dias_desde_atualizacao'].median():.0f} dias")
    
    print("\n" + "="*60)

def main():
    """Executa todas as análises e gera os gráficos"""
    df = load_data()
    
    # Mostra estatísticas primeiro
    mostrar_estatisticas(df)
    
    # Gera gráficos
    print("🎨 Gerando gráficos...")
    gerar_graficos(df)
    print(f"✅ Análise completa! {len(df)} repositórios analisados.")
    print("📊 Gráficos salvos em 'graficos/'")
    print("📈 Estatísticas exibidas acima.")

if __name__ == "__main__":
    main()
