from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse) # 
def read_root(request: Request,):
    return templates.TemplateResponse("item.html",{"request": request, })
    # return {"hwllo":"World"}

@app.get("/card", response_class=HTMLResponse) # 
def read_root(request: Request,):
    return templates.TemplateResponse("card.html",{"request": request, })


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, ):
    return templates.TemplateResponse("index.html", {"request": request, })
