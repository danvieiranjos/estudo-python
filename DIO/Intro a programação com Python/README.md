# 📚 Introdução à Programação com Python

Repositório com exercícios práticos e exemplos de código de um curso progressivo de **Introdução à Programação com Python** da DIO (Digital Innovation One). O projeto abrange desde conceitos básicos até tópicos intermediários da linguagem.

---

## 📋 Conteúdo do Projeto

### 🎯 Progressão de Aprendizado

O projeto está organizado de forma progressiva, começando com conceitos básicos e evoluindo para tópicos mais avançados:

#### **Nível Básico (Aulas 3-5)**
- Variáveis e tipos de dados
- Estruturas condicionais (`if/elif/else`)
- Loops (`for` e `while`) com validação
- Listas e operadores

#### **Nível Intermediário (Aulas 7-10)**
- Programação Orientada a Objetos (Classes)
- Funções e funções lambda
- Manipulação de arquivos
- Módulos e importações
- Trabalhando com datas e horas

#### **Nível Intermediário-Avançado (Aulas 11-12)**
- Tratamento de exceções
- Exceções personalizadas
- Requisições HTTP e APIs REST
- Web scraping

---

## 📁 Estrutura do Projeto

### Arquivos na Raiz

| Arquivo | Assunto | Descrição |
|---------|---------|-----------|
| `aula3.py` | Estruturas Condicionais | Encontra o maior número entre valores e classifica como par/ímpar |
| `aula4.py` | Loops (for) | Itera números e identifica números primos |
| `aula4_II.py` | Loops (while) com Validação | Coleta notas de 4 bimestres e calcula média |
| `aula4-II.py` | Loops com Validação | Versão corrigida com aprovação/reprovação |
| `aula5.py` | Listas e Operadores | Operações com listas, operador `in` e métodos `.count()` |
| `aula7.py` | POO - Classes | Classe `Calculadora` com operações básicas |
| `aula7_TV.py` | POO - Classes | Classe `Televisao` com controle remoto |

### Pasta `app_python/`

| Arquivo | Assunto | Descrição |
|---------|---------|-----------|
| `aula3.py` | Estruturas Condicionais | Classificação de números |
| `aula4.py` | Loops e Validação | Cálculo de média com validação |
| `aula5.py` | Listas | Operações com estruturas de dados |
| `aula7_caculadora1.py` | Classes | Implementação de calculadora |
| `aula7_calculadora2.py` | Classes | Versão alternativa da calculadora |
| `aula7_televisao.py` | Classes | Controle de televisão com testes |
| `aula8_contador_letras.py` | Funções | Contagem de letras em palavras |
| `aula8_importacao.py` | Módulos | Importação e reutilização de classes |
| `aula8_lambda.py` | Funções Lambda | Funções anônimas para operações |
| `aula9.py` | Arquivos | Leitura/escrita de arquivos e cálculo de médias |
| `aula10.py` | Módulo datetime | Manipulação de datas e horas |
| `aula11.py` | Exceções | Try/except para tratamento de erros |
| `aula11_personalizar_excecao.py` | Exceções Personalizadas | Classe `InputError` customizada com validação |
| `aula12.py` | APIs REST | Requisições HTTP com ViaCEP e PokéAPI |
| `web_scraping.py` | Web Scraping | Importações para web scraping |

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado
- (Opcional) Ambiente virtual configurado

### Executar um Arquivo

```bash
python nome_arquivo.py
```

Exemplo:
```bash
python app_python/aula7_televisao.py
python app_python/aula12.py
```

---

## 📦 Dependências

A maioria dos arquivos usa apenas a biblioteca padrão do Python. Para os arquivos que requerem pacotes externos:

- **aula12.py**: `requests` (para requisições HTTP)
- **web_scraping.py**: `beautifulsoup4`, `pandas` (para web scraping)

Para instalar as dependências opcionais:

```bash
pip install requests beautifulsoup4 pandas
```

---

## 📝 Conceitos Abordados

- ✅ Variáveis e tipos de dados
- ✅ Operadores (aritméticos, lógicos, de comparação)
- ✅ Estruturas de controle (`if`, `elif`, `else`)
- ✅ Loops (`for`, `while`)
- ✅ Listas, tuplas e dicionários
- ✅ Funções e funções lambda
- ✅ Programação Orientada a Objetos (classes, herança, métodos)
- ✅ Tratamento de exceções
- ✅ Manipulação de arquivos
- ✅ Módulos e importações
- ✅ Datas e horas
- ✅ Requisições HTTP e APIs
- ✅ Web scraping (introdução)

---

## ⚠️ Notas Importantes

- Este é um projeto educacional em progresso
- Alguns arquivos contêm erros intencionais para fins de aprendizado
- Os exercícios estão organizados para seguir uma progressão lógica
- Recomenda-se estudar os arquivos em ordem numérica

---

## 💡 Dicas de Estudo

1. **Comece pela raiz**: Execute primeiro os arquivos da raiz (aula3.py → aula7_TV.py)
2. **Depois explore app_python**: Continue com os arquivos em ordem numérica na pasta `app_python`
3. **Identifique padrões**: Observe como os conceitos se conectam entre aulas
4. **Experimente modificações**: Tente modificar e estender o código para praticar
5. **Procure pelos erros**: Alguns arquivos têm bugs - tente identificá-los e corrigi-los

---

## 👤 Autor

Projeto educacional - Baseado no curso da DIO (Digital Innovation One)

---

**Última atualização**: Junho de 2026
