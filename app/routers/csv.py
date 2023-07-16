from fastapi import status, HTTPException, Depends, APIRouter, UploadFile, File 
from sqlalchemy.orm import Session 
import csv 
import models, schemas 
from typing import List 
from database import get_db 
 
router = APIRouter( 
    tags=['CSV'] 
) 
 
@router.post("/upload-data") 
async def upload_data(file: UploadFile = File(...), db: Session = Depends(get_db)): 
    try: 
        if file.content_type != "text/csv": 
            return {"message": "Invalid file format. Please upload a CSV file."} 
 
        # Read the file data synchronously 
        csv_data = file.file.read().decode('utf-8') 
 
        csv_reader = csv.DictReader(csv_data.splitlines(), delimiter=',') 
 
        for row in csv_reader: 
            stock = models.Stock(**row) 
            db.add(stock) 
 
        db.commit() 
        
 
        return {"message": "Data uploaded successfully"} 
    except Exception as e: 
        db.rollback() 
        return {"message": f"An error occurred: {str(e)}"} 
 
@router.get("/get-data", response_model=List[schemas.StockOut]) 
def get_data(db: Session = Depends(get_db)): 
    stocks = db.query(models.Stock).all() 
    return stocks