# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.templating import Jinja2Templates
import os
import sqlite3
from datetime import date

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'frontend' directory as a static directory
folder = os.path.dirname(__file__)

app.mount("/static", StaticFiles(directory=folder + "/frontend/static", html=True), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="frontend/templates")

# SQLite functions
def fetch_word_from_sqlite(current_date):
    conn = sqlite3.connect('database/word_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM daily_words WHERE date=?", (current_date,))
    result = cursor.fetchone()

    conn.close()

    return result


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Fetch the current date
    current_date = str(date.today())
    current_date = "02/01/2024"
    # Check if the data is already in Redis
    word_data = fetch_word_from_sqlite(current_date)

    if not word_data:
        word_data = ('No Date Found', 'No Word Found', 'No Definition Found', 'No Example1 Found', 'No Example2 Found')

    # Extract individual values
    _, word, definition, example1, example2 = word_data

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "word": word, "definition": definition, "example1": example1, "example2": example2}
    )

# Add additional routes for definition, examples, and Spotify song
# You can use different routes like /definition, /examples, etc.

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
