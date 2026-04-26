# MGPEB: Missão Aurora Siger - Controlador de Aproximação e Pouso

Este repositório contém o protótipo do sistema **MGPEB** (Módulo de Gerenciamento de Pouso e Engenharia de Base), desenvolvido como parte da Atividade Integradora do curso de Ciência da Computação da FIAP. O sistema é responsável por gerenciar a sequência autônoma de desacoplamento e descida de cinco módulos da missão de colonização a Marte.

## 🚀 Sobre o Projeto
O MGPEB simula a tomada de decisão autônoma em tempo real, necessária devido ao atraso de comunicação entre a Terra e Marte. O sistema utiliza estruturas de dados para organizar a fila de pouso, algoritmos para otimizar a ordem de descida baseada em criticidade e combustível, e lógica booleana para validar condições de segurança (meteorológicas e estruturais) antes de autorizar a descida.



## 🛠 Funcionalidades
* **Gerenciamento de Fila:** Uso de `deque` (fila FIFO) para processamento sequencial de módulos.
* **Ordenação Dinâmica:** Algoritmo de ordenação parametrizado para priorizar módulos com base em `criticidade` ou `combustível`.
* **Motor de Regras (Lógica de Decisão):** Validação de segurança baseada em múltiplas variáveis (combustível, vento, visibilidade, status do sensor).
* **Estruturas de Dados:** Integração de listas, filas e pilhas para gerenciar o estado da missão.

## 📋 Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Conceitos Aplicados:**
    * Estruturas de Dados (Filas, Pilhas, Listas)
    * Algoritmos de Ordenação (Timsort) e Busca
    * Lógica Booleana e Portas Lógicas

## ⚙️ Como Executar
1. Certifique-se de ter o Python instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/Traiba/projeto_aurora_2.git
3. Rode utilizando `python3 mgpeb_main.py`
