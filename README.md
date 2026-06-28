# Clinica Veterinária API

API REST desenvolvida em Python com Flask para o Trabalho Final da disciplina de Cloud Computing — UNIDAVI (2026).

O sistema simula o gerenciamento de pacientes de uma clínica veterinária, expondo endpoints para consulta de registros via HTTP.

---

## Pré-requisitos

- Python 3.10 ou superior
- pip
- Git

---

## Estrutura de Diretórios

```
.
├── api/
│   ├── app.py              # Código principal da API
│   ├── requirements.txt    # Dependências do projeto
│   ├── data/
│   │   └── pacientes.json  # Dados simulados dos pacientes
│   └── testes/
│       └── test_api.py     # Testes unitários com pytest
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de Integração Contínua
└── README.md
```

---

## Execução Local — Sem Container

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/clinica-vet-api.git
cd clinica-vet-api
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r api/requirements.txt
```

### 4. Inicie a API

```bash
python api/app.py
```

A API estará disponível em `http://localhost:5000`.

---

## Execução Local — Com Container (Docker)

> Requer Docker instalado: https://docs.docker.com/get-docker/

### 1. Construa a imagem

```bash
docker build -t clinica-vet-api .
```

### 2. Inicie o container

```bash
docker run -p 5000:5000 clinica-vet-api
```

A API estará disponível em `http://localhost:5000`.

---

## Endpoints Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/status` | Retorna nome, versão e status da API |
| GET | `/pacientes` | Retorna todos os pacientes cadastrados |
| GET | `/pacientes/{id}` | Retorna um paciente pelo ID |

### Exemplos de resposta

**GET /status**
```json
{
  "status": "success",
  "data": {
    "nome": "Clinica Vet. API",
    "versao": "1.0.0",
    "status": "ok"
  }
}
```

**GET /pacientes/1**
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "nome": "Rex",
    "especie": "Cachorro",
    "raca": "Labrador",
    "idade": 3,
    "peso_kg": 28.5,
    "tutor": "Carlos Souza",
    "telefone_tutor": "(47) 99999-0001",
    "ultima_consulta": "2026-03-15",
    "status": "ativo"
  }
}
```

**GET /pacientes/999** (ID inexistente)
```json
{
  "status": "error",
  "mensagem": "Paciente com o id 999 não foi encontrado"
}
```

---

## Executando os Testes

Com o ambiente virtual ativado:

```bash
pytest api/testes/ -v
```

Para gerar relatório de cobertura:

```bash
pip install pytest-cov
pytest api/testes/ --cov=api --cov-report=term-missing
```

---

## Identificação

- **Instituição:** UNIDAVI
- **Curso:** Bacharelado em Sistemas de Informação
- **Disciplina:** Cloud Computing
- **Professor:** Prof. Esp. Ademar Perfoll Junior
- **Aluno:** Gustavo
- **Prazo:** 29 de junho de 2026