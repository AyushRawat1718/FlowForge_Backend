# FlowForge Backend

`FlowForge Backend` is a FastAPI-based backend service designed to support the FlowForge workflow pipeline builder. The backend is responsible for processing pipeline graph data received from the frontend, analyzing graph structure, and validating whether the workflow forms a Directed Acyclic Graph (DAG).

The service exposes REST API endpoints that allow the frontend to submit pipeline node and edge data for real-time graph analysis.

---

# Project Overview

The backend receives pipeline data from the React frontend and performs:

* Node counting
* Edge counting
* Graph traversal
* Cycle detection
* DAG validation

The processed results are returned to the frontend and displayed through a custom analysis modal.

---

# Key Features

## Pipeline Graph Analysis

The backend analyzes incoming workflow structures by:

* Counting total nodes
* Counting total edges
* Building graph adjacency mappings
* Traversing graph relationships

---

## Directed Acyclic Graph (DAG) Validation

A graph traversal algorithm is implemented to determine whether the submitted workflow contains cycles.

The backend validates:

* Valid DAG pipelines
* Cyclic graph detection
* Workflow integrity

---

## FastAPI REST API

The backend provides lightweight and fast API endpoints using FastAPI.

Features include:

* JSON request handling
* RESTful API structure
* Frontend integration support
* CORS-enabled communication

---

# Tech Stack

* Python
* FastAPI
* Uvicorn

---

# API Endpoints

## Health Check

```http id="1n7dca"
GET /
```

Response:

```json id="v5t8k4"
{
  "message": "FlowForge backend is running successfully!"
}
```

---

## Parse Pipeline

```http id="9n9a6m"
POST /pipelines/parse
```

Request Body:

```json id="x4f6zh"
{
  "nodes": [],
  "edges": []
}
```

Response:

```json id="k2n8yf"
{
  "num_nodes": 3,
  "num_edges": 2,
  "is_dag": true
}
```

---

# Running the Project Locally

## 1. Clone Repository

```bash id="r7s0u1"
git clone https://github.com/AyushRawat1718/FlowForge_Backend
```

---

## 2. Create Virtual Environment

```bash id="p8v2y3"
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash id="f3w7n5"
venv\Scripts\activate
```

### Mac/Linux

```bash id="z6x1m8"
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash id="d4b9k2"
pip install -r requirements.txt
```

---

## 5. Run Backend Server

```bash id="g8r5y1"
uvicorn main:app --reload
```

Backend runs at:

```bash id="w2k7p9"
http://127.0.0.1:8000
```

---

# Frontend Integration

The backend is configured to communicate with the deployed React frontend using CORS middleware.

Frontend Deployment:
https://flow-forge-1718.vercel.app

---

# Live Deployment

Backend:
https://flowforge-backend.onrender.com

---

# Developed By

Ayush Rawat
