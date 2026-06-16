# HandsOn Python

Este repositório reúne exercícios e projetos em Python para estudo e prática. A ideia é manter uma organização clara entre scripts de treino, subprojetos e recursos auxiliares.

## Estrutura reorganizada

- `scripts/` — scripts principais de estudo em Python, programas interativos e exemplos rápidos.
- `subprojetos/` — projetos de treino ou testes maiores, com organização própria.
- `notebooks/` — notebooks Jupyter usados para estudos e experimentos.
- `docs/` — documentos auxiliares, notas e arquivos de referência.

## Scripts principais (`scripts/`)

- `CountWords.py` — conta frequência de palavras a partir de um arquivo de texto.
- `gerarSenha.py` — gera senhas aleatórias com letras, números e símbolos.
- `jogarDado.py` — simulador de lançamento de dado com opção de novo jogo ou sair.
- `printRainbow.py` — desenha uma forma colorida usando `arcade`.
- `Sistema Bancario.py` — sistema bancário simples com depósito, saque, extrato, usuário e contas.
- `speechText.py` — converte texto em fala usando `gtts` e reproduz o áudio com `playsound`.
- `WebScraping.py` — exemplo de scraping com `requests`, `pandas` e `BeautifulSoup`.
- `VariosgetURL/main.py` — lê URLs de `teste.csv` e verifica se um texto bloqueado aparece nas respostas.

## Subprojetos de treino (`subprojetos/`)

### `subprojetos/HandsOn-Python/`
- `IMC.py` — calculadora de índice de massa corporal.
- `importCSV.py` — converte CSV em documentos para MongoDB.

### `subprojetos/hiring-challenges-master/`
- `countstrings.py` — conta quantas vezes um caractere aparece em uma frase.
- `reverselist.py` — demonstra várias formas de inverter uma lista.
- `sort.py` — ordena uma lista usando `sort()` e uma implementação manual.

### `subprojetos/MyBudget_Alunos/MyBudget/`
- `app.py` — configuração inicial de um app Dash.
- `myindex.py` — layout básico do app Dash.

### `subprojetos/YouTube Subtitle/`
- `youtube_subtitle_generator.py` — gera legendas `.srt` ou `.vtt` para vídeos do YouTube.
- `README.md` — documentação específica do subprojeto.

## Notebooks

- `notebooks/Producer.ipynb` — notebook de estudo ou experimento para aprendizado em Python.

## Documentos auxiliares

- `docs/Script para Gerar CSV de PDF.txt` — notas ou script de referência para gerar CSV a partir de PDF.

## Como usar

### Executar um script do `scripts/`

```bash
cd scripts
python nome_do_arquivo.py
```

Exemplos:

```bash
cd scripts
python gerarSenha.py
python jogarDado.py
```

### Rodar o app Dash

```bash
cd subprojetos/MyBudget_Alunos/MyBudget
python app.py
```

Em seguida, abra o navegador em `http://127.0.0.1:8051/`.

### Usar o gerador de legendas do YouTube

```bash
cd subprojetos/YouTube Subtitle
python youtube_subtitle_generator.py <URL_DO_VIDEO>
```

Consulte `subprojetos/YouTube Subtitle/README.md` para opções avançadas.

## Dependências comuns

Alguns scripts exigem pacotes adicionais:

- `arcade` — usado por `scripts/printRainbow.py`
- `gtts`, `playsound` — usado por `scripts/speechText.py`
- `requests`, `pandas`, `beautifulsoup4` — usados por `scripts/WebScraping.py`
- `dash`, `dash-bootstrap-components`, `plotly` — usados por `subprojetos/MyBudget_Alunos/MyBudget`
- `pymongo` — usado por `subprojetos/HandsOn-Python/importCSV.py`
- `yt-dlp`, `openai-whisper` — usados por `subprojetos/YouTube Subtitle/youtube_subtitle_generator.py`

Recomendação:

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Não há um `requirements.txt` padrão, então instale apenas os pacotes necessários para os scripts que deseja executar.

## Objetivo do repositório

Esta coleção é destinada ao aprendizado progressivo de Python. Os arquivos em `scripts/` são exemplos e pequenos exercícios; os itens em `subprojetos/` representam estudos maiores, testes de conceitos ou projetos mais completos.

Use esta estrutura para encontrar rapidamente o conteúdo certo para cada tipo de estudo e manter o projeto organizado.