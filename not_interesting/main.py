#Lib's
import uvicorn
#Classes
from not_interesting.api import server

app = server.app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)