from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Monter les fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration de Jinja2
templates = Jinja2Templates(directory="templates")

# Route HTML avec un template Jinja2
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

# Route de base retournant un JSON
@app.get("/")
def read_root():
    """Cette fonction retourne juste un JSON"""
    return {"Hello": "World"}

# Route JSON pour obtenir un item avec paramètre optionnel
@app.get("/items/{item_id}")
def read_item_json(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
