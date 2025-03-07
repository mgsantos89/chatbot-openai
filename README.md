# Chatbot Local com OpenAI API

🔹 Objetivo: Criar um chatbot que interaja via terminal ou interface web, utilizando a API da OpenAI (GPT-4).

🔹 Tecnologias: Python (Flask para Web), OpenAI API, Docker (opcional).

chatbot-openai/
│── src/                 # Código-fonte do chatbot
│   ├── main.py          # Versão CLI do chatbot
│   ├── app.py           # Versão Web com Flask
│   ├── chatbot.py       # Módulo central da IA
│── requirements.txt     # Dependências do projeto
│── .env.example         # Modelo de variáveis de ambiente (API Key)
│── README.md            # Documentação principal
│── Dockerfile           # Docker para facilitar deploy (opcional)
│── roadmap.md           # Roadmap completo
│── tests/               # Testes unitários
│── templates/           # HTML para interface web (se houver)
│── static/              # Arquivos CSS/JS (se houver)
