# Configuração do Antigravity para Tarefas Longas e Autoria

Guia prático para garantir estabilidade e continuidade na execução de workflows longos (/goal) no Antigravity 2.0.

---

## 1. Ajustes em Settings > Application

| Configuração | Valor Recomendado | Finalidade | Cuidados |
| :--- | :---: | :--- | :--- |
| **Prevent Sleep** | **ON** | Impede o sistema de entrar em repouso no meio da tarefa | Manter o notebook conectado à tomada |
| **Keep In Menu Bar** | **ON** | Garante que o processo continue rodando ao fechar a janela | Monitorar consumo de recursos e cotas |
| **Enable Remote Control** | **ON (quando necessário)** | Acompanhamento do progresso pelo smartphone via QR Code | Desconectar após a finalização da rotina |

---

## 2. Dicas para Evitar Interrupções no /goal

* **Aprovação de Terminal:** Evite comandos interativos ou que exijam inputs manuais. Mantenha os arquivos organizados previamente em texto (.md/.txt).
* **Gestão de Cotas:** Para diretórios grandes com dezenas de arquivos, parcele os processamentos em módulos para evitar atingir o teto temporário de chamadas de modelo.
