from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://flow-forge-1718.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "FlowForge backend is running successfully!"
    }


@app.post("/pipelines/parse")
async def parse_pipeline(payload: dict):

    nodes = payload.get("nodes", [])
    edges = payload.get("edges", [])

    num_nodes = len(nodes)
    num_edges = len(edges)

    # Build adjacency list
    graph = {}

    for node in nodes:
        graph[node["id"]] = []

    for edge in edges:
        source = edge["source"]
        target = edge["target"]

        graph[source].append(target)

    # DAG Detection using DFS
    visited = set()
    visiting = set()

    def has_cycle(node):

        if node in visiting:
            return True

        if node in visited:
            return False

        visiting.add(node)

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        visiting.remove(node)
        visited.add(node)

        return False

    is_dag = True

    for node in graph:
        if has_cycle(node):
            is_dag = False
            break

    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": is_dag,
    }