
# 📬 Classificador de E-mails - Backend (FastAPI + OpenAI)

Este projeto é um backend desenvolvido com **FastAPI** que utiliza **inteligência artificial da OpenAI** para classificar e-mails recebidos em duas categorias principais:

- **Produtivo**: e-mails que requerem ação ou resposta (ex: suporte, dúvidas, atualizações).
- **Improdutivo**: e-mails sem necessidade de resposta (ex: felicitações, agradecimentos).

Além da classificação, o sistema também gera **respostas automáticas em formato de e-mail profissional**, escritas por um atendente virtual.

---

## 🌐 Deploy

- 🔗 **Backend** hospedado no [Render](https://render.com/)
- 💻 **Frontend** disponível via GitHub Pages:  
  👉 https://thialylima.github.io/Classificador-de-emails-front/

⚠️ **Importante**: O Render entra em modo de hibernação após 15 minutos de inatividade. Isso pode causar uma pequena demora na primeira resposta após esse tempo.

---

## 🚀 Funcionalidades

- Classificação automática de e-mails via texto, arquivo ou ambos.
- Geração de resposta automática em linguagem natural.
- Suporte a arquivos `.pdf` e `.txt`.
- Integração com a API OpenAI (`gpt-4.1-mini`).

---

## 🧠 Tecnologias utilizadas

- FastAPI
- OpenAI API
- Python 3.11+
- Uvicorn
- dotenv
- PyMuPDF (fitz)

---

## ⚙️ Como rodar localmente

### 1. Clone o repositório

```
git clone https://github.com/thialylima/Classificador-de-emails-back.git
cd Classificador-de-emails-back
```

### 2. Crie e ative o ambiente virtual

```
python -m venv .venv
.venv\Scripts\activate    # No Windows
# source .venv/bin/activate  # No Linux/macOS
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Configure a chave da OpenAI

Crie um arquivo chamado `.env` na raiz do projeto e insira:

```
OPENAI_API_KEY=sua-chave-aqui
```

Você pode obter sua chave em: https://platform.openai.com/account/api-keys

### 5. Rode o servidor

```
uvicorn main:app --reload
```

O FastAPI estará acessível em: http://127.0.0.1:8000/docs

---

## 🔁 Endpoint `/processar`

Este endpoint aceita:

- Apenas texto (`email`)
- Apenas arquivo (`file`)
- **Ou ambos juntos**

### Campos aceitos:

| Campo  | Tipo          | Obrigatório? | Descrição                        |
|--------|---------------|--------------|----------------------------------|
| email  | string (Form) | Opcional     | Texto do e-mail                  |
| file   | UploadFile    | Opcional     | Arquivo `.pdf` ou `.txt`         |

### Exemplo com apenas texto:

```
email: Olá, gostaria de saber o status da minha solicitação.
```

### Exemplo com arquivo:

Envie um arquivo no campo `file` via `multipart/form-data`.

---

## 📁 Estrutura do projeto

```
Classificador-de-emails-back/
│
├── main.py              # Código principal com FastAPI e integração com OpenAI
├── requirements.txt     # Dependências do projeto
├── .env                 # chave da OpenAI
├── .gitignore           # Ignora venv, .env e arquivos desnecessários
└── README.md            # Este arquivo
```

---

## ✅ Exemplo de resposta esperada

```
{
  "categoria": "Produtivo",
  "resposta": "Prezado(a),\n\nAgradecemos o contato. Estamos verificando sua solicitação e em breve entraremos em contato com uma atualização.\n\nAtenciosamente,\nThialy Lima"
}
```

---

## 📌 Observações

* Caso a chave da OpenAI esteja sem crédito ou exceda o limite, será retornado erro HTTP 429.
* Utiliza o modelo `gpt-4.1-mini`, que oferece ótimo desempenho com custo reduzido.

---

## 👨‍💻 Desenvolvido por

**Thialy Lima**  
https://github.com/thialylima
