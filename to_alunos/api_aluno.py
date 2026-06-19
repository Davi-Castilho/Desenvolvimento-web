"""
API do ALUNO (FastAPI).

Cada aluno roda esta API na porta 8000. O servidor do professor varre a rede
e detecta automaticamente quem esta com a porta 8000 aberta.

Opcionalmente, ao iniciar, o aluno pode avisar o professor o seu nome usando o
endpoint /cadastrar do servidor do professor.

Execucao basica (so a API):
    uvicorn api_aluno:app --host 0.0.0.0 --port 8000

Execucao com auto-cadastro do nome (recomendado):
    python api_aluno.py --professor 192.168.0.5 --nome "Ana Silva"
"""

import argparse
import socket
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
import requests
import uvicorn
app = FastAPI(title="API do Aluno")

class Mensagem(BaseModel):
    emissor: str      # IP de quem enviou
    destino: str      # IP de quem recebeu
    mensagem: str
    horario: datetime
# registro global, em memória
registro: list[Mensagem] = []

NOME_ALUNO = "Davi"


class EnvioMensagem(BaseModel):
    ip: str
    porta: int
    mensagem: str


class RecebimentoMensagem(BaseModel):
    emissor: str
    mensagem: str

def obter_ip_local() -> str:
    """Descobre o IP desta maquina na rede local."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def registrar(emissor: str, destino: str, texto: str):
    registro.append(
        Mensagem(
            emissor=emissor,
            destino=destino,
            mensagem=texto,
            horario=datetime.now()
        )
    )


@app.post("/receber_mensagem")
def receber_mensagem(dados: RecebimentoMensagem):
    try:
        registro.append(Mensagem(
            emissor=dados.emissor,
            destino=obter_ip_local(),
            texto=dados.mensagem,
            horario=datetime.now()))

        return {
            "status": "ok",
            "mensagem": "Mensagem recebida."
        }

    except Exception as erro:
        return {
            "status": "erro",
            "detalhes": str(erro)
        }
        

@app.post("/enviar_mensagem")
def enviar_mensagem(dados: EnvioMensagem):

    url = f"http://{dados.ip}:{dados.porta}/receber_mensagem"

    try:
        resposta = requests.post(
            url,
            json={
                "emissor": obter_ip_local(),
                "mensagem": dados.mensagem
            },
            timeout=3
        )

        if resposta.status_code == 200:

            registro.append(
                Mensagem(emissor=obter_ip_local(),destino=dados.ip,texto=dados.mensagem,horario=datetime.now())
            )

            return {
                "status": "ok",
                "mensagem": "Mensagem entregue."
            }

        return {
            "status": "erro"
        }

    except requests.RequestException:
        return {
            "status": "erro",
            "mensagem": "Destino indisponível."
        }
        

@app.get("/info_aluno")
def info_aluno():
    return {
        "nome": NOME_ALUNO,
        "ip": obter_ip_local()
    }

@app.get("/obter_conversa")
def obter_conversa():
    return registro

@app.get("/exibir_chat")
def exibir_chat(ip: str):

    conversa = []

    for msg in registro:

        if msg.emissor == ip or msg.destino == ip:
            conversa.append({
                "emissor": msg.emissor,
                "mensagem": msg.mensagem,
                "horario": msg.horario
            })

    return conversa

IP_PROFESSOR = "172.22.53.157"

@app.get("/broadcast")
def broadcast(mensagem: str):

    enviados = []
    falhas = []

    try:
        resposta = requests.get(
            f"http://{IP_PROFESSOR}:5000/dados",
            timeout=3
        )

        alunos = resposta.json()

    except Exception:
        return {
            "erro": "Nao foi possivel acessar o servidor do professor."
        }

    meu_ip = obter_ip_local()

    for aluno in alunos:

        ip = aluno.get("ip")

        if not ip or ip == meu_ip:
            continue

        try:
            requests.post(
                f"http://{ip}:8000/receber_mensagem",
                json={
                    "emissor": meu_ip,
                    "mensagem": mensagem
                },
                timeout=3
            )

            registrar(
                emissor=meu_ip,
                destino=ip,
                texto=mensagem
            )

            enviados.append(ip)

        except Exception:
            falhas.append(ip)

    return {
        "enviados": enviados,
        "falhas": falhas
    }

@app.get("/")
def raiz():
    return {"mensagem": "API do aluno no ar!", "ip": obter_ip_local()}


@app.get("/ola/{nome}")
def ola(nome: str):
    return {"mensagem": f"Ola, {nome}!"}


def cadastrar_no_professor(ip_professor: str, nome: str):
    """Avisa o servidor do professor o nome associado a este IP."""
    import urllib.parse
    import urllib.request

    meu_ip = obter_ip_local()
    parametros = urllib.parse.urlencode({"ip": meu_ip, "nome": nome})
    url = f"http://{ip_professor}:5000/cadastrar?{parametros}"
    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            print(f"Cadastrado no professor: {resposta.read().decode()}")
    except Exception as erro:
        print(f"Nao foi possivel cadastrar no professor: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API do aluno (FastAPI).")
    parser.add_argument("--professor", help="IP do servidor do professor")
    parser.add_argument("--nome", help="Seu nome para cadastrar no professor")
    parser.add_argument("--porta", type=int, default=8000, help="Porta da API (padrao 8000)")
    args = parser.parse_args()

    if args.professor and args.nome:
        cadastrar_no_professor(args.professor, args.nome)

    print(f"Iniciando API do aluno em http://{obter_ip_local()}:{args.porta}")
    uvicorn.run(app, host="0.0.0.0", port=args.porta)