# Analisador de Complexidade de Algoritmos

Um analisador Python que combina análise estática e empírica para determinar a complexidade computacional de algoritmos.

## 📋 Descrição

Este projeto permite analisar a complexidade de algoritmos Python através de duas abordagens:

- **Análise Estática**: Examina o código fonte para estimar a complexidade Big O baseada na estrutura do código (laços, recursão, etc.)
- **Análise Empírica**: Executa o algoritmo com diferentes tamanhos de entrada e mede o tempo de execução real

## 🚀 Funcionalidades

- ✅ Análise automática de complexidade Big O
- ✅ Detecção de recursão e laços aninhados
- ✅ Medição de performance em tempo real
- ✅ Geração de gráficos de performance
- ✅ Suporte para múltiplos tipos de algoritmos
- ✅ Interface de linha de comando intuitiva

## 📦 Instalação

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Instalando dependências

```bash
# Clone o repositório ou baixe os arquivos
cd Analisador

# Instale as dependências
pip install -r requirements.txt
```

### Dependências incluídas

- `matplotlib==3.10.3` - Para geração de gráficos
- `numpy==2.3.1` - Para cálculos numéricos

## 🎯 Como Usar

### Sintaxe Básica

```bash
python main.py <caminho_arquivo> <nome_funcao> <tamanhos_entrada>
```

### Parâmetros

- `caminho_arquivo`: Caminho para o arquivo Python contendo a função
- `nome_funcao`: Nome da função a ser analisada
- `tamanhos_entrada`: Tamanhos de entrada separados por vírgula (ex: 10,50,100,500)

### Exemplos de Uso

#### 1. Analisando Busca Linear

```bash
python main.py algoritmos_teste.py busca_linear "100,500,1000,2000"
```

#### 2. Analisando Bubble Sort

```bash
python main.py algoritmos_teste.py ordenacao_bolha "10,50,100,200"
```

#### 3. Analisando Merge Sort

```bash
python main.py algoritmos_teste.py ordenacao_merge "10,50,100,500"
```

#### 4. Analisando Algoritmo Cúbico

```bash
python main.py algoritmos_teste.py algoritmo_cubico "5,10,15,20"
```

#### 5. Analisando Busca Binária Recursiva

```bash
python main.py algoritmos_teste.py busca_binaria_recursiva "100,500,1000,2000"
```

### Demonstração Automatizada

Para uma demonstração completa com todos os algoritmos de exemplo:

```bash
python exemplo_uso.py
```

Este script executará automaticamente várias análises e pausará entre cada exemplo.

## 📊 Saída do Programa

O programa gera:

1. **Análise Estática** - Informações sobre:
   - Se a função é recursiva
   - Profundidade máxima de laços
   - Tipos de laços encontrados
   - Complexidade estimada (Big O)

2. **Análise Empírica** - Medições de:
   - Tempo de execução para cada tamanho de entrada
   - Progressão do tempo conforme o tamanho aumenta

3. **Gráfico de Performance** - Arquivo PNG com:
   - Pontos de medição plotados
   - Linha de tendência
   - Visualização da curva de crescimento

### Exemplo de Saída

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
🔍 Executando análise empírica...
N=10, Tempo: 0.00025 segundos
N=50, Tempo: 0.00156 segundos
N=100, Tempo: 0.00623 segundos
N=200, Tempo: 0.02489 segundos

Gráfico de performance salvo como 'performance_ordenacao_bolha.png'

==================================================
Análise concluída com sucesso!
```

## 📁 Estrutura do Projeto

```
Analisador/
├── main.py                 # Programa principal
├── algoritmos_teste.py     # Algoritmos de exemplo para teste
├── exemplo_uso.py          # Script de demonstração
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🧪 Algoritmos de Teste Incluídos

O arquivo `algoritmos_teste.py` contém implementações de vários algoritmos clássicos:

- **O(n)**: Busca Linear, Soma de Elementos
- **O(n log n)**: Merge Sort
- **O(n²)**: Bubble Sort, Selection Sort, Insertion Sort
- **O(n³)**: Algoritmo Cúbico, Floyd-Warshall
- **O(log n)**: Busca Binária Recursiva
- **O(2ⁿ)**: Fibonacci Recursivo
- **Backtracking**: Problema das N-Rainhas

## 🔧 Criando Seus Próprios Algoritmos

Para analisar seus próprios algoritmos:

1. Crie um arquivo Python com sua função
2. A função deve aceitar pelo menos um parâmetro (lista de inteiros)
3. Execute o analisador apontando para seu arquivo

Exemplo de função personalizada:

```python
def meu_algoritmo(lista):
    # Sua implementação aqui
    resultado = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            resultado += lista[i] * lista[j]
    return resultado
```

Análise:

```bash
python main.py meu_arquivo.py meu_algoritmo "10,50,100"
```

## ⚠️ Limitações e Considerações

- A análise estática é uma estimativa baseada na estrutura do código
- Algoritmos com complexidade dependente de dados podem variar
- Funções muito lentas podem demorar com entradas grandes
- O analisador assume que a função aceita uma lista como primeiro parâmetro

## 📈 Interpretando os Resultados

- **O(1)**: Tempo constante - não depende do tamanho da entrada
- **O(log n)**: Logarítmico - cresce muito lentamente
- **O(n)**: Linear - tempo proporcional ao tamanho da entrada
- **O(n log n)**: Log-linear - típico de algoritmos eficientes de ordenação
- **O(n²)**: Quadrático - tempo cresce rapidamente
- **O(n³)**: Cúbico - muito lento para entradas grandes
- **O(2ⁿ)**: Exponencial - impraticável para entradas médias/grandes

...
