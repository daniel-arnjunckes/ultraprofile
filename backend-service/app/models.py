from sqlalchemy import Column, Integer, String

from database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id:             int = Column(Integer, primary_key=True, index=True)
    name:           str = Column(String(50), nullable=False)
    age:            int = Column(Integer, nullable=False)
    description:    str = Column(String(100), nullable=True)
    