import argparse #analisar argumentos de linha de comando
import ast #árvore de sintaxe abstrata
import sys
import os  # Adicionado import necessário
import timeit #medir o tempo de execução de pequenos trechos de código
import importlib.util #importar módulos dinamicamente
import inspect #inspecionar objetos, como mód, class, fun e frames de pilha
import random #gerar números pseudoaleatórios e realizar seleções aleatórias
from typing import List, Tuple, Callable #Suporte para dicas de tipo. List: Indica uma lista onde todos os elementos são de um tipo específico
#Tuple: Similar ao List, mas para tuplas. Callable: Descreve um objeto que pode ser chamado, como uma função
import matplotlib.pyplot as plt #visualização de dados


class AnalisadorComplexidade(ast.NodeVisitor):
    def __init__(self):
        self.profundidade_laco = 0
        self.max_profundidade_laco = 0
        self.eh_recursiva = False
        self.nome_funcao = None
        self.tem_lacos_aninhados = False
        self.tipos_lacos = []

    def visit_FunctionDef(self, node):
        nome_funcao_anterior = self.nome_funcao
        self.nome_funcao = node.name
        self.generic_visit(node)
        self.nome_funcao = nome_funcao_anterior

    def visit_For(self, node):
        self.profundidade_laco += 1
        self.max_profundidade_laco = max(self.max_profundidade_laco, self.profundidade_laco)
        self.tipos_lacos.append('for')
        if self.profundidade_laco > 1:
            self.tem_lacos_aninhados = True
        self.generic_visit(node)
        self.profundidade_laco -= 1

    def visit_While(self, node):
        self.profundidade_laco += 1
        self.max_profundidade_laco = max(self.max_profundidade_laco, self.profundidade_laco)
        self.tipos_lacos.append('while')
        if self.profundidade_laco > 1:
            self.tem_lacos_aninhados = True
        self.generic_visit(node)
        self.profundidade_laco -= 1

    def visit_Call(self, node):#recursão
        if isinstance(node.func, ast.Name) and node.func.id == self.nome_funcao:
            self.eh_recursiva = True
        self.generic_visit(node)


def analisar_estatico(caminho_arquivo: str, nome_funcao: str) -> dict:

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo_fonte = arquivo.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo: {e}")

    try:
        arvore = ast.parse(codigo_fonte)
    except SyntaxError as e:
        raise SyntaxError(f"Erro de sintaxe no arquivo: {e}")

    no_funcao = None
    for no in ast.walk(arvore):
        if isinstance(no, ast.FunctionDef) and no.name == nome_funcao:
            no_funcao = no
            break

    if no_funcao is None:
        raise ValueError(f"Função '{nome_funcao}' não encontrada no arquivo.")

    analisador = AnalisadorComplexidade()
    analisador.nome_funcao = nome_funcao
    analisador.visit(no_funcao)

    complexidade = estimar_complexidade(analisador)

    return {
        'eh_recursiva': analisador.eh_recursiva,
        'max_profundidade_laco': analisador.max_profundidade_laco,
        'tem_lacos_aninhados': analisador.tem_lacos_aninhados,
        'tipos_lacos': analisador.tipos_lacos,
        'complexidade_estimada': complexidade
    }

def estimar_complexidade(analisador: 'AnalisadorComplexidade') -> str:
    if analisador.eh_recursiva:
        if analisador.max_profundidade_laco == 0:
            return "O(log n) ou O(n) - Recursão típica (ex: busca binária, divisão e conquista)"
        elif analisador.max_profundidade_laco == 1:
            return "O(n log n) - Recursão com divisão e conquista (ex: mergesort, quicksort)"
        else:
            return "O(n^k log n) - Recursão com múltiplos laços aninhados"
    else:
        if analisador.max_profundidade_laco == 0:
            return "O(1) - Constante"
        elif analisador.max_profundidade_laco == 1:
            return "O(n) - Linear"
        elif analisador.max_profundidade_laco == 2:
            return "O(n^2) - Quadrática"
        elif analisador.max_profundidade_laco == 3:
            return "O(n^3) - Cúbica"
        else:
            return f"O(n^{analisador.max_profundidade_laco}) - Polinomial de grau {analisador.max_profundidade_laco}"

def carregar_funcao_do_arquivo(caminho_arquivo: str, nome_funcao: str) -> Callable:
    try:
        especificacao = importlib.util.spec_from_file_location("modulo", caminho_arquivo)
        modulo = importlib.util.module_from_spec(especificacao)
        especificacao.loader.exec_module(modulo)
        if not hasattr(modulo, nome_funcao):
            raise AttributeError(f"Função '{nome_funcao} não encontrada no módulo.")
        return getattr(modulo, nome_funcao)
    except Exception as e:
        raise Exception(f"Erro ao carregar função: {e}")

