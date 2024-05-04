import secrets
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request

# Assuming authentication, database, and chat services will be structured with routers
# from authentication_service.main import router as auth_router
# from database_service.main import router as db_router
# from chat_service.main import router as chat_router

app = FastAPI(title='API Gateway', description='API Gateway for LangChain services', version='0.1')

#Middleware Config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="secret_key",
)

def renegerate_secret_key():
    new_secret_key - secrets.token_urlsafe(32)
    app.user_state.session.secret_key = new_secret_key
    

#Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
    
# Including routers from other services once they are implemented
# Uncomment the following lines as you develop other modules
# app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# app.include_router(db_router, prefix="/database", tags=["Database"])
# app.include_router(chat_router, prefix="/chat", tags=["Chat"])
#Use langchain agent to interact with the services
#Change to Langchain Agents

#Root endpoint for testing
@app.get("/", tags=["Root"])
async def root():
    return {"message": "API Gateway for LangChain services"}


# Run the application using Uvicorn if this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)