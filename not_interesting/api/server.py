from fastapi import FastAPI, HTTPException
from ..manager import Manager

app = FastAPI()
manager = Manager()

@app.get("/")
def get_root():
    return {'Hello':'World'}


#Read
#All
@app.get("/get_data")
async def get_all_data():
    try:
        res = manager.get_data_from_db()
        return {"result":res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})