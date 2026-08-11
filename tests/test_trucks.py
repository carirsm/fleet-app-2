from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_trucks():
    response = client.get('/trucks')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_trucks():
    response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "ABC1234",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["truck_no"] == 9999
    assert data["plate"] == "ABC1234"
    assert data["vin"] == "1HGBH41JXMN109186"
    assert data["model"] == "Test Truck"
    assert data["available"] == True

def test_get_truck_by_id():
    create_response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "ABC1234",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    truck_id = create_response.json()["id"]
    response = client.get(f'/trucks/{truck_id}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_truck_not_found():
    response = client.get('/trucks/99999')
    assert response.status_code == 404

def test_delete_truck():
    create_response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "ABC1234",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    truck_id = create_response.json()["id"]
    response = client.delete(f'/trucks/{truck_id}')
    assert response.status_code == 200
    assert response.json()["message"] == "Truck deleted"
