# Estudo de Python 3

Este repositório contém exercícios baseados no livro "Learn Python 3 the Hard Way". O objetivo é praticar a sintaxe fundamental, manipulação de arquivos e lógica de programação.

## Estrutura do Projeto

- `/exercises`: Scripts Python contendo os exercícios práticos.
  - `ex9.py`: Prática com strings multi-linha e caracteres de escape.
  - `ex17.py`: Script para cópia de arquivos via linha de comando.
- `/data`: Arquivos de texto utilizados para testes de entrada e saída.

## Como Executar

Para executar os scripts, utilize o terminal a partir da raiz do projeto.

### Exemplo Exercício 17:
```bash
python exercises/ex17.py data/file.txt data/ts.txt
```

## Notas de Estudo
- Uso de `argv` para capturar argumentos de linha de comando.
- Gerenciamento de arquivos utilizando `with open(...)` para garantir segurança e limpeza de recursos.
- Manipulação de strings e formatação com f-strings.