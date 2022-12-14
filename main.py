from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from mylib.logic import filter_by,query_all,query_specific,order_by
from mylib.connectDB import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
CAT = ""
NAME = ""

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("homepage.html",{"request":request})

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

#apply filters to show columns that want to see on previously fetched result
#Example1: /filter/Name/Type1/""/""/""/""
#Example2: /filter/Name/Type1/Total/Generation/""/""
@app.get("/filter/{c1}/{c2}/{c3}/{c4}/{c5}/{c6}", response_class=HTMLResponse)
async def filter(request:Request, c1: str, c2:str,c3:str, c4:str, c5:str, c6:str):
    conn,cursor = connect_db()
    comma = ","
    str_lst_complete = [c1,c2,c3,c4,c5,c6]
    str_lst = []
    for s in str_lst_complete:
        if len(s)>2:
            str_lst.append(s)
    filter_str = ""
    for st in str_lst:
        filter_str += st + comma
    filter_str = filter_str[:-1]
    result = filter_by(cursor,CAT,NAME,filter_str)
    close_db(conn)
    columns = str_lst
    return templates.TemplateResponse("form.html", {"request":request, "columns":columns, "results":result})

if __name__ == '__main__':
    
    uvicorn.run(app, port=8080, host="0.0.0.0")