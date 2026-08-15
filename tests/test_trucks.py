def test_get_trucks(client):
    response = client.get('/trucks')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_trucks(client):
    response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST0001",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["truck_no"] == 9999
    assert data["plate"] == "TST0001"
    assert data["vin"] == "1HGBH41JXMN109186"
    assert data["model"] == "Test Truck"
    assert data["available"] == True

def test_get_truck_by_id(client):
    create_response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST0002",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    truck_id = create_response.json()["id"]
    response = client.get(f'/trucks/{truck_id}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_truck_not_found(client):
    response = client.get('/trucks/99999')
    assert response.status_code == 404

def test_delete_truck(client):
    create_response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST0003",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    truck_id = create_response.json()["id"]
    response = client.delete(f'/trucks/{truck_id}')
    assert response.status_code == 200
    assert response.json()["message"] == "Truck deleted"

def test_create_truck_invalid_plate_length(client):
    response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST123456789",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    assert response.status_code == 422

def test_create_truck_plate_uppercased(client):
    response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "tst0004",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["plate"] == "TST0004"

def test_create_truck_duplicate_plate(client):
    response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST0005",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    duplicate_response = client.post('/trucks', json={
        "truck_no": 9999,
        "plate": "TST0005",
        "vin": "1HGBH41JXMN109186",
        "model": "Test Truck",
        "available": True
    })
    assert duplicate_response.status_code == 409