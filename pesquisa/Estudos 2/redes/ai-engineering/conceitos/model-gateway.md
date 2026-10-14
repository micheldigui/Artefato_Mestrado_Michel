# 🧠 Gateway de Modelos (*Model Gateway*)

**Rede:** `ai-engineering`  
areas: `arquitetura-de-sistemas`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 10 — Arquitetura de Engenharia de IA e Feedback do Usuário
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Uma camada de software intermediária centralizada que unifica o acesso a múltiplos provedores de modelos de fundação (APIs comerciais e modelos auto-hospedados), fornecendo uma interface padronizada de requisições, controle de acesso, políticas de fallback, monitoramento de custos e roteamento de tráfego.

### Em linguagem simples

É um "portal único" ou central de controle na sua empresa para conversar com qualquer IA: se a OpenAI cair, o portal desvia o tráfego automaticamente para o Claude ou para um modelo local sem que o seu código precise ser reescrito.

### Escopo e distinções

Diferencia-se de uma chamada de API direta: atua como proxy corporativo de infraestrutura para governança, segurança e resiliência de chamadas a modelos gerativos.

## 🧩 Problema que resolve

Resolve o acoplamento rígido entre o código da aplicação e provedores específicos de API de IA, mitigando riscos de interrupções de serviço, explosão de custos e vazamento de credenciais.

## 💡 Intuição

Pense em um adaptador universal de tomadas ou em um roteador de internet corporativo: não importa se o provedor de energia muda, os aparelhos dentro de casa continuam plugados na mesma tomada padronizada.

## ⚙️ Como funciona

### Etapas

1. A aplicação envia uma requisição padronizada para o *Model Gateway* local em vez de chamar diretamente um provedor externo.
2. O gateway valida as permissões do usuário, aplica políticas de controle de orçamento e verifica regras de mascaramento de dados sensíveis (*PII*).
3. O gateway despacha a chamada para o modelo primário configurado.
4. Se o modelo primário falhar ou atingir o limite de taxa (*rate limit*), o gateway executa automaticamente a política de *fallback* roteando para um modelo secundário.

### Entradas e saídas

- Entradas: Requisições de inferência padronizadas vindas da camada de aplicação.
- Saídas: Respostas consolidadas dos modelos com metadados de rastreamento de custos e latência.

## 📐 Formulação matemática

Não possui formulação matemática própria (trata-se de um componente de arquitetura de rede e proxy de microsserviços).

## 🧱 Hipóteses e condições de validade

- Supõe que os modelos alternativos conectados ao gateway aceitam estruturas de dados compatíveis ou que o gateway realiza a tradução de esquema (*schema translation*) corretamente.

## ✅ Quando usar

- Em ambientes corporativos de médio a grande porte que utilizam múltiplos provedores de IA e exigem governança centralizada, auditoria e resiliência contra quedas de API.

## 🚫 Quando não usar

- Em protótipos acadêmicos ou aplicativos de usuário único extremamente simples onde chamadas diretas a uma única API reduzem a complexidade de setup.

## ⚠️ Limitações e armadilhas

- O gateway pode se tornar um ponto único de falha (*Single Point of Failure*) ou um gargalo de latência adicional se não for dimensionado com alta disponibilidade.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[model-gateway|Gateway de Modelos]] | Centralizar, padronizar e proteger o acesso a múltiplos modelos de IA. | Requisições padronizadas de IA. | Respostas encaminhadas com governança. | Atua como proxy corporativo unificado para resiliência e controle de custos. |
| [[chamada-de-api-direta|Chamada de API Direta]] | Conectar o código diretamente ao endpoint de um único provedor. | Código da aplicação + Chave de API direta. | Resposta isolada do provedor. | Acoplamento rígido, sem redundância de *fallback* e difícil governança centralizada. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um sistema de RH envia uma requisição para `gateway.empresa.com/model`, e o gateway decide se a requisição vai para o modelo GPT-4o na nuvem ou para um modelo Llama 3 rodando em um servidor local da empresa, sem que o desenvolvedor mude nenhuma linha de código.

## 🔗 Relações no grafo

### Pré-requisitos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 10 — Arquitetura de Engenharia de IA e Feedback do Usuário
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação conceitual do Gateway de Modelos como componente de infraestrutura para padronização, fallback e governança de APIs de IA.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Gateway de Modelos (Model Gateway)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 10 — Arquitetura de Engenharia de IA e Feedback do Usuário. A interpretação final deve ser revisada pelo estudante.*
