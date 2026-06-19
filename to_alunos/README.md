# Serviço de Mensagem — Painel da Turma

Projeto didático para a aula de FastAPI. O professor roda um servidor Flask que
varre a rede local procurando as APIs FastAPI dos alunos (porta 8000) e exibe,
em uma página HTML, quem está pronto para receber conexões.

## Instalação

```bash
pip install -r requirements.txt
```

## 1. Script do professor — `servidor_professor.py`

```bash
python servidor_professor.py
```

- Abre a página em `http://<ip-do-professor>:5000`
- A cada 10 segundos varre a sub-rede local (`/24`) procurando a porta **8000** aberta.
- Cada IP detectado aparece na página (atualizada automaticamente a cada 5 s).

### Endpoint de cadastro

```
GET /cadastrar?ip=<ip-do-aluno>&nome=<nome-do-aluno>
```

Exemplo (no navegador ou via `curl`):

```
http://192.168.0.5:5000/cadastrar?ip=192.168.0.10&nome=Ana
```

Quando há um nome associado a um IP, o par **nome + IP** é exibido na página.

### Endpoint auxiliar

- `GET /dados` — estado atual em JSON (útil para depuração).

## 2. Script do aluno — `api_aluno.py`

API FastAPI simples que roda na porta 8000.

Execução básica (será detectado apenas pelo IP):

```bash
python api_aluno.py
```

Execução com auto-cadastro do nome no servidor do professor:

```bash
python api_aluno.py --professor 192.168.0.5 --nome "Ana Silva"
```

Endpoints da API do aluno:

- `GET /` — confirma que a API está no ar e mostra o IP local.
- `GET /ola/{nome}` — exemplo de rota com parâmetro de caminho.
- `GET /docs` — documentação automática do FastAPI (Swagger UI).

## Observações

- Todos devem estar na **mesma rede local** (mesma sub-rede `/24`).
- O firewall do Windows pode bloquear a porta 8000; se o aluno não aparecer no
  painel, libere a porta ou desative temporariamente o firewall na rede da aula.
