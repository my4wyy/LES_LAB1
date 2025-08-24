# Relatório - Análise de Repositórios Populares no GitHub

**Grupo:**  
- Gabriel Faria
- João Victor Salim
- Lucas Garcia
- Maísa Pires
- Miguel Vieira

**Disciplina:** Laboratório de Experimentação de Software  

---
## 1. Introdução  
Este relatório preliminar apresenta hipóteses e metodologia para análise dos 1.000 repositórios mais populares do GitHub (com mais de 10k estrelas). O objetivo é investigar padrões de maturidade, contribuição, atualização e linguagens.

---

## 2. Hipóteses Informais  

### RQ01: Maturidade dos Repositórios  
**Hipótese:**  
> "Repositórios populares terão idade média superior a 5 anos, pois precisam de tempo para acumular estrelas e comunidade."

Acreditamos nisso porque ganhar muitas estrelas leva tempo: o projeto precisa ser descoberto, testado e recomendado por muita gente. Quanto mais tempo no ar, maior a chance de formar comunidade, receber melhorias e passar por vários ciclos de evolução. Em empresas e cursos, a preferência por tecnologias estáveis também favorece projetos que já provaram seu valor.

### RQ02: Contribuição Externa  
**Hipótese:**  
> "Repositórios com mais estrelas terão mediana de PRs aceitas acima de 500, indicando alta atividade de contribuidores externos."

Projetos muito estrelados normalmente têm caminho de contribuição bem explicado (README, CONTRIBUTING, rótulos como “good first issue”) e rotinas de revisão claras. Isso reduz barreiras para quem quer ajudar, então chegam mais PRs e muitos acabam sendo mesclados. No longo prazo, esse fluxo constante eleva a mediana de PRs aceitos por projeto.

### RQ03: Frequência de Releases  
**Hipótese:**  
> "A mediana de releases será maior que 20, sugerindo atualizações regulares (pelo menos 2-3 por ano)."

Times de projetos populares tendem a publicar versões menores e frequentes para reduzir riscos e manter usuários atualizados. Ferramentas de automatização (CI/CD, changelog) barateiam o custo de lançar, então a contagem de releases cresce naturalmente. Em ecossistemas com gerenciadores de pacote (npm, PyPI, etc.), essa cadência é ainda mais comum.

### RQ04: Atualização Recente  
**Hipótese:**  
> "Pelo menos 80% dos repositórios terão sido atualizados nos últimos 6 meses."

Projetos grandes sofrem demanda contínua: correções de bugs, ajustes de segurança e compatibilidade com novas dependências. Além do trabalho do time e da comunidade, bots de atualização (dependências, alertas de segurança) geram atividade regular. O resultado é que uma fatia alta dos repositórios populares costuma ter updatedAt recente (últimos meses).

### RQ05: Linguagens Dominantes  
**Hipótese:**  
> "JavaScript, Python e Java representarão mais de 60% das linguagens primárias."

Essas linguagens têm bases de usuários enormes e aplicações muito amplas: web (JS/TS), dados e IA (Python) e backend/Android (Java). Como muita gente usa e aprende essas stacks, os projetos nelas tendem a ganhar mais visibilidade e estrelas. Por isso, ao olhar os “tops”, é natural que elas apareçam como principais em boa parte dos repositórios.

### RQ06: Gestão de Issues  
**Hipótese:**  
> "O percentual médio de issues fechadas será superior a 70%, indicando boa manutenção."

Projetos populares costumam ter processos simples e objetivos para triagem: templates, rótulos, política de duplicados e vínculo entre PR e issue. A comunidade também ajuda a reproduzir problemas e propor correções. Com esse fluxo, fechar issues vira rotina e sustenta percentuais de fechamento mais altos ao longo do tempo.

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
