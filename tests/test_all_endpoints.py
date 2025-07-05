import pytest
from httpx import AsyncClient
from fastapi import status
from main import app

import asyncio

@pytest.mark.asyncio
async def test_create_and_get_machine():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/machines", json={"name": "E-beam Evaporator", "description": "Metal deposition"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "E-beam Evaporator"
        machine_id = data["id"]

        response = await ac.get("/machines")
        assert response.status_code == status.HTTP_200_OK
        machines = response.json()
        assert any(m["id"] == machine_id for m in machines)

@pytest.mark.asyncio
async def test_create_and_get_cleanroom():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/cleanrooms", json={"name": "NanoLab", "description": "Main cleanroom"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "NanoLab"
        cleanroom_id = data["id"]

        response = await ac.get("/cleanrooms")
        assert response.status_code == status.HTTP_200_OK
        cleanrooms = response.json()
        assert any(c["id"] == cleanroom_id for c in cleanrooms)

@pytest.mark.asyncio
async def test_create_and_get_step():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/steps", json={"name": "Bake", "description": "Bake at 200C", "temperature": 200})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Bake"
        step_id = data["id"]

        response = await ac.get("/steps")
        assert response.status_code == status.HTTP_200_OK
        steps = response.json()
        assert any(s["id"] == step_id for s in steps)

@pytest.mark.asyncio
async def test_create_and_get_process_step():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/process-steps", json={"name": "Lithography", "description": "Photoresist patterning"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Lithography"
        process_step_id = data["id"]

        response = await ac.get("/process-steps")
        assert response.status_code == status.HTTP_200_OK
        process_steps = response.json()
        assert any(p["id"] == process_step_id for p in process_steps)

@pytest.mark.asyncio
async def test_create_and_get_recipe():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/recipes", json={"name": "Basic Process", "description": "Test recipe"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Basic Process"
        recipe_id = data["id"]

        response = await ac.get("/recipes")
        assert response.status_code == status.HTTP_200_OK
        recipes = response.json()
        assert any(r["id"] == recipe_id for r in recipes)
