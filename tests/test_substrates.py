import pytest
from httpx import AsyncClient
from fastapi import status
from main import app

import asyncio

@pytest.mark.asyncio
async def test_create_and_get_substrate():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a substrate
        response = await ac.post("/substrates", json={"material": "Silicon", "description": "Test wafer"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["material"] == "Silicon"
        substrate_id = data["id"]

        # Get all substrates
        response = await ac.get("/substrates")
        assert response.status_code == status.HTTP_200_OK
        substrates = response.json()
        assert any(s["id"] == substrate_id for s in substrates)

@pytest.mark.asyncio
async def test_create_and_get_interface():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create an interface
        response = await ac.post("/interfaces", json={"name": "Si/SiO2", "description": "Silicon to oxide interface"})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Si/SiO2"
        interface_id = data["id"]

        # Get all interfaces
        response = await ac.get("/interfaces")
        assert response.status_code == status.HTTP_200_OK
        interfaces = response.json()
        assert any(i["id"] == interface_id for i in interfaces)
