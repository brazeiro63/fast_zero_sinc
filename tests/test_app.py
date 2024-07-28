from http import HTTPStatus

from fastapi.testclient import TestClient


def test_read_root_deve_retornar_ok_e_ola_mundo(client: TestClient):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client: TestClient):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client: TestClient):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def teste_update_user(client: TestClient):
    response = client.put(
        '/users/1',
        json={
            'password': 'secret',
            'username': 'alfredo',
            'email': 'alice@example.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'alfredo',
        'email': 'alice@example.com',
        'id': 1,
    }


def teste_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}
