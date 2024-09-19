from fastapi import FastAPI, HTTPException, status, Response, Path, Header, Depends
from model import Whales
from typing import Optional, Any, List

app = FastAPI(title='Whales', version='0.0.1', description='Whales Species.')

species = {
    1: {
        "scientific_name": "Balaenoptera musculus",
        "name": "Blue Whale",
        "max_weight": "Up to 200 tons",
        "max_lenght": "Up to 100 feet (30 meters)",
        "name_pt_br": "Baleia Azul"
    },

    2: {
        "scientific_name": "Balaena mysticetus",
        "name": "Bowhead Whale",
        "max_weight": "Up to 100 tons",
        "max_lenght": "Up to 66 feet (20 meters)",
        "name_pt_br": "Baleia de Cabeça Grande ou Baleia-Bowhead"
    },

    3: {
        "scientific_name": "Balaenoptera brydei",
        "name": "Bryde's Whale",
        "max_weight": "Up to 25 tons",
        "max_lenght": "Up to 55 feet (17 meters)",
        "name_pt_br": "Baleia de Bryde"
    },

    4: {
        "scientific_name": "Balaenoptera acutorostrata",
        "name": "Common Minke Whale",
        "max_weight": "Up to 10 tons",
        "max_lenght": "Up to 35 feet (10.7 meters)",
        "name_pt_br": "Baleia Minke Comum"
    },

    5: {
        "scientific_name": "Kogia sima",
        "name": "Dwarf Sperm Whale",
        "max_weight": "Up to 1.5 tons",
        "max_lenght": "Up to 9 feet (2.7 meters)",
        "name_pt_br": "Cachalote-Anão"
    },

    6: {
        "scientific_name": "Balaenoptera physalus",
        "name": "Fin Whale",
        "max_weight": "Up to 80 tons",
        "max_lenght": "Up to 85 feet (26 meters)",
        "name_pt_br": "Baleia Fin"
    },

    7: {
        "scientific_name": "Eschrichtius robustus",
        "name": "Gray Whale",
        "max_weight": "Up to 36 tons",
        "max_lenght": "Up to 49 feet (15 meters)",
        "name_pt_br": "Baleia-Cinza"
    },

    8: {
        "scientific_name": "Megaptera novaeangliae",
        "name": "Humpback Whale",
        "max_weight": "Up to 40 tons",
        "max_lenght": "Up to 60 feet (18 meters)",
        "name_pt_br": "Baleia-Jubarte"
    },

    9: {
        "scientific_name": "Eubalaena glacialis",
        "name": "North Atlantic Right Whale",
        "max_weight": "Up to 70 tons",
        "max_lenght": "Up to 55 feet (17 meters)",
        "name_pt_br": "Baleia-Franca-Norte"
    },

    10: {
        "scientific_name": "Kogia breviceps",
        "name": "Pygmy Sperm Whale",
        "max_weight": "Up to 1 ton",
        "max_lenght": "Up to 8.5 feet (2.6 meters)",
        "name_pt_br": "Cachalote-Pigmeu"
    }
}


# GET:
@app.get('/')
async def beginning():
    return {'For whale': 'whales/id',
            'For all whales': 'whales'}

@app.get('/whales')
async def get_whales():
    return species

@app.get('/whales/{whale_id}')
async def get_whale_id(whale_id: int):
    try:
        whale = species[whale_id]
        return whale
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Whale not found.")


# POST:
@app.post('/whales', status_code=status.HTTP_201_CREATED, description="Add whale.")
async def post_whales(whale: Optional[Whales] = None):
    try:
        next_id = len(species) + 1

        species[next_id] = whale
        del whale.id
        return whale
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This whale already exists.")
    

# PUT:
@app.put('/whales/{whale_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_whales(whale_id: int, whale: Whales):
    if whale_id in species:
        species[whale_id] = whale
        whale.id = whale_id
        return whale
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Whale no found.")
    
# DELETE:
@app.delete("/whales/{whale_id}")
async def delete_whale(whale_id: int):
    if whale_id in species:
        del species[whale_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Whale not found.")
    

# DESAFIO 01: MÉTODO PATCH

@app.patch("/whale/{whale_id}", response_model=Whales)
async def patch_whale(whale_id: int, atr_update=Whales):
    if whale_id not in species:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Whale not found.")
    
    if whale_id 


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("exercise:app", host="127.0.0.1", port=8000, log_level="info", reload=True)