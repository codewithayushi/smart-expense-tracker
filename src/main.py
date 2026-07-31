from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json
import os

app = FastAPI(title="Smart Expense Tracker API")

DATA_FILE = "expenses.json"

# Model for Expense
class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: str

# Helper function to load data
def load_data() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Helper function to save data
def save_data(data: List[dict]):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.post("/expenses", status_code=201)
def add_expense(expense: Expense):
    expenses = load_data()
    if any(e["id"] == expense.id for e in expenses):
        raise HTTPException(status_code=400, detail="Expense with this ID already exists")
    expenses.append(expense.dict())
    save_data(expenses)
    return {"message": "Expense added successfully", "expense": expense}

@app.get("/expenses", response_model=List[Expense])
def get_expenses(category: Optional[str] = None):
    expenses = load_data()
    if category:
        expenses = [e for e in expenses if e["category"].lower() == category.lower()]
    return expenses

@app.get("/expenses/total")
def get_total_expenses(category: Optional[str] = None):
    expenses = load_data()
    if category:
        filtered = [e for e in expenses if e["category"].lower() == category.lower()]
        total = sum(e["amount"] for e in filtered)
        return {"category": category, "total": total}
    
    overall_total = sum(e["amount"] for e in expenses)
    category_totals = {}
    for e in expenses:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]
        
    return {"overall_total": overall_total, "category_totals": category_totals}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_data()
    new_expenses = [e for e in expenses if e["id"] != expense_id]
    if len(new_expenses) == len(expenses):
        raise HTTPException(status_code=404, detail="Expense not found")
    save_data(new_expenses)
    return {"message": "Expense deleted successfully"}

