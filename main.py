from fastapi import FastAPI, HTTPException, status, Response, Path, Header, Depends
from model import Digital_solutions_11
from typing import Optional, Any, List
import requests

app = FastAPI(title='DS11', version="0.0.1", description="API of Students.")  #Variável que armazena e instância a classe FastAPI

students = {
    1:{
        "name": "Andrey Rosa Dias",
        "birthdate": "24/03/2005",
        "area": "AI",
        "edv": 92904262,
        "fav_ice_cream": "Creme"
    },

    2:{
        "name": "Vitoria Stefany Grizotto",
        "birthdate": "17/02/2006",
        "area": "SAP",
        "edv": 92904198,
        "fav_ice_cream": "flocos"
    },

    3:{
        "name": "Emilly Rodrigues de Mello",
        "birthdate": "27/10/2005",
        "area": "Web3",
        "edv": 92904246,
        "fav_ice_cream": "tropical fruits"
    }
}

def fake_db():
    try:
        print('Conecting DB...')

    finally:
        print('Closing DB...')

@app.get("/pokemon/{name}")
async def get_pokemon(name: str):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return {'Msg': 'Deu ruim'}

@app.get("/")
async def beginning():  #Função assíncriona
    return {"Message": "Hello DS11"}  #O que a função retorna

@app.get("/students", summary="Return all students.", response_model=List[Digital_solutions_11])
async def get_students_ds11(db: Any = Depends(fake_db)):
    return students

@app.get("/students/{student_id}")
async def get_student_ds11(student_id: int = Path(..., title='Student ID', description='O ID deve ser entre 1 e 3', gt=0, lt=4)):
    try:
        student = students[student_id]
        return student
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
@app.post("/students", status_code=status.HTTP_201_CREATED, description="Create new student.")
async def post_students_ds11(student: Optional[Digital_solutions_11] = None):
    try:
        next_id = len(students) + 1

        students[next_id] = student
        del student.id
        return student
    except KeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This student already exists.")
    
@app.put("/students/{student_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_students_ds11(student_id: int, student: Digital_solutions_11):
    if student_id in students:
        students[student_id] = student
        student.id = student_id
        return student
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
@app.delete("/students/{student_id}")
async def delete_student_ds11(student_id: int):
    if student_id in students:
        del students[student_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
# Query
@app.get("/calculadora")
async def cacular(n1: int, n2: int):
    soma = n1 + n2
    return {"Resultado": soma}

# Header
@app.get("/ds11")
async def exHeader(msg: str = Header(...)):
    return{f"Message": {msg}}

# 


if __name__ == "__main__":  #É o que vai executar o servidor sem que precise usar o terminal toda vez.
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

    '''
    uvicorn.run - roda o uvicorn
    ("main:app") é o nome do meu arquivo (main) + o nome da minha variável que armazena a classe FastAPI (app)
    (host="127.0.0.1") é o host do local onde meu servidor vai ficar hospedado
    (port=8000) é a porta que meu servidor vai ser aberto
    (log_level="info") é a descrição do que é minha API, ajuda na documentação
    (reload=True) é pra recarregar sozinho sem precisar ficar abrindo o servidor várias vezes

    '''