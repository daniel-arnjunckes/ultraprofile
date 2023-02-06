from sqlalchemy.orm import Session
from models import Profile

class ProfileDTO:
    @staticmethod
    def get_all(db: Session) -> list[Profile]:
        return db.query(Profile).all()
    
    @staticmethod
    def save(db: Session, profile: Profile) -> Profile:
        if profile.id:
            db.merge(profile)
        else:
            db.add(profile)
        db.commit()

        return profile
    
    @staticmethod
    def get_by_id(db: Session, id: int) -> Profile:
        return db.query(Profile).filter(Profile.id == id).first()
    
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Profile).filter(Profile.id == id).first() is not None
    
    # Potencial para melhoria?
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        profile = db.query(Profile).filter(Profile.id ==id).first
        if profile is not None:
            db.delete(profile)
            db.commit