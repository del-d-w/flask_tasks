import unittest
from app import app
from unittest.mock import patch

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('app.db.session')
    def test_create_item(self, mock_db_session):
        response = self.client.post('/items', json={'name': 'Test Item'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Item created successfully'})
        mock_db_session.add.assert_called_once()
        mock_db_session.commit.assert_called_once()

    @patch('app.Item.query')
    def test_get_item(self, mock_query):
        mock_item = mock_query.get.return_value
        mock_item.id = 1
        mock_item.name = 'Test Item'

        response = self.client.get('/items/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'item_id': 1, 'name': 'Test Item'})
        mock_query.get.assert_called_once_with('1')

    @patch('app.Item.query')
    @patch('app.db.session')
    def test_update_item(self, mock_db_session, mock_query):
        mock_item = mock_query.get.return_value
        mock_item.id = 1
        mock_item.name = 'Test Item'

        response = self.client.put('/items/1', json={'item_id': 1, 'name': 'Test Item Updated'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Item updated successfully'})

        mock_query.get.assert_called_once_with('1')
        mock_db_session.commit.assert_called_once()

    @patch('app.Item.query')
    @patch('app.db.session')
    def test_delete_item(self, mock_db_session, mock_query):
        mock_item = mock_query.get.return_value
        mock_item.id = 1
        mock_item.name = 'Test Item'

        response = self.client.delete('/items/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Item deleted successfully'})

        mock_query.get.assert_called_once_with('1')
        mock_db_session.delete.assert_called_once_with(mock_item)
        mock_db_session.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
