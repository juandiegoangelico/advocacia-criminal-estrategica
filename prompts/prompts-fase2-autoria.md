# Biblioteca de Prompts - Fase 2: Autoria Original

Estes prompts operam na **Fase 2 (Pública)**, onde o agente de IA atua estritamente como editor dos seus dados, notas e casos reais.

---

## 1. Prompt Geral de Montagem de Guia Autoral (/goal)

```text
/goal
Usando APENAS os arquivos de /notas, /experimentos e /estilo, monte em /produto/guia.md um material original sobre [TEMA], para [PÚBLICO-ALVO].

Regras:
- Siga a sequência didática definida em /notas/sequencia.md.
- Escreva com a voz dos textos em /estilo (tom, vocabulário, ritmo).
- Use como exemplos somente os casos reais de /experimentos.
- Foque no passo a passo prático, mantendo o "porquê" de cada etapa.
- Inclua "Erros Comuns e Como Evitar" ao final de cada aula, baseado nos erros registrados em /experimentos.
- Quando uma ideia tiver autor conhecido indicado nas notas, cite a fonte no texto.
- Não acrescente fatos, números ou exemplos que não estejam nos arquivos. Se faltar algo, marque [PREENCHER] e liste no final.
- Ao terminar, crie /produto/revisao.md com as lacunas encontradas.
```

---

## 2. Prompt para Geração de Checklists Operacionais

```text
Com base no arquivo /notas/[tema].md e nos casos relatados em /experimentos/, construa um checklist operacional passo a passo para advogados que precisam executar [ato processual].

Regras:
1. Organize em 3 fases: Antes do Ato, Durante o Ato, Após o Ato.
2. Cada item deve começar com um verbo de ação.
3. Se houver divergência prática encontrada nos experimentos, inclua como 'Alerta Prático'.
4. Havendo lacuna sobre detalhes locais do tribunal, use a tag [PREENCHER].
```
