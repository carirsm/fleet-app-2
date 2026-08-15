def test_get_drivers(client):
    response = client.get('/drivers')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_drivers(client):
    response = client.post('/drivers', json={
        "driver_no": 9999,
        "first_name": "First",
        "last_name": "Last",
        "is_hazmat": True,
        "is_tanker": True,
        "is_doubles": True,
        "is_triples": True,
        "available": True,
        "shift": "day"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["driver_no"] == 9999
    assert data["first_name"] == "First"
    assert data["last_name"] == "Last"
    assert data["is_hazmat"] == True
    assert data["is_tanker"] == True
    assert data["is_doubles"] == True
    assert data["is_triples"] == True
    assert data["available"] == True
    assert data["shift"] == "day"

def test_get_driver_by_id(client):
    create_response = client.post('/drivers', json={
        "driver_no": 9999,
        "first_name": "First",
        "last_name": "Last",
        "is_hazmat": True,
        "is_tanker": True,
        "is_doubles": True,
        "is_triples": True,
        "available": True,
        "shift": "day"
    })
    driver_id = create_response.json()["id"]
    response = client.get(f'/drivers/{driver_id}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_driver_not_found(client):
    response = client.get('/drivers/99999')
    assert response.status_code == 404

def test_delete_driver(client):
    create_response = client.post('/drivers', json={
        "driver_no": 9999,
        "first_name": "First",
        "last_name": "Last",
        "is_hazmat": True,
        "is_tanker": True,
        "is_doubles": True,
        "is_triples": True,
        "available": True,
        "shift": "day"
    })
    driver_id = create_response.json()["id"]
    response = client.delete(f'/drivers/{driver_id}')
    assert response.status_code == 200
    assert response.json()["message"] == "Driver deleted"