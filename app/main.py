from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import auth, users, transactions, investments
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Finance Manager App")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(investments.router, prefix="/investments", tags=["Investments"])


@app.get("/")
def home():
    print("Redirecting to /docs")
    return RedirectResponse(url="/docs")








# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# from app.api.routes import auth, users, transactions, investments
# from app.db.base import Base
# from app.db.session import engine

# app = FastAPI(title="Finance Manager App")

# templates = Jinja2Templates(directory="templates")

# Base.metadata.create_all(bind=engine)

# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# # Router
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
# app.include_router(investments.router, prefix="/investments", tags=["Investments"])
