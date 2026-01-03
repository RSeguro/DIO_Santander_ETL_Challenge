# 🚀 Pipeline de ETL: Otimizador de Retenção de Clientes

Este projeto foi desenvolvido como um desafio pratico para consolidar os conhecimentos adquiridos sobre **ETL** utilizando **Python** e a biblioteca **Pandas**. O objetivo é simular um cenário real de e-commerce onde dados de diferentes fontes são integrados e processados para gerar campanhas de marketing personalizadas.

## 📌 Cenário do Desafio
Uma empresa de e-commerce precisa reativar clientes que abandonaram carrinhos de compras. O pipeline deve identificar clientes inativos há mais de 7 dias e gerar mensagens de retenção personalizadas com base no valor do produto esquecido.

## 🛠️ Tecnologias Utilizadas
*   **Linguagem:** Python 3.14.0
*   **Manipulação de Dados:** Pandas
*   **Ambiente:** Virtualenv (venv)

## ⚙️ O Pipeline de ETL

### 1. Extração (Extract)
Os dados são extraídos de dois arquivos CSV distintos:
*   `clientes.csv`: Contém informações cadastrais (ID, Nome, Email, Categoria_Fidelidade);
*   `compras.csv`: Contém informações do carrinho de compras (ID_Cliente, Ultimo_Produto_Visto, Valor_No_Carrinho, Dias_Desde_Ultima_Visita).

### 2. Transformação (Transform)
Esta é a logica do projeto, onde o **Pandas** é utilizado para:
*   **Merge de Dados:** Unificação das tabelas de clientes e compras através de chaves primárias;
*   **Limpeza (Data Cleaning):** Tratamento de valores nulos (`isnull`) e remoção de colunas redundantes;
*   **Regra de Negócio:** Filtragem de clientes inativos e segmentação por faixa de preço;
*   **Otimização:** Uso do método `.apply()` para processamento eficiente das mensagens personalizadas.

### 3. Carga (Load)
O resultado final é exportado para um novo arquivo `campanha-retencao.csv`, utilizando codificação `utf-8-sig` para garantir compatibilidade total com ferramentas como Microsoft Excel.

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
