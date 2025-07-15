#!/usr/bin/env python3
"""
Exemplos de uso do Analisador de Complexidade de Algoritmos
"""

import os
import subprocess
import sys

def executar_comando(comando):
    """Executa um comando e mostra o resultado"""
    print(f"🔍 Executando: {comando}")
    print("="*60)
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado.stdout)
        if resultado.stderr:
            print("Erros:", resultado.stderr)
    except Exception as e:
        print(f"Erro ao executar comando: {e}")
    print("="*60)
    print()

def main():
    """Demonstra o uso do analisador com diferentes algoritmos"""

    print("🚀 DEMONSTRAÇÃO DO ANALISADOR DE COMPLEXIDADE")
    print("="*60)

    # Verificar se os arquivos existem
    if not os.path.exists("main.py"):
        print("❌ Arquivo main.py não encontrado!")
        return

    if not os.path.exists("algoritmos_teste.py"):
        print("❌ Arquivo algoritmos_teste.py não encontrado!")
        return

    print("✅ Arquivos encontrados. Iniciando demonstração...\n")

    # Exemplos de uso
    exemplos = [
        {
            "nome": "Algoritmo Linear (Busca Linear)",
            "comando": "python main.py algoritmos_teste.py busca_linear \"100,500,1000,2000\""
        },
        {
            "nome": "Algoritmo Quadrático (Bubble Sort)",
            "comando": "python main.py algoritmos_teste.py ordenacao_bolha \"10,50,100,200\""
        },
        {
            "nome": "Algoritmo Recursivo (Merge Sort)",
            "comando": "python main.py algoritmos_teste.py ordenacao_merge \"10,50,100,500\""
        },
        {
            "nome": "Algoritmo Cúbico",
            "comando": "python main.py algoritmos_teste.py algoritmo_cubico \"5,10,15,20\""
        },
        {
            "nome": "Busca Binária Recursiva",
            "comando": "python main.py algoritmos_teste.py busca_binaria_recursiva \"100,500,1000,2000\""
        }
    ]

    for i, exemplo in enumerate(exemplos, 1):
        print(f"📊 EXEMPLO {i}: {exemplo['nome']}")
        executar_comando(exemplo["comando"])

        # Pausa entre exemplos
        input("Pressione Enter para continuar para o próximo exemplo...")
        print()

    print("🎉 Demonstração concluída!")
    print("📈 Verifique os gráficos gerados (performance_*.png)")

if __name__ == "__main__":
    main()
