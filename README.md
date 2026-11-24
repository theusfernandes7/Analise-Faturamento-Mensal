# Análise de Faturamento Mensal

Projeto em Python que lê uma planilha Excel com várias abas, identifica o valor de **Total Bruto** em cada aba, organiza os resultados em uma tabela e gera um gráfico com o faturamento mensal e o total geral.

O projeto foi desenvolvido para praticar leitura e manipulação de planilhas, análise de dados e visualização de informações.

## Funcionalidades

- Recebe uma planilha Excel (`.xlsx`) pelo Google Colab.
- Percorre as abas da planilha.
- Procura o texto `Total Bruto:` em cada aba.
- Extrai o valor numérico localizado na célula seguinte.
- Organiza os valores em uma tabela com Pandas.
- Calcula o faturamento bruto total.
- Gera e disponibiliza para download um gráfico em PNG.

## Tecnologias utilizadas

- Python 3
- Pandas
- Matplotlib
- OpenPyXL
- Google Colab

## Estrutura do projeto

```text
analise-faturamento-mensal/
├── faturamento_mensal.py
├── README.md
├── requirements.txt
├── .gitignore
└── exemplo_faturamento.xlsx
```

## Como executar no Google Colab

1. Baixe o arquivo `faturamento_mensal.py` deste repositório.
2. Abra o [Google Colab](https://colab.research.google.com/).
3. Crie um novo notebook.
4. No painel de arquivos do Colab, envie o arquivo `faturamento_mensal.py`.
5. Em uma célula do notebook, execute:

   ```python
   %run faturamento_mensal.py
   ```

6. Quando solicitado, envie uma planilha Excel (`.xlsx`) que siga o formato esperado.
7. O programa exibirá a tabela e o gráfico, além de disponibilizar o PNG para download.

## Formato esperado da planilha

O programa percorre todas as abas do Excel. Em cada aba, procura uma célula cujo conteúdo seja exatamente `Total Bruto:` (desconsiderando maiúsculas, minúsculas e espaços nas extremidades). O valor numérico deve estar na célula imediatamente à direita.

O repositório inclui `exemplo_faturamento.xlsx`, com dados totalmente fictícios, apenas para demonstrar o formato esperado.

## Cuidados com os dados

Este projeto pode ser utilizado com planilhas financeiras. **Não publique planilhas reais da empresa, dados de clientes, funcionários ou informações comerciais confidenciais sem autorização.** O arquivo de exemplo deste repositório contém somente valores fictícios.

## Bibliotecas

As dependências estão listadas em `requirements.txt`. No Google Colab, Pandas e Matplotlib geralmente já estão disponíveis; caso necessário, instale as dependências com:

```python
!pip install -r requirements.txt
```

## Autor

Matheus dos Santos

GitHub: [@theusfernandes7](https://github.com/theusfernandes7)
