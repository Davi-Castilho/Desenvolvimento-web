# Atividade — Serviço de Mensagens com FastAPI

## Contexto

Nesta atividade, cada aluno vai transformar sua API FastAPI (rodando na porta
**8000**) em um pequeno serviço de mensagens. Como todos os computadores da
turma estão na mesma rede local, as APIs poderão conversar entre si: a sua API
será ao mesmo tempo um **servidor** (recebe mensagens dos colegas) e um
**cliente** (envia mensagens para as APIs dos colegas).

O painel do professor (`http://<ip-do-professor>:5000`) mostra os IPs de todos
os alunos com a API no ar — use-o para descobrir com quem você pode conversar.

## Objetivos de aprendizagem

- Criar endpoints `GET` e `POST` com FastAPI.
- Receber dados via corpo da requisição (JSON) e via parâmetros de consulta.
- Consumir uma API a partir de outra (sua API agindo como cliente HTTP).
- Trabalhar com códigos de status HTTP (`200`, `404`, `500`).
- Manter estado em memória (registro de mensagens).

## Requisito geral: registro de mensagens

Como não usaremos banco de dados, as mensagens serão armazenadas
**temporariamente em memória**. Para isso, sua API deve obrigatoriamente
definir:

1. A classe **`Mensagem`** (modelo Pydantic), que representa cada mensagem;
2. A lista global **`registro`**, onde todas as mensagens (enviadas e
   recebidas) são guardadas.

Use exatamente esta estrutura como ponto de partida:

```python
from datetime import datetime
from pydantic import BaseModel

class Mensagem(BaseModel):
    emissor: str      # IP de quem enviou a mensagem
    destino: str      # IP de quem recebeu a mensagem
    mensagem: str     # texto da mensagem
    horario: datetime # momento em que foi enviada/recebida

# registro temporário, em memória (substitui o banco de dados)
registro: list[Mensagem] = []
```

Sempre que uma mensagem for **enviada** (`enviar_mensagem` / `broadcast`) ou
**recebida** (`receber_mensagem`), crie um objeto `Mensagem` e acrescente-o ao
`registro` com `registro.append(...)`, **no momento em que o evento ocorre**.

**Atenção à ordem das mensagens:** enviadas e recebidas ficam juntas na mesma
lista `registro`, na **sequência em que ocorreram** — é o `append` na hora
certa que garante a ordem. É essa sequência que permite ao `exibir_chat`
reconstruir a conversa corretamente, como em um aplicativo de chat. Se você
guardar enviadas e recebidas em listas separadas, ou sem horário, não
conseguirá exibir a troca de mensagens na ordem certa.

> Dica: centralize o armazenamento em uma única função auxiliar (ex.:
> `registrar(emissor, destino, texto)`) e chame-a tanto no envio quanto no
> recebimento.

Lembre-se: por ser um armazenamento em memória, o `registro` é **volátil** —
ao reiniciar a API, o histórico é perdido. Isso é esperado nesta atividade.

Esse registro é a base do endpoint `exibir_chat`.

## Endpoints obrigatórios

### 1. `POST /enviar_mensagem`

Envia uma mensagem para a API de outro aluno.

- **Recebe** (corpo JSON): um endereço **IP**, uma **porta** e a **mensagem**.

```json
{
  "ip": "192.168.0.10",
  "porta": 8000,
  "mensagem": "Olá, colega!"
}
```

- **Comportamento**: sua API deve fazer uma requisição `POST` para o endpoint
  `/receber_mensagem` da máquina de destino, identificando-se como emissor.
  A mensagem enviada também deve ser guardada na lista `registro` (como um
  objeto `Mensagem`).
- **Responde**:
  - `200` — mensagem entregue com sucesso;
  - `404` — falha na entrega (máquina não encontrada, porta fechada, timeout).

### 2. `POST /receber_mensagem`

Recebe uma mensagem enviada por outro aluno.

- **Recebe** (corpo JSON): a **mensagem** e a identificação do **emissor**.

```json
{
  "emissor": "192.168.0.10",
  "mensagem": "Olá, colega!"
}
```

- **Comportamento**: criar um objeto `Mensagem` identificando o emissor e
  acrescentá-lo à lista `registro`.
- **Responde**:
  - `200` — mensagem recebida e registrada;
  - `500` — erro ao processar/registrar a mensagem.

### 3. `GET /broadcast`

Envia uma mensagem para **todos** os computadores da rede.

- **Recebe** (parâmetro de consulta): a **mensagem**.

```
GET /broadcast?mensagem=Bom%20dia,%20turma!
```

- **Comportamento**: descobrir os IPs ativos da turma (dica: o painel do
  professor expõe `GET /dados` com a lista de IPs detectados) e enviar a
  mensagem a cada um deles reutilizando a lógica do `enviar_mensagem`.
- **Responde**: `200` com um resumo do envio, por exemplo:

```json
{
  "enviados": ["192.168.0.10", "192.168.0.12"],
  "falhas": ["192.168.0.15"]
}
```

### 4. `GET /info_aluno`

Retorna as informações de identificação do dono da API.

- **Recebe**: nada.
- **Responde**: `200` com o **nome** e o **IP** do aluno.

