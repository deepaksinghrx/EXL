from fastapi import FastAPI
import uvicorn
 
app = FastAPI()

patients = [
        {
            "patient_id": 1,
            "age": 45,
            "gender": "Male",
            "diagnosis": "Diabetes",
            "treatment": "Insulin",
            "outcome": "Improved"
        },
        {
            "patient_id": 2,
            "age": 60,
            "gender": "Female",
            "diagnosis": "Hypertension",
            "treatment": "ACE Inhibitors",
            "outcome": "Stable"
        }
]

# class Patientsmodel:
#         id = int
#         age = int
#         gender = str

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/patients")
def get_patients():
    return patients

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["patient_id"] == patient_id:
            return patient
    return {"error": "Patient not found"}

@app.post("/add_patients")
def add_patient(patient: dict):
    try:
        patient_id = max(p["patient_id"] for p in patients) + 1
    except ValueError:
        patient_id = 1
    patient["patient_id"] = patient_id
    
    patients.append(patient)
    return {"message": "Patient added successfully", "patient": patient}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8080)