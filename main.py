from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from mylib.logic import *
from mylib.connectDB import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
CAT = ""
NAME = ""

@app.get("/")
async def root():
    return {"message": "Welcome to Pokedex"}

#Get the complete pokedex
@app.get("/all", response_class=HTMLResponse)
async def queryAll(request: Request):
    conn,cursor = connect_db()
    result = query_all(cursor)
    close_db(conn)
    columns = [ "ID", "Name", "Form", "Type1", "Type2", "Total", "HP", "Attack", "Defense","Sp_Atk","Sp_Def","Speed","Generation"]
    return templates.TemplateResponse("form.html", {"request":request, "columns":columns, "results":result})

#By default it's a pokedex for 9th generation
@app.get("/query", response_class=HTMLResponse)
async def query(request: Request):
    conn,cursor = connect_db()
    result = query_specific(cursor)
    close_db(conn)
    global CAT, NAME
    CAT = "Generation"
    NAME = "9"
    columns = [ "ID", "Name", "Form", "Type1", "Type2", "Total", "HP", "Attack", "Defense","Sp_Atk","Sp_Def","Speed","Generation"]
    return templates.TemplateResponse("form.html", {"request":request, "columns":columns, "results":result})

#Query for specific items, with format: /query/COLUMN_NAME/SPECIFIC_ITEM 
#Example: /query/generation/9
#if it is a Pokemon name or type name, please use ""
#Example: /query/Name/"Pikachu"
@app.get("/query/{cat}/{name}", response_class=HTMLResponse)
async def query_custom(request:Request, cat: str, name:str):
    conn,cursor = connect_db()
    result = query_specific(cursor,cat,name)
    close_db(conn)
    global CAT,NAME
    CAT = cat
    NAME = name
    columns = [ "ID", "Name", "Form", "Type1", "Type2", "Total", "HP", "Attack", "Defense","Sp_Atk","Sp_Def","Speed","Generation"]
    return templates.TemplateResponse("form.html", {"request":request, "columns":columns, "results":result})

#apply sorting based on given category and rule (DESC or ASC) on previously fetched result
#Example: /order_by/Attack/DESC
@app.get("/order_by/{category}/{rule}", response_class=HTMLResponse)
async def sort_order_by(request:Request, category: str, rule:str):
    conn,cursor = connect_db()
    result = order_by(cursor,CAT,NAME,category,rule)
    close_db(conn)
    columns = [ "ID", "Name", "Form", "Type1", "Type2", "Total", "HP", "Attack", "Defense","Sp_Atk","Sp_Def","Speed","Generation"]
    return templates.TemplateResponse("form.html", {"request":request, "columns":columns, "results":result})

if __name__ == '__main__':
    
    uvicorn.run(app, port=8080, host="0.0.0.0")