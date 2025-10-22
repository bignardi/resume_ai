# Resume AI

API para gera��o e an�lise de curr�culos utilizando intelig�ncia artificial.

## Requisitos

- Python 3.13 ou superior
- Docker (opcional)

## Instala��o Local

1. Clone o reposit�rio:
   ```bash
   git clone https://github.com/bignardi/resume_ai.git
   cd resume_ai

2. Crie e ative um ambiente virtual:
   ```bash
python -m venv .venv
.venv\Scripts\activate

3. Instale as depend�ncias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplica��o:
uvicorn app:app --host 0.0.0.0 --port 8000

5. Acesse no navegador:

http://localhost:8000/

Documenta��o Swagger:
http://localhost:8000/docs

## Utilizando com Docker

1. Construa a imagem Docker:
docker build -t resume_ai .

2. Rode o container:
docker run -it -p 8000:8000 resume_ai

3. Acesse a API:
http://localhost:8000/
http://localhost:8000/docs

## Licen�a

Este projeto est� licenciado sob a licen�a MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.