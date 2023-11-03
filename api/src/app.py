from datetime import datetime
from typing import TypedDict

from fastapi import FastAPI, Form, status, Query
from fastapi.responses import RedirectResponse
from datetime import timedelta

from services.database import JSONDatabase

app = FastAPI()


class Quote(TypedDict):
    name: str
    message: str
    time: str


database: JSONDatabase[list[Quote]] = JSONDatabase("data/database.json")


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database when starting API server."""
    if "quotes" not in database:
        print("Adding quotes entry to database")
        database["quotes"] = []


@app.on_event("shutdown")
def on_shutdown() -> None:
    """Close database when stopping API server."""
    database.close()


@app.post("/quote")
def post_message(name: str = Form(), message: str = Form()) -> RedirectResponse:
    """
    Process a user submitting a new quote.
    You should not modify this function except for the return value.
    """
    now = datetime.now().replace(microsecond=0)

    quote = Quote(name=name, message=message, time=now.isoformat())
    database["quotes"].append(quote)

    # You may modify the return value as needed to support other functionality
    return RedirectResponse("/", status.HTTP_303_SEE_OTHER)


# TODO: add another API route with a query parameter to retrieve quotes based on max age

@app.get("/quote")
def get_quotes(max_age: str = Query("all")) -> list[Quote]:
    max_age_to_timedelta = {
        "week": timedelta(weeks=1),
        "month": timedelta(days=30),
        "year": timedelta(days=365),
    }
    ageLimit = datetime.now()-timedelta(days=7)
    current_time = datetime.now()
    filtered_quotes = [
        quote for quote in database["quotes"]
        if datetime.fromisoformat(quote["time"]) >= ageLimit
    ]

    return filtered_quotes