```json
{
  "nome": "Ana Silva",
  "ip": "192.168.0.10"
}
```

> Dica: os colegas podem usar este endpoint para descobrir quem é o dono de um
> IP que aparece no painel do professor.

### 5. `GET /obter_conversa`

Retorna **todas as mensagens enviadas e recebidas** pelo aluno, ou seja, o
histórico completo do `registro`.

- **Recebe**: nada.

```
GET /obter_conversa
```

- **Comportamento**: retornar o conteúdo completo da lista `registro`
  (mensagens enviadas e recebidas, com qualquer colega), em ordem cronológica,
  identificando o emissor e o destino de cada uma.
- **Responde**: `200` com a lista completa de mensagens, por exemplo:

```json
[
  { "emissor": "192.168.0.10", "destino": "192.168.0.22", "mensagem": "Oi!",      "horario": "14:02:11" },
  { "emissor": "192.168.0.22", "destino": "192.168.0.10", "mensagem": "Oi!",      "horario": "14:02:45" },
  { "emissor": "192.168.0.15", "destino": "192.168.0.22", "mensagem": "Bom dia!", "horario": "14:05:30" }
]
```

> Repare na diferença: o `obter_conversa` devolve o **histórico completo**
> (todas as mensagens, com todos os colegas), enquanto o `exibir_chat` devolve
> apenas a conversa com **um IP específico**.

### 6. `GET /exibir_chat`

Exibe a conversa completa com um determinado aluno.

- **Recebe** (parâmetro de consulta): o **IP** de um aluno.

```
GET /exibir_chat?ip=192.168.0.10
```

- **Comportamento**: filtrar a lista `registro` e retornar **todas as
  mensagens trocadas** com aquele IP (enviadas e recebidas, ou seja, em que o
  IP aparece como `emissor` ou como `destino`), **na exata ordem em que a
  troca aconteceu** (ordem cronológica), identificando o emissor de cada uma.
  A saída deve reproduzir a conversa como em um aplicativo de chat: pergunta e
  resposta intercaladas, e não as enviadas separadas das recebidas.
- **Responde**: `200` com a lista de mensagens, por exemplo:

```json
[
  { "emissor": "192.168.0.10", "mensagem": "Oi!",          "horario": "14:02:11" },
  { "emissor": "192.168.0.22", "mensagem": "Oi, tudo bem?", "horario": "14:02:45" }
]
```

## Desafio bônus — troca de imagens

Implemente dois endpoints adicionais:

1. **`POST /receber_imagem`** — recebe um arquivo de imagem (upload) e o salva
   em disco, registrando quem foi o emissor.
2. **`POST /enviar_imagem`** — recebe o IP de destino e um arquivo de imagem,
   e envia a imagem para o endpoint `/receber_imagem` do colega.

> Dicas: pesquise sobre `UploadFile` e `File` no FastAPI para o recebimento, e
> sobre envio de arquivos `multipart/form-data` com a biblioteca `requests`
> (parâmetro `files=`). Lembre-se de instalar `python-multipart`.

## Dicas gerais

- Use a biblioteca **`requests`** (ou `httpx`) para que sua API faça chamadas
  às APIs dos colegas. Sempre defina um **timeout** (ex.: 3 segundos) para não
  travar quando o destino estiver fora do ar.
- Para retornar códigos de erro no FastAPI, use
  `raise HTTPException(status_code=404, detail="...")`.
- Use **Pydantic** (`BaseModel`) para definir o corpo das requisições `POST`.
- Teste seus endpoints pela documentação automática em
  `http://localhost:8000/docs` antes de testar com os colegas.
- **Teste consigo mesmo primeiro**: envie uma mensagem para o seu próprio IP —
  sua API deve receber e registrar normalmente.

## Roteiro sugerido

1. Suba a API base (`api_aluno.py`) e confirme que você aparece no painel do
   professor com seu nome.
2. Crie a classe `Mensagem` e a lista `registro`.
3. Implemente `receber_mensagem` guardando as mensagens no `registro`.
4. Implemente `enviar_mensagem` e teste enviando para si mesmo.
5. Implemente `info_aluno` e `obter_conversa`.
6. Implemente `exibir_chat`.
7. Troque mensagens com pelo menos **dois colegas** e mostre o
   `obter_conversa` e o `exibir_chat`.
8. Implemente o `broadcast` e mande um "bom dia" para a turma inteira.
9. (Bônus) Implemente a troca de imagens.

## Critérios de avaliação

| Item                                                        | Pontos |
|-------------------------------------------------------------|:------:|
| `POST /enviar_mensagem` com tratamento de erro (200/404)    |  2,0   |
| `POST /receber_mensagem` com registro do emissor (200/500)  |  2,0   |
| `GET /broadcast` para todos os IPs ativos                   |  1,5   |
| `GET /info_aluno`                                           |  0,5   |
| `GET /obter_conversa` com todas as enviadas e recebidas     |  1,0   |
| `GET /exibir_chat` filtrando por IP e na sequência correta  |  2,0   |
| Uso da classe `Mensagem` e da lista `registro` (ordem ok)   |  1,0   |
| **Bônus:** envio e recebimento de imagens                   | +1,0   |
