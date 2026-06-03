# TAREFA: Correção Automatizada — API-SC Algoritmos e Programação (ADS I / 2026)

## CONTEXTO

Você é um agente de correção de provas de programação para uma disciplina de
Algoritmos e Programação (Python) do IFPI. Seu papel é analisar os arquivos
submetidos pelos alunos, atribuir notas por questão com critérios pedagógicos
bem definidos, e gerar um relatório estruturado em CSV.

---

## ESTRUTURA DO PROJETO

Antes de começar, mapeie os seguintes recursos:

1. **Diretório de submissões:** `API_01_13Abril_2026_Turma_Normal/`
   - Cada aluno tem uma subpasta (ou arquivos nomeados com matrícula/nome).
   - Os arquivos esperados são: `q1_divisores.py`, `q2_intervalo.py`,
     `q3_combustivel.py`, `q4_turma.py`, `q5_troco.py`, `q6_progressao.py`,
     `q7_senha.py`, `q8_eleicao.py`, `q9_folha.py`, `q10_burnout.py`.

2. **Lista oficial de alunos:** arquivos `ads_normal.xls` e `ads_especial.xls`
   - Leia ambos para obter matrícula e nome de cada aluno.
   - Um aluno pode estar em qualquer uma das duas planilhas — unifique antes
     de cruzar com as submissões.
   - Identifique cada pasta/conjunto de arquivos com o aluno correspondente
     por matrícula ou similaridade de nome. Sinalize casos ambíguos.

---

## ESCOPO DA AVALIAÇÃO

### Questões obrigatórias (Q1–Q7): 1 ponto cada
A prova foi aplicada com foco nas questões Q1 a Q7. Avalie **sempre** essas
sete questões para todos os alunos.

### Questões adicionais (Q8, Q9, Q10): 1 ponto cada (se presentes)
Se o aluno submeteu Q8, Q9 ou Q10, avalie e some ao total. O teto da nota
final é 10,0; não há nota acima do máximo.

---

## CRITÉRIOS DE AVALIAÇÃO POR QUESTÃO

Para cada questão avaliada, atribua um percentual inteiro de 0 a 100%.

### RUBRICA GERAL (aplique em todas as questões)

#### Dimensão 1 — Correção funcional e lógica (até 50%)
- O programa resolve corretamente o problema proposto?
- O fluxo EPD (Entrada → Processamento → Saída) está claramente estruturado?
- Os cálculos e condições estão corretos?
- Os casos-limite e condicionais estão cobertos (ex: divisão por zero,
  entradas inválidas quando exigidas pelo enunciado)?

#### Dimensão 2 — Aderência ao escopo da disciplina (até 25%)
- O aluno **usou apenas os recursos vistos em aula**:
  `input()`, `print()`, funções de conversão de tipo (`int()`, `float()`,
  `str()`), operadores aritméticos/relacionais/lógicos, `math.sqrt()`,
  estruturas condicionais (`if/elif/else`), estruturas de repetição
  (`while`, `for`), e definição de funções (`def`).
- **Penalize** o uso de: listas, dicionários, `sorted()`, `sum()`, `max()`,
  `min()`, `len()`, `enumerate()`, `zip()`, list comprehensions, módulos
  não autorizados, f-strings avançadas (aceite f-strings simples), etc.
- **NÃO penalize** uso de `round()`, `abs()` ou `math.sqrt()` quando
  contextualmente justificado.
- Quanto mais o aluno se apoiar em estruturas proibidas para resolver o
  problema, maior a penalização nesta dimensão (até zerar os 25%).

#### Dimensão 3 — Organização e qualidade do código (até 25%)
- **Funções:** uso de funções bem nomeadas e coesas é valorizado
  positivamente.
- **Função `main()`:** foi explicitamente exigida pelo professor. Se ausente,
  **penalize entre 5% e 10%**, mas **não zere** por isso.
- **Nomenclatura:** variáveis e funções com nomes significativos em
  português ou inglês consistente.
- **Legibilidade:** indentação correta, ausência de código morto óbvio
  (variáveis declaradas e nunca usadas, blocos inalcançáveis).
- **Sem comentários excessivos nem ausência total** — comentários pontuais
  são bem-vindos.

### REGRA DO TETO DE 70%
> Notas **acima de 70%** somente são atribuídas se o programa apresentar
> **boa completude** (resolve o problema principal sem lacunas graves) **E**
> **boa organização** (código estruturado, funções utilizadas, main presente
> ou penalizada adequadamente). Um programa que funciona parcialmente mas
> está bem organizado pode atingir 70%. Para ir além, precisa de ambos.

