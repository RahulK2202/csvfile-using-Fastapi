from  fastapi import FastAPI,Request,Depends, File, UploadFile
from fastapi.templating import Jinja2Templates
from  database import engine,SessionLocal
from sqlalchemy.orm import Session
from  models import Userdata , Base 
import csv
from io import StringIO



app=FastAPI()
session = None  
templates = Jinja2Templates(directory="Template")
# Userdata.Base.metadata.create_all(bind=engine)
Userdata.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def DisplayPage(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("HomePage.html", {"request": request, "db": db})


@app.post("/upload")
async def CsvUpload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    Files_data = await file.read()

    # Process the CSV file
    csv_data =  Files_data.decode("utf-8").split("\n")
    csv_reader = csv.reader(csv_data)

    # Skip the header row
    header = next(csv_reader)

    # Insert data into the database
    for row in csv_reader:
        if row:
            name, age = row
            user = Userdata(Name=name, Age=int(age))
            db.add(user)
    db.commit()

    return {"filename": file.filename}










