
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Profile
from database import engine, Base, get_db
from profiles_dto import ProfileDTO
from schemas import ProfileRequest, ProfileResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health-check")
async def health_check():
    return {
        "status":"Health!" 
    }

@app.get("/profile/{profile_id}")
async def get_profile(profile_id: int):
    response = {
                "status": "error",
                "reason":"Profile ID not found"
                }
    for profile in profiles:
        if profile_id == profile["id"]:
            return profile
    return response

@app.get("/profile", response_model=list[ProfileResponse])
async def get_all_profiles(db: Session = Depends(get_db)):
    profiles = ProfileDTO.get_all(db)    
    return [
        ProfileResponse.from_orm(profile) for profile in profiles
        ]


@app.post("/api/profile", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(request: ProfileRequest, db: Session = Depends(get_db)):
    profile = ProfileDTO.save(db, Profile(**request.dict()))
    return ProfileResponse.from_orm(profile)



@app.delete("/profile/{profile_id}")
async def delete_profile(profile_id: int):
    for profile in profiles:
        if profile_id == profile["id"]:
            del profiles[profile_id]
            return {
                "status":"deleted profile {profile_id}"
            }
        