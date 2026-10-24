# Biblioteca de Prompts - Fase 1: Estudo e Rastreabilidade

Estes prompts foram desenvolvidos para a **Fase 1 (Privada)** do método Antigravity 2.0, garantindo rigor na leitura de fontes e isolamento conceitual.

---

## 1. Prompt Geral de Estudo (/goal)

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

## 2. Prompt de Extração de Teses Jurisprudenciais

```text
A partir dos textos de /transcricoes, identifique todos os artigos de lei (CPP, CP, Leis Especiais), Súmulas Vinculantes e precedentes do STJ/STF citados pelo autor.

Para cada citação:
1. Artigo ou Precedente
2. Tese jurídica sustentada
3. Se o entendimento continua atual ou foi superado por jurisprudência recente
4. [arquivo, aula] de origem
```
