import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_daily_recipe(client):
    """test get daily recipe"""
    response = client.get('/daily')
    assert response.status_code == 200
    data = response.get_json()
    assert 'recipe' in data
    assert 'id' in data


def test_recommend_with_ingredients(client):
    """test recommend with ingredients"""
    response = client.post('/recommend', json={'ingredients': ['egg', 'tomato', 'oil', 'salt']})
    assert response.status_code == 200
    data = response.get_json()
    assert 'recipes' in data
    # should recommend Tomato Scrambled Eggs
    assert any(r['name'] == 'Tomato Scrambled Eggs' for r in data['recipes'])


def test_recommend_no_match(client):
    """test recommend no match ingredients"""
    response = client.post('/recommend', json={'ingredients': ['poo']})
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['recipes']) == 0


def test_get_recipe_exists(client):
    """test get existing recipe"""
    response = client.get('/recipe/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Tomato Scrambled Eggs'
    assert 'ingredients' in data


def test_get_recipe_not_found(client):
    """test get non-existing recipe"""
    response = client.get('/recipe/999')
    assert response.status_code == 404