### TRATAMENTO DE AUSÊNCIA
- Questão não submetida: **0%** (registre como `ausente`).
- Arquivo vazio ou apenas com comentários: **0%** (registre como `em_branco`).
- Arquivo com tentativa real, mesmo que não funcione: avalie normalmente.

---

## PROCESSO DE ANÁLISE (siga esta ordem)

**Passo 1 — Mapeamento**
1. Leia `ads_normal.xls` e `ads_especial.xls`; unifique numa lista de alunos
   com matrícula e nome.
2. Liste os diretórios/arquivos em `API_01_13Abril_2026_Turma_Normal/`.
3. Associe cada submissão ao aluno correspondente. Documente associações
   incertas.

**Passo 2 — Análise por aluno**
Para cada aluno identificado:
1. Leia cada arquivo `.py` submetido.
2. Aplique a rubrica (3 dimensões) a cada questão presente.
3. Registre a nota percentual (0–100%, inteiro) por questão.
4. Se questão ausente/em branco, registre `0` e o motivo.

**Passo 3 — Cálculo da nota final**
nota_questao_pontos = percentual / 100.0        # ex: 85% → 0.85 pontos
nota_final = soma dos pontos das questões        # máximo 10.0

Use **2 casas decimais** na nota final.
Questões não submetidas valem 0 ponto.

**Passo 4 — Observações**
Para cada aluno, escreva **1 a 3 frases objetivas** que expliquem a nota,
mencionando:
- O que foi bem feito (ex: "Lógica correta em Q1–Q3, bom uso de funções").
- O que foi penalizado (ex: "Q5 usou lista para acumular cédulas —
  estrutura não vista em aula").
- Ausências ou tentativas incompletas relevantes.
Seja transparente e preciso. Evite julgamentos subjetivos sobre o aluno.

---

## SAÍDA ESPERADA

### Arquivo: `gabarito_api01_ads1_2026.csv`

Colunas (nesta ordem):

| Coluna         | Descrição                                              |
|----------------|--------------------------------------------------------|
| `matricula`    | Matrícula do aluno (da planilha oficial)               |
| `nome`         | Nome completo do aluno                                 |
| `q1_pct`       | Nota Q1 em % inteiro (0–100)                           |
| `q2_pct`       | Nota Q2 em % inteiro (0–100)                           |
| `q3_pct`       | Nota Q3 em % inteiro (0–100)                           |
| `q4_pct`       | Nota Q4 em % inteiro (0–100)                           |
| `q5_pct`       | Nota Q5 em % inteiro (0–100)                           |
| `q6_pct`       | Nota Q6 em % inteiro (0–100)                           |
| `q7_pct`       | Nota Q7 em % inteiro (0–100)                           |
| `q8_pct`       | Nota Q8 em % inteiro (0–100) ou vazio se não submetida |
| `q9_pct`       | Nota Q9 em % inteiro (0–100) ou vazio se não submetida |
| `q10_pct`      | Nota Q10 em % inteiro (0–100) ou vazio se não submetida|
| `nota_final`   | Soma ponderada, escala 0–10, 2 casas decimais          |
| `observacoes`  | Texto breve (1–3 frases), transparente e objetivo      |

**Formato CSV:** separador `,`, encoding `UTF-8 com BOM` (para abrir
corretamente no Excel/LibreOffice), aspas duplas em campos de texto.

### Arquivo adicional: `log_correcao.txt`
Registre aqui:
- Alunos da lista oficial sem submissão encontrada.
- Submissões encontradas sem correspondência clara na lista oficial.
- Qualquer decisão de interpretação que afetou uma nota.

---

## RESTRIÇÕES IMPORTANTES

- **Não execute** os arquivos `.py` dos alunos. Faça análise **estática**
  do código (leitura e interpretação manual).
- Em caso de dúvida entre duas notas, **favoreça o aluno** e registre
  a incerteza no `log_correcao.txt`.
- Mantenha consistência: se um padrão de erro é o mesmo em múltiplos
  alunos, aplique a mesma penalização a todos.
- O objetivo pedagógico é avaliar **compreensão e empenho com a linguagem**,
  não perfeição sintática. Um código com pequeno erro de sintaxe mas lógica
  claramente correta deve receber nota mais alta do que um código sintaticamente
  perfeito mas logicamente vazio.

---

## INÍCIO

Comece pelo **Passo 1** — mapeamento dos alunos e submissões.
Reporte o que encontrou antes de prosseguir para a análise.

OBSERVACAO: As pastas e arquivos podem não estar no padrao solicitado entao tente identificar cada um dos alunos.