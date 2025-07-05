from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv
import fitz  # PyMuPDF

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def criar_prompt(texto: str) -> str:
    return f"""
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

@app.post("/processar")
async def processar(email: str = Form(None), file: UploadFile = File(None)):
    texto = ""

    # Se tiver texto
    if email:
        texto += email.strip()

    # Se tiver arquivo
    if file:
        if not file.filename.lower().endswith((".pdf", ".txt")):
            raise HTTPException(status_code=400, detail="Apenas arquivos PDF ou TXT são aceitos.")
        try:
            if file.filename.lower().endswith(".pdf"):
                contents = await file.read()
                doc = fitz.open(stream=contents, filetype="pdf")
                for pagina in doc:
                    texto += "\n" + pagina.get_text()
            else:  # TXT
                texto += "\n" + (await file.read()).decode("utf-8")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao ler o arquivo: {str(e)}")

    # Validação final
    if not texto.strip():
        return {"categoria": "Erro", "resposta": "Nenhum conteúdo foi enviado."}

    prompt = criar_prompt(texto.strip())

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

        return {"categoria": categoria, "resposta": resposta_gerada}

    except Exception as e:
        return {"categoria": "Erro", "resposta": f"Erro ao gerar resposta: {str(e)}"}
