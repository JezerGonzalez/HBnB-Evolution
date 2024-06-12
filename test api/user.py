from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=6)

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


from fastapi import APIRouter, HTTPException, status
from app.models.user import User, UserCreate
from typing import List
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

# Almacenamiento en memoria para los usuarios
users_db = {}
id_counter = 1

@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global id_counter
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict.update({"id": id_counter, "hashed_password": hashed_password})
    users_db[id_counter] = user_dict
    id_counter += 1
    return User(**user_dict)

@router.get("/users", response_model=List[User])
def read_users():
    return [User(**user) for user in users_db.values()]

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**users_db[user_id])

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict.update({"id": user_id, "hashed_password": hashed_password})
    users_db[user_id] = user_dict
    return User(**user_dict)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return
