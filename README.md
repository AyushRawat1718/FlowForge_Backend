# FlowForge Backend

FastAPI backend for FlowForge — an AI workflow pipeline builder.

## Features

* Pipeline parsing endpoint
* Directed Acyclic Graph (DAG) validation
* Node and edge analysis
* FastAPI REST API
* CORS-enabled frontend integration

## Tech Stack

* Python
* FastAPI
* Uvicorn

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "FlowForge backend is running successfully!"
}
```

---

### Parse Pipeline

```http
POST /pipelines/parse
```

Request Body:

```json
{
  "nodes": [],
  "edges": []
}
```

Response:

```json
{
  "num_nodes": 3,
  "num_edges": 2,
  "is_dag": true
}
```

## Local Development

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```
