# Laboratório de Experimentação de Software

## Integrantes:
- Gabriel Faria
- João Victor Salim
- Lucas Garcia
- Maísa Pires
- Miguel Vieira

## Descrição
Este repositório reúne o desenvolvimento completo do **Laboratório 01 - Características de Repositórios Populares** da disciplina *Laboratório de Experimentação de Software*, ministrada pelo professor João Paulo Carneiro Aramuni no curso de Engenharia de Software.

O objetivo principal é estudar e analisar as características de sistemas open-source populares no GitHub, considerando métricas como maturidade, contribuições externas, frequência de releases, atualização e popularidade da linguagem de programação.

O trabalho será realizado em três etapas (Lab01S01, Lab01S02 e Lab01S03), cobrindo desde a coleta de dados até a análise final com visualização e discussão de resultados.

---

## Questões de Pesquisa (RQs)
- **RQ01:** Sistemas populares são maduros/antigos?  
  *Métrica:* idade do repositório (data de criação).
- **RQ02:** Sistemas populares recebem muita contribuição externa?  
  *Métrica:* total de pull requests aceitas.
- **RQ03:** Sistemas populares lançam releases com frequência?  
  *Métrica:* total de releases.
- **RQ04:** Sistemas populares são atualizados com frequência?  
  *Métrica:* tempo até a última atualização.
- **RQ05:** Sistemas populares são escritos nas linguagens mais populares?  
  *Métrica:* linguagem primária do repositório.
- **RQ06:** Sistemas populares possuem um alto percentual de issues fechadas?  
  *Métrica:* razão entre issues fechadas e total de issues.
- **RQ07 (Bônus):** Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?  

---

## Etapas do Trabalho

### **Lab01S01 - Coleta Inicial de 100 Repositórios**
- Implementação de uma query GraphQL para coletar dados de 100 repositórios mais populares do GitHub.
- Obtenção de todas as métricas necessárias para as RQs.
- Armazenamento dos dados coletados em formato `.json`.
- Verificação do limite de requisições (`rate limit`) antes da coleta.

### **Lab01S02 - Paginação e Coleta de 1000 Repositórios**
- Implementação de paginação para coletar 1000 repositórios.
- Armazenamento dos dados em formato `.csv`.
- Elaboração das hipóteses informais iniciais para cada RQ.

### **Lab01S03 - Análise e Relatório Final**
- Análise estatística dos dados coletados.
- Visualização dos resultados (gráficos e tabelas).
- Discussão e comparação com as hipóteses informais.
- Análise adicional da RQ07 (bônus) separando resultados por linguagem.


