from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class UserBase(SQLModel):
    id: int = Field(primary_key=True, index=True)
    mid: str = Field(index=True)
    account_id: str = Field()

    bank = relationship("BankDetails", back_populates="user")

class BankDetailsBase(SQLModel):
    id: int = Field(primary_key=True, index=True)
    relationship_id: str = Field(index=True)
    bank_name: str = Field()
    account_type: str = Field()
    account_number: str = Field()
    routing_number: str = Field()
    ach_relationship_id: str = Field()
    owner_id: int = Field(foreign_key="users.id")

    user = relationship("User", back_populates="bank")


# # Properties to receive via API on creation
# class UserCreate(UserBase):
#     password: str


# # TODO replace email str with EmailStr when sqlmodel supports it
# class UserRegister(SQLModel):
#     email: str
#     password: str
#     full_name: str | None = None


# # Properties to receive via API on update, all are optional
# # TODO replace email str with EmailStr when sqlmodel supports it
# class UserUpdate(UserBase):
#     email: str | None = None  # type: ignore
#     password: str | None = None


# # TODO replace email str with EmailStr when sqlmodel supports it
# class UserUpdateMe(SQLModel):
#     full_name: str | None = None
#     email: str | None = None


# class UpdatePassword(SQLModel):
#     current_password: str
#     new_password: str


# # Database model, database table inferred from class name
# class User(UserBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     hashed_password: str
#     items: list["Item"] = Relationship(back_populates="owner")


# # Properties to return via API, id is always required
# class UserPublic(UserBase):
#     id: int


# class UsersPublic(SQLModel):
#     data: list[UserPublic]
#     count: int


# # Shared properties
# class ItemBase(SQLModel):
#     title: str
#     description: str | None = None


# # Properties to receive on item creation
# class ItemCreate(ItemBase):
#     title: str


# # Properties to receive on item update
# class ItemUpdate(ItemBase):
#     title: str | None = None  # type: ignore


# # Database model, database table inferred from class name
# class Item(ItemBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str
#     owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
#     owner: User | None = Relationship(back_populates="items")


# # Properties to return via API, id is always required
# class ItemPublic(ItemBase):
#     id: int
#     owner_id: int


# class ItemsPublic(SQLModel):
#     data: list[ItemPublic]
#     count: int


# # Generic message
# class Message(SQLModel):
#     message: str


# # JSON payload containing access token
# class Token(SQLModel):
#     access_token: str
#     token_type: str = "bearer"


# # Contents of JWT token
# class TokenPayload(SQLModel):
#     sub: int | None = None


# class NewPassword(SQLModel):
#     token: str
#     new_password: str
