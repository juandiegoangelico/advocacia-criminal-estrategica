# Guia Prático: Cadeia de Custódia da Prova Digital e Extração de Celulares

**Autor:** Juan Diego Angélico (Angélico Anziutti Advocacia)  
**Base Legal:** Arts. 158-A a 158-F do Código de Processo Penal (Lei nº 13.964/2019 - Pacote Anticrime)  
**Precedentes:** STJ - RHC nº 131.603/MG, HC nº 515.707/SP, HC nº 618.621/SC

---

## 1. O Conceito Jurídico de Cadeia de Custódia Digital

A cadeia de custódia da prova digital é o procedimento formal, técnico e cronológico que documenta a história do vestígio eletrônico desde sua apreensão até o descarte definitivo.

Diferente de um objeto físico imutável, o dado digital é volátil, intangível e facilmente suscetível a adulteração, exclusão inadvertida ou injeção de metadados adulterados sem deixar marcas visíveis ao olho leigo.

---

## 2. Os 10 Elos Obrigatórios da Cadeia de Custódia (Art. 158-B do CPP)

```mermaid
flowchart LR
    A[1. Reconhecimento] --> B[2. Isolamento]
    B --> C[3. Fixação]
    C --> D[4. Coleta]
    D --> E[5. Acondicionamento]
    E --> F[6. Transporte]
    F --> G[7. Recebimento]
    G --> H[8. Processamento]
    H --> I[9. Armazenamento]
    I --> J[10. Descarte]
```

### Onde ocorrem 90% das nulidades policiais:
1. **Acondicionamento Inadequado (Sem Lacre Numerado):** O celular apreendido deve ser imediatamente embalado em envelope de evidência ou saco de Faraday (que bloqueia sinais de rádio, Wi-Fi e dados celulares), lacrado e com numeração expressa no auto de apreensão.
2. **Manipulação Prévia por Policiais sem Autorização Judicial:** Policiais que navegam pelo WhatsApp ou galeria de fotos do preso na viatura ou delegacia violam a integridade e geram a nulidade insanável da prova (STJ, Sexta Turma, HC 515.707/SP).
3. **Ausência de Cálculo de Hash Criptográfico (SHA-256):** No momento da extração dos dados (via software forense como Cellebrite UFED), o perito é obrigado a gerar o valor de hash do arquivo bruto (*raw image*). Qualquer divergência entre o hash da extração e o hash disponibilizado à defesa indica que o dado foi corrompido.

---

## 3. Tese Defensiva: Quebra de Custódia e Iadmissibilidade Probatória

A quebra da cadeia de custódia não é mera irregularidade formal. Ela fulmina a confiabilidade epistêmica da prova:

* **Inversão do Ônus Probatório:** Cabe ao Estado-Acusador comprovar a higidez e a rastreabilidade integral da evidência digital.
* **Inadmissibilidade da Prova (Art. 157, CPP):** Não comprovada a preservação do vestígio, o laudo pericial é imprestável e deve ser desentranhado dos autos.
* **Teoria dos Frutos da Árvore Envenenada (Art. 157, § 1º, CPP):** Todas as diligências, quebras de sigilo bancário ou prisões preventivas fundamentadas nos dados extraídos ilegalmente são contaminadas e nulas.
