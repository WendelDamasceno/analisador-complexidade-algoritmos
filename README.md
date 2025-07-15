# 🔍 Analisador de Complexidade de Algoritmos

Um analisador de código Python capaz de avaliar algoritmos em termos de complexidade e eficiência, desenvolvido como projeto acadêmico.

## 📋 Funcionalidades

### 🔬 Análise Estática
- **Identificação de complexidade assintótica (Big O)**: Detecta automaticamente O(1), O(n), O(n²), O(n³), O(log n), O(n log n)
- **Reconhecimento de padrões**: Identifica recursão, laços aninhados, divisão e conquista
- **Análise estrutural**: Conta profundidade de laços e tipos de estruturas de controle

### 📊 Análise Empírica
- **Medição de tempo real**: Executa algoritmos com diferentes tamanhos de entrada
- **Visualização gráfica**: Gera gráficos de performance automaticamente
- **Análise comparativa**: Permite comparar diferentes implementações

### 🛠️ Características Técnicas
- Interface de linha de comando profissional
- Tratamento robusto de erros
- Suporte para múltiplos tamanhos de entrada
- Geração automática de relatórios

## 📁 Estrutura do Projeto

```
├── main.py                    # Analisador principal
├── algoritmos_teste.py        # Algoritmos de teste
├── requirements.txt           # Dependências
├── README.md                 # Este arquivo
└── exemplos/                 # Exemplos de uso
```

## 🚀 Instalação

### Pré-requisitos
- Python 3.7+
- pip

### Instalação das dependências
```bash
pip install -r requirements.txt
```

Ou criar um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## 📖 Como usar

### Sintaxe básica
```bash
python main.py <caminho_arquivo> <nome_funcao> <tamanhos>
```

### Exemplos de uso

**Analisar algoritmo de ordenação bolha:**
```bash
python main.py algoritmos_teste.py ordenacao_bolha "10,50,100,200"
```

**Analisar merge sort:**
```bash
python main.py algoritmos_teste.py ordenacao_merge "10,50,100,500"
```

**Analisar busca binária:**
```bash
python main.py algoritmos_teste.py busca_binaria_recursiva "100,500,1000,2000"
```

**Analisar algoritmo cúbico:**
```bash
python main.py algoritmos_teste.py algoritmo_cubico "5,10,15,20"
```

## 📊 Exemplo de Saída

```
==================================================
Análise do Algoritmo 'ordenacao_bolha'
Arquivo: algoritmos_teste.py
==================================================

Análise Estática (Estimativa Big O):
Função é recursiva: Não
Máxima profundidade de laços: 2
Tipos de laços encontrados: for, for
Complexidade estimada: O(n^2) - Quadrática

Análise Empírica de performance:
Executando análise empírica...
N=10, Tempo: 0.00001 segundos
N=50, Tempo: 0.00011 segundos
N=100, Tempo: 0.00031 segundos
N=200, Tempo: 0.00122 segundos

Gráfico de performance salvo como 'performance_ordenacao_bolha.png'
==================================================
Análise concluída com sucesso!
```

## 🧪 Algoritmos Testados

O projeto inclui implementações de algoritmos clássicos para teste:

### Ordenação
- **Bubble Sort** (O(n²)) - Ordenação por bolha
- **Insertion Sort** (O(n²)) - Ordenação por inserção
- **Selection Sort** (O(n²)) - Ordenação por seleção  
- **Merge Sort** (O(n log n)) - Ordenação por divisão e conquista

### Busca
- **Linear Search** (O(n)) - Busca linear
- **Binary Search** (O(log n)) - Busca binária recursiva

### Algoritmos Avançados
- **Floyd-Warshall** (O(n³)) - Caminhos mínimos em grafos
- **N-Queens Backtracking** - Problema das N rainhas
- **Fibonacci Recursivo** - Sequência de Fibonacci

## 🔧 Tecnologias Utilizadas

- **Python 3.11**
- **AST (Abstract Syntax Tree)** - Análise estática do código
- **timeit** - Medição precisa de tempo
- **matplotlib** - Visualização de dados
- **argparse** - Interface de linha de comando

## 📈 Complexidades Detectadas

| Complexidade | Descrição | Exemplo |
|-------------|-----------|---------|
| O(1) | Constante | Acesso a array |
| O(n) | Linear | Busca linear |
| O(n²) | Quadrática | Bubble sort |
| O(n³) | Cúbica | Floyd-Warshall |
| O(log n) | Logarítmica | Busca binária |
| O(n log n) | Linearítmica | Merge sort |

## 🎯 Objetivos Acadêmicos

Este projeto foi desenvolvido para demonstrar:
- Compreensão de análise de algoritmos
- Implementação de analisadores de código
- Técnicas de análise estática e empírica
- Visualização de dados de performance
- Boas práticas de desenvolvimento Python

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos.

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para a disciplina de Análise de Algoritmos.

---

**📧 Contato**: Para dúvidas ou sugestões, entre em contato através do GitHub.
