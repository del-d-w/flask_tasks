**Installing Requirements**

pip install flask

pip install flask_sqlalchemy

pip install pytest

pip install pytest-mock

**Running all test cases with pytest**

python -m pytest -v 

**Running individual test cases with pytest**

python -m pytest -v -k test_create_item

python -m pytest -v -k test_get_item 

python -m pytest -v -k test_update_item

python -m pytest -v -k test_delete_item
