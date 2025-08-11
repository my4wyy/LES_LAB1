# Relatório Inicial - Análise de Repositórios Populares no GitHub

**Grupo:**  
**Disciplina:** Laboratório de Experimentação de Software  

---
## 1. Introdução  
Este relatório preliminar apresenta hipóteses e metodologia para análise dos 1.000 repositórios mais populares do GitHub (com mais de 10k estrelas). O objetivo é investigar padrões de maturidade, contribuição, atualização e linguagens.

---

## 2. Hipóteses Informais  

### RQ01: Maturidade dos Repositórios  
**Hipótese:**  
> "Repositórios populares terão idade média superior a 5 anos, pois precisam de tempo para acumular estrelas e comunidade."

### RQ02: Contribuição Externa  
**Hipótese:**  
> "Repositórios com mais estrelas terão mediana de PRs aceitas acima de 500, indicando alta atividade de contribuidores externos."

### RQ03: Frequência de Releases  
**Hipótese:**  
> "A mediana de releases será maior que 20, sugerindo atualizações regulares (pelo menos 2-3 por ano)."

### RQ04: Atualização Recente  
**Hipótese:**  
> "Pelo menos 80% dos repositórios terão sido atualizados nos últimos 6 meses."

### RQ05: Linguagens Dominantes  
**Hipótese:**  
> "JavaScript, Python e Java representarão mais de 60% das linguagens primárias."

### RQ06: Gestão de Issues  
**Hipótese:**  
> "O percentual médio de issues fechadas será superior a 70%, indicando boa manutenção."

---

## 3. Metodologia  

### Coleta de Dados  
- **Fonte:** API GraphQL do GitHub.  
- **Amostra:** Top 1.000 repositórios com `stars:>10000`.  
- **Variáveis Coletadas:**  
  ```plaintext
  - Nome, proprietário, data de criação (createdAt), última atualização (updatedAt)  
  - Linguagem primária (primaryLanguage)  
  - Total de PRs aceitas (pullRequests), releases, issues abertas/fechadas  
  - Contagem de estrelas (stargazerCount) 

### Ferramentas

**Script Python:**
    - Biblioteca requests para consultas à API.
    - Paginação via cursor para coletar todos os 1.000 repositórios.

**Saída:**
    - Arquivo JSON (repos_1000.json) como backup.
    - Arquivo CSV (repos_1000.csv) para análise.

**Processo:**
    - Consulta à API com autenticação por token.
    - Paginação em lotes de 20 repositórios por requisição.
    - Tratamento de erros e delays entre requisições.