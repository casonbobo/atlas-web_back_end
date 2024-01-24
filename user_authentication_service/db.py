#!/usr/bin/env python3
"""DB module
    Copied from Atlas Intranet
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import bcrypt

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by keyword arguments."""
        try:
            query = self._session.query(User).filter_by(**kwargs).first()
            if query is None:
                raise NoResultFound
            return query
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user."""
        user = self.find_user_by(id=user_id)
        if user is None:
            raise ValueError("No user found with the provided id.")

        for attr, value in kwargs.items():
            if not hasattr(User, attr):
                raise ValueError(f"Invalid attribute '{attr}'.")
            setattr(user, attr, value)

        self._session.commit()
