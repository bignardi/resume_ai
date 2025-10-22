# Resume AI

API para geração e análise de currículos utilizando inteligência artificial.

## Requisitos

- Python 3.13 ou superior
- Docker (opcional)

## Instalação Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/bignardi/resume_ai.git
   cd resume_ai

2. Crie e ative um ambiente virtual:
   ```bash
python -m venv .venv
.venv\Scripts\activate

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
uvicorn app:app --host 0.0.0.0 --port 8000

5. Acesse no navegador:

http://localhost:8000/

Documentação Swagger:
http://localhost:8000/docs

## Utilizando com Docker

1. Construa a imagem Docker:
docker build -t resume_ai .

2. Rode o container:
docker run -it -p 8000:8000 resume_ai

3. Acesse a API:
http://localhost:8000/
http://localhost:8000/docs

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.