from vip_matchmaker.api import app


def test_index_page():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'VIP Matchmaker' in resp.data
