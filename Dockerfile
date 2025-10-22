# Imagem base oficial do Python
FROM python:3.13-slim

# Define o diret�rio de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as depend�ncias
RUN pip install --no-cache-dir -r requirements.txt

# Exp�e a porta padr�o do Uvicorn
EXPOSE 8080

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]