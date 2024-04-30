from fastapi import Header, HTTPException, Security, Request, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWTError
from typing import Optional