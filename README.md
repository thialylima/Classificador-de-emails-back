# 📬 Classificador de E-mails - Backend (FastAPI + OpenAI)

Este projeto é um backend desenvolvido com **FastAPI** que utiliza **inteligência artificial da OpenAI** para classificar e-mails recebidos em duas categorias principais:

- **Produtivo**: e-mails que requerem ação ou resposta (ex: suporte, dúvidas, atualizações).
- **Improdutivo**: e-mails sem necessidade de resposta (ex: felicitações, agradecimentos).

Além da classificação, o sistema também gera **respostas automáticas em formato de e-mail profissional**, escritas por um atendente virtual.


---

## 🌐 Deploy

- 🔗 **Backend** hospedado no [Render](https://render.com/)
- 💻 **Frontend** disponível via GitHub Pages:  
  👉 [https://thialylima.github.io/Classificador-de-emails-front/](https://thialylima.github.io/Classificador-de-emails-front/)

⚠️ **Importante**: O Render entra em modo de hibernação após 15 minutos de inatividade. Isso pode causar uma pequena demora na primeira resposta após esse tempo.

---

## 🚀 Funcionalidades

- Classificação automática de e-mails recebidos via POST.
- Geração de resposta automática em linguagem natural.
- Integração com a API OpenAI (`gpt-4.1-mini`).

---

## 🧠 Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI API](https://platform.openai.com/)
- [Python 3.11+](https://www.python.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/thialylima/Classificador-de-emails-back.git
cd Classificador-de-emails-back
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate    # No Windows
# source .venv/bin/activate  # No Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da OpenAI

Crie um arquivo chamado `.env` na raiz do projeto e insira:

```env
OPENAI_API_KEY=sua-chave-aqui
```

Você pode obter sua chave em: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

### 5. Rode o servidor

```bash
uvicorn main:app --reload
```

O FastAPI estará acessível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Acesse a interface de testes

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Lá você pode testar a rota `POST /processar-email` com o corpo:

```json
{
  "email": "Olá, gostaria de saber como está o andamento da minha solicitação de reembolso."
}
```

---

## 📁 Estrutura do projeto

```
Classificador-de-emails-back/
│
├── main.py              # Código principal com FastAPI e integração com OpenAI
├── requirements.txt     # Dependências do projeto
├── .env                 # (não versionado) chave da OpenAI
├── .gitignore           # Ignora venv, .env e arquivos desnecessários
└── README.md            # Este arquivo
```

---

## ✅ Exemplo de resposta esperada

```json
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
🔗 [github.com/thialylima](https://github.com/thialylima)

---
