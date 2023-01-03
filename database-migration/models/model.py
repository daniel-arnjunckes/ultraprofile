from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship

Base = declarative_base()


class Profile(Base):  
    __tablename__ = 'profile'
    id      = Column(Integer, primary_key=True)
    name    = Column(String)
    created = Column(DateTime, default=func.now())


class Adress(Base):  
    __tablename__ = 'adress'
    id = Column(Integer, primary_key=True)
    profile_id = Column(ForeignKey('profile.id'),
                           nullable=False,
                           index=True)
    bug_tracker_url = Column(String, unique=True)
    who = Column(String)
    when = Column(DateTime, default=func.now())

    profile = relationship(Profile)

    def __repr__(self):
        return 'id: {}, profile: {}'.format(self.id, self.profile.name)
