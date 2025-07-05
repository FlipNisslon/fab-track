
# Fabrication Engineering API

This project is a FastAPI backend for managing fabrication process recipes, process steps, steps, cleanrooms, machines, substrates, and interfaces for cleanroom fabrication engineering.

## Setup

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Run the FastAPI app**
   ```
   uvicorn main:app --reload
   ```

3. **Access the API**
   - Root endpoint: http://127.0.0.1:8000/
   - Interactive docs: http://127.0.0.1:8000/docs

## Project Structure

- `main.py` – FastAPI app entry point
- `app/models/` – Pydantic models for all entities
- `app/routers/` – API routers for each entity

---

This is a starting point. Extend with authentication, database integration, and a frontend as needed.
