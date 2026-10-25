# Estudo de Caso Forense: Quebra de Cadeia de Custódia em Conversas de WhatsApp

**Relator do Estudo:** Juan Diego Angélico (Angélico Anziutti Advocacia)  
**Precedente Vinculante:** STJ - RHC nº 131.603/MG e HC nº 515.707/SP

---

## 1. O Caso Concreto Didático
Em cumprimento a mandado de busca e apreensão, a polícia apreendeu dois smartphones pertencentes a um empresário investigado por suposto crime tributário e associação criminosa.

No relatório policial final anexado aos autos, constavam apenas **capturas de tela (prints) impressas e coladas** no corpo do documento, nas quais supostamente o investigado combinava transações ilícitas.

Ao analisar o inquérito, a defesa técnica constatou três graves irregularidades:
1. O celular não foi acondicionado em embalagem lacrada com número de controle no momento da apreensão.
2. A polícia não realizou a cópia forense integral (*raw image bit-a-bit*) com cálculo do algoritmo Hash SHA-256.
3. Não foi disponibilizada à defesa a base de dados bruta do aplicativo WhatsApp (`msgstore.db`), impossibilitando a perícia defensiva.

---

## 2. A Tese da Defesa Técnica

A defesa impetrou **Habeas Corpus perante o Tribunal de Justiça**, sustentando:
* **Inviabilidade do Print Screen como Prova Pericial Idônea:** Conforme fixado pela Sexta Turma do STJ no RHC 131.603/MG, meros prints de conversas de WhatsApp são desprovidos de força probatória autônoma por sua extrema vulnerabilidade a edições e exclusões seletivas.
* **Violação Frontal aos Arts. 158-A a 158-F do CPP:** A omissão do laudo com cálculo de hash e a falta de lacre caracterizam quebra insanável da cadeia de custódia.
* **Cerceamento de Defesa:** A recusa em fornecer o espelhamento integral impede o exercício da ampla defesa técnica e a produção de contraprova por assistente técnico.

---

## 3. Resultado Forense
A Câmara Criminal concedeu a ordem de Habeas Corpus por unanimidade para:
1. Declarar a **nulidade da prova digital obtida e de todos os relatórios policiais dela derivados**;
2. Determinar o **desentranhamento imediato** de todos os prints e laudos viciados;
3. Determinar o trancamento da ação penal quanto às imputações dependentes exclusivamente da referida prova.
