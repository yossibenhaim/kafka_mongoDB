from fastapi import FastAPI, HTTPException
from pub.producer import Producer


app = FastAPI()
producer = Producer()

@app.get("/")
def get_root():
    return {'Hello':'World'}


#Read
#All
@app.get("/send_interesting")
async def send_interesting():
    try:
        producer.send_message("interesting", producer.get_interesting())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

@app.get("/send_not_interesting")
async def send_not_interesting():
    try:
        producer.send_message("not_interesting", producer.get_not_interesting())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})