from typing import Any

from sqlmodel import Session, select

from app.models import UserBase, BankDetailsBase

# from app.core.security import get_password_hash, verify_password
# from app.models import Item, ItemCreate, User, UserCreate, UserUpdate

def create_user(*, session: Session, user_in: UserBase) -> UserBase:
    db_user = UserBase.model_validate(user_in)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_mid(*, session: Session, mid: str) -> UserBase | None:
    statement = select(UserBase).where(UserBase.mid == mid)
    session_user = session.exec(statement).first()
    return session_user

def create_bank_details(*, session: Session, bank_details_in: BankDetailsBase) -> BankDetailsBase:
    db_bank_details = BankDetailsBase.model_validate(bank_details_in)
    session.add(db_bank_details)
    session.commit()
    session.refresh(db_bank_details)
    return db_bank_details

def create_bank_details(*, session: Session, bank_details_in: BankDetailsBase) -> BankDetailsBase:
    db_bank_details = BankDetailsBase.model_validate(bank_details_in)
    session.add(db_bank_details)
    session.commit()
    session.refresh(db_bank_details)
    return db_bank_details


# def authenticate(*, session: Session, email: str, password: str) -> User | None:
#     db_user = get_user_by_email(session=session, email=email)
#     if not db_user:
#         return None
#     if not verify_password(password, db_user.hashed_password):
#         return None
#     return db_user
