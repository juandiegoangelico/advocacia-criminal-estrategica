# Framework de Pesquisa, Validação e Autoria Jurídica com IA

**Autor:** Juan Diego Angélico (Angélico Anziutti Advocacia)  
**Finalidade:** Metodologia de Engenharia de Conhecimento e Produção Técnica Autoral com Antigravity

---

## 1. Visão Geral

Este framework estabelece uma metodologia estruturada para transformar pesquisas doutrinárias, julgados dos tribunais e análises técnicas em **conteúdo jurídico autoral de alto valor**, preservando o rigor técnico e a originalidade da voz do advogado.

O fluxo é dividido em **duas fases com isolamento estrutural**:
1. **Fase 1 (Pesquisa & Consolidação Conceitual):** O agente de IA processa o acervo legislativo, precedentes e documentos brutos em uma pasta privada, organizando conceitos e teses.
2. **Validação Prática Forense:** O advogado aplica e valida as teses no contexto real de sua advocacia (varas e tribunais), registrando casos concretos, impressões práticas e estratégias próprias.
3. **Fase 2 (Autoria & Redação de Produtos):** Em um ambiente isolado, sem os arquivos brutos da pesquisa inicial, o agente atua como editor organizando os manuais, checklists e petições a partir exclusivamente das anotações e da casuística do autor.

---

## 2. Princípios de Originalidade e Rigor Técnico

A produção intelectual jurídica diferenciada exige que a prática do advogado seja o elemento central da obra:

| Elemento | Abordagem Autoral |
| :--- | :--- |
| **Doutrina e Jurisprudência** | Extração dos conceitos abstratos e aplicação aos julgados vinculantes atuais (STF e STJ) |
| **Sequência Didática** | Fluxo cronológico concebido a partir da rotina da trincheira penal |
| **Casuística** | Casos reais e hipotéticos estruturados pela vivência forense do advogado |
| **Prompts e Peças** | Modelos e comandos testados e validados na prática forense diária |

---

## 3. Arquitetura de Pastas e Separação de Ambientes

```text
/Pesquisa/ProjetoPenal/               ← Fase 1 (Pesquisa Privada)
   ├── fontes/                       # Jurisprudência, legislação e acervo bruto
   ├── transcricoes/                 # Transcrições e degravações de atos processuais
   └── saida/                        # Anotações conceituais de trabalho

/Autoria/AdvocaciaCriminal/          ← Fase 2 (Repositório Público / Produtos)
   ├── notas/                        # Conceitos e teses consolidadas pelo autor
   ├── experimentos/                 # Casos práticos, peças e resultados
   ├── estilo/                       # Diretrizes de tom e voz do autor
   └── produto/                      # Guias, modelos e apostilas finais
```

---

## 4. O Prompt de Estruturação Conceitual (Fase 1)

```text
/goal
Leia os documentos de /fontes e /transcricoes.
Crie /saida/anotacoes_estudo.md para USO TÉCNICO INTERNO:
- Organize os conceitos em ordem lógica de atuação forense.
- Para cada conceito: o que é, por que importa e como se aplica no processo penal.
- Destaque divergências jurisprudenciais entre STJ e Tribunais Estaduais.
- Ao final de cada tópico, liste "Questões Práticas para Validação Forense".
```

---

## 5. O Prompt de Redação Autoral (Fase 2)

```text
/goal
Usando APENAS os arquivos de /notas, /experimentos e /estilo, monte em /produto/guia.md um manual prático sobre [TEMA].

Regras:
- Siga a sequência didática definida em /notas/sequencia.md.
- Escreva com a voz dos textos em /estilo (assertiva, combativa e técnica).
- Use como exemplos somente os casos de /experimentos.
- Inclua "Erros Comuns e Como Evitar" ao final de cada capítulo.
- Se faltar dados locais específicos da comarca, use o marcador [PREENCHER].
```
