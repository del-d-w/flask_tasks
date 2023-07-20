import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_create_item(client, mocker):
    # Mock the database session and commit
    mock_db_session = mocker.patch('app.db.session')
    mock_db_commit = mocker.patch('app.db.session.commit')

    response = client.post('/items', json={'name': 'Test Item'})

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Item created successfully'}

    # Verify that the database session and commit were called
    mock_db_session.add.assert_called_once()
    mock_db_commit.assert_called_once()

def test_get_item(client, mocker):
    # Mock the database query
    mock_query = mocker.patch('app.Item.query')
    mock_item = mocker.Mock()
    mock_item.id = 1
    mock_item.name = 'Test Item'
    mock_query.get.return_value = mock_item

    response = client.get('/items/1')

    assert response.status_code == 200
    assert response.get_json() == {'item_id': 1, 'name': 'Test Item'}

def test_update_item(client, mocker):
    # Mock the database query and commit
    mock_query = mocker.patch('app.Item.query')
    mock_item = mocker.Mock()
    mock_item.id = 1
    mock_item.name = 'Test Item'
    mock_query.get.return_value = mock_item

    mock_db_commit = mocker.patch('app.db.session.commit')

    response = client.put('/items/1', json={'item_id': 1, 'name': 'Test Item Updated'})

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Item updated successfully'}

    # Verify that the database query and commit were called
    mock_query.get.assert_called_once_with('1')
    mock_db_commit.assert_called_once()

def test_delete_item(client, mocker):
    # Mock the database query and commit
    mock_query = mocker.patch('app.Item.query')
    mock_item = mocker.Mock()
    mock_item.id = 1
    mock_item.name = 'Test Item'
    mock_query.get.return_value = mock_item

    mock_db_session = mocker.patch('app.db.session')
    
    # Mock the delete operation in the session
    mock_db_session.delete.return_value = None

    response = client.delete('/items/1')

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Item deleted successfully'}

    # Verify that the database query and session methods were called with the expected arguments
    mock_query.get.assert_called_once_with('1')
    mock_db_session.delete.assert_called_once_with(mock_item)
    mock_db_session.commit.assert_called_once()

if __name__ == '__main__':
    pytest.main()
