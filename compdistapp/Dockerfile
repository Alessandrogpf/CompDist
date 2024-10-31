# imagem base
FROM python:3.12-slim

# Instala o gcc, pois o MAC eh uma maravilha
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório 
WORKDIR /app


COPY requirements.txt .

# Intala as dependências do projeto
RUN pip install -r requirements.txt

# Copia o conteúdo do diretório atual para o diretório de trabalho no container
COPY . .

# Variavel de ambieente
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Porta que o container vai colocar
EXPOSE 8080

# rodar o app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
