# LAB02 - Análise de Qualidade em Repositórios Java

Este repositório contém os artefatos desenvolvidos para o *Laboratório de Experimentação de Software (LAB02), da disciplina **Laboratório de Experimentação de Software, no curso de **Engenharia de Software* (PUC Minas).  

O trabalho consiste em *analisar atributos de qualidade em repositórios Java* disponíveis no GitHub, utilizando métricas extraídas pela ferramenta *CK*.  

O objetivo é correlacionar características de qualidade (como acoplamento, coesão e profundidade de herança) com aspectos do processo de desenvolvimento dos repositórios, tais como:  
- *Popularidade* (número de estrelas)  
- *Tamanho* (linhas de código e comentários)  
- *Atividade* (número de releases)  
- *Maturidade* (idade do repositório)  

---

## Questões de Pesquisa

As *questões de pesquisa (RQs)* abordadas neste trabalho foram:  

1. Qual a relação entre a popularidade e a qualidade dos repositórios?  
2. Qual a relação entre a maturidade e a qualidade dos repositórios?  
3. Qual a relação entre a atividade e a qualidade dos repositórios?  
4. Qual a relação entre o tamanho e a qualidade dos repositórios?  

---

## Estrutura do Repositório

bash
├── data/        # Dados coletados (CSVs gerados pela ferramenta CK e APIs do GitHub)
├── results/     # Resultados das análises e gráficos gerados
├── scripts/     # Scripts utilizados para automação, coleta e análise
├── Relatorio.md # Relatório final com metodologia, resultados e discussão
├── Slide.pdf    # Apresentação utilizada na entrega
└── README.md    # Este arquivo

---

## Requisitos

- python 3.10+  
- java 8+  ]
- maven  
- token do GitHub no arquivo secrets/.env  
---

## Passos

1. Exportar variáveis do .env:  

   ```bash
   export $(cat secrets/.env | xargs)
