# Roteiro Prático 2.0: do Estudo à Autoria com o Antigravity

**Autor:** Juan Diego Angélico  
**Área:** Metodologia de IA Aplicada à Advocacia & Produção de Conteúdo Jurídico Autoral

---

## 1. Visão Geral

Este roteiro estabelece um padrão rigoroso para transformar estudos, cursos e referências técnicas em material próprio, com você como autor legítimo perante a Lei de Direitos Autorais (Lei nº 9.610/98).

O trabalho ocorre em **duas fases que jamais se misturam**:
1. **Fase 1, Estudo (Privada):** O agente de IA lê materiais de terceiros e gera notas conceituais estritamente para seu uso pessoal de aprendizado, com a fonte de cada ideia mapeada. Nada daqui é publicado.
2. **Sua Contribuição (Filtro Humano):** Você aplica os métodos em casos reais, registra resultados, dados, divergências e sua própria voz.
3. **Fase 2, Autoria (Pública):** Em um projeto fisicamente isolado no computador, sem acesso aos arquivos originais dos cursos, o agente atua como editor organizando exclusivamente as suas notas, testes e casos.

---

## 2. Princípio Jurídico de Autoria (Lei nº 9.610/98)

Ideias, sistemas e métodos são livres (art. 8º da Lei nº 9.610/98). No entanto, a forma como outro autor expressou essas ideias é protegida (art. 29). Paráfrase gerada por IA sobre obra alheia continua configurando obra derivada/adaptação não autorizada.

| Pode Usar Livremente | Não Pode Usar sem Autorização |
| :--- | :--- |
| Conceitos jurídicos, artigos do CPP, teses consolidadas | Textos literais ou roteiros de aulas do curso original |
| Sua própria sequência didática e curricular | A mesma estrutura de módulos e aulas do autor |
| Exemplos e casos reais da sua própria advocacia | Exemplos fictícios ou casos próprios do professor |
| Prompts e templates desenvolvidos e validados por você | Prompts e tabelas copiados do material do curso |
| Ideias de várias fontes cruzadas e devidamente citadas | Frameworks com nome próprio comercial do autor sem citação |

---

## 3. Arquitetura de Pastas e Isolamento Físico

A separação física em diretórios independentes impede vazamento acidental de dados (*data leakage*):

```text
/Estudos/CursoCriminal/              ← Fase 1 (Privada)
   ├── fontes/                       # Arquivos originais do curso (.pdf, .docx, .mp4)
   ├── transcricoes/                 # Transcrições em texto (.txt, .srt)
   └── saida/                        # anotacoes_estudo.md e relatorio.md

/Autoria/AdvocaciaCriminal/          ← Fase 2 (Pública / Repositório Git)
   ├── notas/                        # Suas notas reescritas com suas palavras
   ├── experimentos/                 # Casos práticos, peças, números e decisões
   ├── estilo/                       # Textos que expressam sua voz e tom profissional
   └── produto/                      # Onde o agente compõe os guias finais
```

---

## 4. O Prompt de Estudo (/goal Fase 1)

```text
/goal
Leia recursivamente os arquivos de /fontes e /transcricoes (.pdf, .txt, .md, .srt).
Liste no relatório qualquer arquivo de vídeo/áudio sem transcrição e qualquer arquivo que não conseguiu ler.

Crie /saida/anotacoes_estudo.md para MEU USO PESSOAL DE ESTUDO:
- Organize os conceitos em ordem de aprendizado.
- Para cada conceito: o que é, por que importa, como se aplica.
- Indique a origem de cada item no formato [arquivo, aula].
- Separe o que é princípio geral (ideia/método) do que é material específico do autor (exemplos, cases, frameworks com nome próprio, prompts prontos).
- Ao final de cada módulo, liste "Dúvidas para testar na prática".

Crie também /saida/relatorio.md com: arquivos lidos, arquivos ignorados e o motivo, e trechos ambíguos que precisam de revisão.
```

---

## 5. O Prompt de Autoria (/goal Fase 2)

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
