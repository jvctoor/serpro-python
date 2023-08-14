
from fastapi import FastAPI

app = FastAPI();

vendas = {
    1: "copo",
    2: "escova"
}

@app.get("/home")
def home():
    return "Minha api está no ar"

@app.get("/vendas/{id_venda}")
def vendaById(id_venda: int):
    return vendas[id_venda]

