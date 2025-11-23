import random
import requests

HOST = "https://qa-internship.avito.com"
SELLER_ID = random.randint(111111, 999999)

def create_payload(seller_id=None, title="Postman Item", description="From Postman", price=1234):
    return {
        "sellerId": seller_id or SELLER_ID,
        "title": title,
        "description": description,
        "price": price
    }

def test_01_create_item_success():
    payload = create_payload()
    r = requests.post(f"{HOST}/api/1/item", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "itemId" in data
    global ITEM_ID
    ITEM_ID = data["itemId"]

def test_02_create_duplicate_payload():
    payload = create_payload()
    r1 = requests.post(f"{HOST}/api/1/item", json=payload)
    r2 = requests.post(f"{HOST}/api/1/item", json=payload)
    assert r1.status_code == 200
    assert r2.status_code == 200
    id1 = r1.json()["itemId"]
    id2 = r2.json()["itemId"]
    assert id1 != id2

def test_03_create_empty_title():
    payload = create_payload(title="")
    r = requests.post(f"{HOST}/api/1/item", json=payload)
    assert r.status_code == 400

def test_04_create_zero_price():
    payload = create_payload(price=0)
    r = requests.post(f"{HOST}/api/1/item", json=payload)
    assert r.status_code == 400

def test_05_create_bad_seller_id():
    payload = create_payload(seller_id="abc")
    r = requests.post(f"{HOST}/api/1/item", json=payload)
    assert r.status_code == 400

def test_06_get_item_valid():
    r = requests.get(f"{HOST}/api/1/item/{ITEM_ID}")
    assert r.status_code == 200
    data = r.json()
    assert data["itemId"] == ITEM_ID

def test_07_get_item_invalid_id_type():
    r = requests.get(f"{HOST}/api/1/item/not-an-id")
    assert r.status_code == 400

def test_08_get_item_nonexistent():
    r = requests.get(f"{HOST}/api/1/item/999999999999")
    assert r.status_code == 404

def test_09_get_items_by_seller():
    r = requests.get(f"{HOST}/api/1/items", params={"sellerId": SELLER_ID})
    assert r.status_code == 200
    arr = r.json()
    assert isinstance(arr, list)
    assert any(item["itemId"] == ITEM_ID for item in arr)

def test_10_get_items_by_seller_no_items():
    new_seller = random.randint(111111, 999999)
    r = requests.get(f"{HOST}/api/1/items", params={"sellerId": new_seller})
    assert r.status_code == 200
    assert r.json() == []

def test_11_get_items_by_seller_invalid_type():
    r = requests.get(f"{HOST}/api/1/items", params={"sellerId": "bad"})
    assert r.status_code == 400

def test_12_get_stat_valid():
    r = requests.get(f"{HOST}/api/1/stat/{ITEM_ID}")
    assert r.status_code == 200
    stats = r.json()
    assert "views" in stats and "contacts" in stats
    assert stats["views"] >= 0
    assert stats["contacts"] >= 0

def test_13_get_stat_nonexistent():
    r = requests.get(f"{HOST}/api/1/stat/9999999999")
    assert r.status_code == 404

def test_14_get_stat_invalid_id():
    r = requests.get(f"{HOST}/api/1/stat/invalid")
    assert r.status_code == 400
