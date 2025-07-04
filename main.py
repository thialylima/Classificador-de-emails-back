from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI com a chave da API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Permitir chamadas do frontend (CORS liberado para testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Troque por seu domínio na produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados esperado
class EmailEntrada(BaseModel):
    email: str

@app.post("/processar-email")
async def processar_email(dados: EmailEntrada):
    texto = dados.email.strip()

    if not texto:
        return {
            "categoria": "Erro",
            "resposta": "Texto do e-mail está vazio."
        }

    # Prompt enviado para o modelo
    prompt = f"""
Você é um assistente inteligente de uma empresa do setor financeiro. Sua tarefa é analisar o e-mail abaixo e fazer duas coisas:

1. Classificar o e-mail em uma das duas categorias:

- Produtivo: Emails que requerem uma ação ou resposta específica, como solicitações de suporte técnico, pedidos de atualização sobre casos em andamento, dúvidas sobre o sistema, entre outros assuntos que precisam de retorno.
- Improdutivo: Emails que não necessitam de uma ação imediata, como mensagens de felicitações, agradecimentos, votos de boas festas ou perguntas não relevantes.

2. Gerar uma resposta automática apropriada ao conteúdo do e-mail e à categoria atribuída. Se a categoria for Improdutivo, a resposta pode ser simples e cordial. As respostas devem ser em formato de e-mail formal, escrito por Thialy Lima.

Formato da resposta (sem texto adicional):

Categoria: <Produtivo ou Improdutivo>
Resposta: <Resposta automática adequada em formato de e-mail>

E-mail para análise:
\"\"\"
{texto}
\"\"\"
"""

    try:
        resposta = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5,
        )

        conteudo = resposta.choices[0].message.content.strip()

        categoria = "Desconhecida"
        resposta_gerada = ""

        if "Categoria:" in conteudo and "Resposta:" in conteudo:
            partes = conteudo.split("Resposta:")
            categoria = partes[0].replace("Categoria:", "").strip()
            resposta_gerada = partes[1].strip()

        return {
            "categoria": categoria,
            "resposta": resposta_gerada
        }

    except Exception as e:
        return {
            "categoria": "Erro",
            "resposta": f"Erro ao gerar resposta: {str(e)}"
        }