def gerar_entrada_teste(tamanho: int) -> List[int]:
    return [random.randint(1, 100) for _ in range(tamanho)]

def analisar_empirico(caminho_arquivo: str, nome_funcao: str, tamanhos: List[int]) -> Tuple[List[int], List[float]]:
    funcao = carregar_funcao_do_arquivo(caminho_arquivo, nome_funcao)
    assinatura = inspect.signature(funcao)
    qtd_parametros = len(assinatura.parameters)
    if qtd_parametros == 0:
        raise ValueError(f"A função '{nome_funcao}' não aceita parâmetros.")
    tempos_execucao = []
    print(f"Executando análise empírica...")
    for tamanho in tamanhos:
        entrada_teste = gerar_entrada_teste(tamanho)
        def executar_funcao():
            copia_entrada = entrada_teste.copy()
            return funcao(copia_entrada)
        try:
            tempo_gasto = timeit.timeit(executar_funcao, number = 10) / 10
            tempos_execucao.append(tempo_gasto)
            print(f"N={tamanho}, Tempo: {tempo_gasto:.5f} segundos")
        except Exception as e:
            print(f"Erro ao executar a função com N={tamanho}: {e}")
            tempos_execucao.append(0)
    return tamanhos, tempos_execucao

def criar_grafico_performance(tamanhos: List[int], tempos_execucao: List[float], nome_funcao: str) -> str:
    plt.figure(figsize=(10, 6))
    plt.scatter(tamanhos, tempos_execucao, color='blue', alpha=0.5, s=50, label='Pontos de medição')
    plt.plot(tamanhos, tempos_execucao, color='red', alpha = 0.8, linewidth=2, label='Linha de tendência')
    plt.xlabel('Tamanho da Entrada (N)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title(f'Performance da Função {nome_funcao}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    nome_arquivo = f"performance_{nome_funcao}.png"
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    plt.close()
    return nome_arquivo

def main():
    parser = argparse.ArgumentParser(description="Analisador de Complexidade de Algoritmos", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="")

    # Adicionar argumentos necessários
    parser.add_argument('caminho_arquivo', help='Caminho para o arquivo Python contendo a função')
    parser.add_argument('nome_funcao', help='Nome da função a ser analisada')
    parser.add_argument('tamanhos', help='Tamanhos de entrada separados por vírgula (ex: 10,50,100,500)')

    argumentos = parser.parse_args()

    if not os.path.exists(argumentos.caminho_arquivo):
        print(f"Erro: O arquivo '{argumentos.caminho_arquivo}' não existe.")
        sys.exit(1)

    try:
        tamanhos = [int(x.strip()) for x in argumentos.tamanhos.split(',')]
        if not tamanhos:
            raise ValueError("Lista de tamanhos vazia.")
        if any(t <= 0 for t in tamanhos):
            raise ValueError("Tamanhos devem ser positivos.")
    except ValueError as e:
        print(f"Erro ao processar tamanhos: {e}")
        print("Use formato: '10,50,100,500' (números positivos separados por vírgula)")
        sys.exit(1)

    try:
        print("=" * 50)
        print(f"Análise do Algoritmo '{argumentos.nome_funcao}'")
        print(f"Arquivo: {argumentos.caminho_arquivo}")
        print("=" * 50)

        print("\nAnálise Estática (Estimativa Big O):")
        analisar_estatica = analisar_estatico(argumentos.caminho_arquivo, argumentos.nome_funcao)
        print(f"Função é recursiva: { 'Sim' if analisar_estatica['eh_recursiva'] else 'Não' }")
        print(f"Máxima profundidade de laços: {analisar_estatica['max_profundidade_laco']}")
        print(f"Tipos de laços encontrados: {', '.join(analisar_estatica['tipos_lacos']) if analisar_estatica['tipos_lacos'] else 'Nenhum'}")
        print(f"Complexidade estimada: {analisar_estatica['complexidade_estimada']}")

        print(f"\nAnálise Empírica de performance:")
        tamanhos_testados, tempos_execucao = analisar_empirico(argumentos.caminho_arquivo, argumentos.nome_funcao, tamanhos)

        nome_arquivo_grafico = criar_grafico_performance(tamanhos_testados, tempos_execucao, argumentos.nome_funcao)
        print(f"\nGráfico de performance salvo como '{nome_arquivo_grafico}'")

        print("=" * 50)
        print("Análise concluída com sucesso!")

    except Exception as e:
        print(f"Erro durante a análise: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()