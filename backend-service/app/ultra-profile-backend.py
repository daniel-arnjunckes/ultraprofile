from pathlib import Path
import sys

root_path = Path(__file__).parents[2]
sys.path.append(str(root_path))


from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .dto.models import Profile
from .dto.database import get_db, engine, Base
from .dto.profiles_dto import ProfileDTO
from .dto.schemas import ProfileRequest, ProfileResponse, NewProfileRequest


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/api/health-check")
async def health_check():
    return {
        "status":"Health!" 
    }

@app.get("/api/profile/{profile_id}", response_model = ProfileResponse)
async def get_profile(id: int, db: Session = Depends(get_db)):
    profile = ProfileDTO.get_by_id(db, id)
    if not profile:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Profile not found"
        )
    return ProfileResponse.from_orm(profile)


@app.get("/api/profile", response_model=list[ProfileResponse])
async def get_all_profiles(db: Session = Depends(get_db)):
    profiles = ProfileDTO.get_all(db)    
    return [
        ProfileResponse.from_orm(profile) for profile in profiles
        ]


@app.put("/api/profile", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(request: ProfileRequest, db: Session = Depends(get_db)):
    profile = ProfileDTO.create(db, Profile(**request.dict()))
    return ProfileResponse.from_orm(profile)

@app.post("/api/profile", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def update_profile(request: NewProfileRequest, db: Session = Depends(get_db)):
    
    if not ProfileDTO.exists_by_id(db, request.id):
                raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Profile not found"
        )    
    profile = ProfileDTO.update(db, Profile(**request.dict()))
    return ProfileResponse.from_orm(profile)

@app.delete("/api/profile/{profile_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_profile(id: int, db: Session = Depends(get_db)):
    if not ProfileDTO.exists_by_id(db, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Profile not found"
        )
    ProfileDTO.delete_by_id(db, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)