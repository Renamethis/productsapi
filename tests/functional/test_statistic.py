from datetime import datetime, timedelta
def test_statistic(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": 151
        }
    ])
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": 251
        }
    ])
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": 321
        },
    ])
    now = datetime.now()
    dateStart = (now - timedelta(minutes=30)).isoformat()
    dateEnd = (now + timedelta(minutes=30)).isoformat()
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a334/statistic?dateStart=" + dateStart + "&dateEnd=" + dateEnd)
    assert response.status_code == 200
    assert len(response.json) == 3
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a334")

def test_invalid_statistic(client):
    response = client.get('/nodes/3fa85f64-5717-4562-b3fc-2c963f66a334/statistic?dateStart=5&dateEnd=6')
    assert response.status_code == 400
    now = datetime.now()
    dateStart = (now - timedelta(minutes=30)).isoformat()
    dateEnd = (now + timedelta(minutes=30)).isoformat()
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a335/statistic?dateStart=" + dateStart + "&dateEnd=" + dateEnd)
    assert response.status_code == 404