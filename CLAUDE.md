# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About this repository

This is a teaching repository for an Algorithms and Programming course (ADS 2026.1) at IFPI, taught by Professor Rogério Silva. It contains demonstrations, exercises, and student assessments across two languages: **Python** (primary) and **JavaScript** (Node.js/ES modules, secondary).

## Running code

**Python scripts** (no build step — run directly):
```bash
python3 <script.py>
```

**JavaScript scripts** (ES modules via Node.js):
```bash
node <script.js>
```
The project uses `readline-sync` for interactive input in JS. Install dependencies with:
```bash
yarn install
```

## Repository structure

Code is organized by topic unit (unidades), plus assessment folders and experiments:

- `unidade_1_operadores_aritmeticos/` — arithmetic operators; contains student submissions in `A_fabio_01/`
- `unidade_2_funcoes/` — functions and reusable procedures
- `unidade_3_condicionais/` — conditionals; includes shared utility modules (`utils_io.py`, `utils_geometria_plana.py`)
- `unidade_4_repeticao/` — loops (while/for); includes `io_utils.py` with validated input helpers
- `unidade_5_strings/` — string manipulation; includes its own `io_utils.py`
- `API_01_13Abril_2026_Turma_Normal/` — student submissions for the first assessment (API = Avaliação de Performance Individual), one subfolder per student
- `hello_javascript/` — introductory JS examples
- `projeto_turtle/` — Python turtle graphics demo

## Shared utility pattern

Both `unidade_3_condicionais/utils_io.py` and `unidade_4_repeticao/io_utils.py` / `unidade_5_strings/io_utils.py` follow the same pattern: thin wrappers around `input()` and `print()` with type coercion (`obter_inteiro`, `obter_numero_real`, `obter_texto`, `escrever`). The unidade_4 version adds validation loops (`obter_inteiro_min`, `obter_inteiro_positivo`).

## Conventions

- Python scripts use `input()` / `print()` directly or via the local `io_utils` / `utils_io` module.
- JavaScript scripts use `readline-sync`'s `question()` for interactive input and ES module syntax (`import`/`export`).
- Programs are structured as `main()` + helper functions, with `main()` called at the bottom.
- Variable names and comments are in **Portuguese**.
- No test framework is used; scripts are run and validated manually via stdin/stdout.
