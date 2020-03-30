"""
A collection of all API namespaces provided by the app.

If you want to add more namespaces, you need to provide them inside this sub-module
and add the namespace to the `Api`. Here is an example:

After creating a new file called `new_api.py` with the following simple content:

```python
from flask_restx import Namespace

new_api_namespace = Namespace('New API', description='Any description.')
```

We have to add the new namespace to our `Api` via inserting the following lines into `apis/__init__.py`:

```python
from .new_api import new_api_namespace

api.add_namespace(new_api_namespace, path='/new/')
```

Now, the `New API` can be contacted via `baseurl/new/`
"""
from flask_restx import Api
from .respond import respond_namespace

api = Api(
    version='1.0',
    title='Learning Docker API',
    description='A simple API created by Zadjad Rezai',
)

api.add_namespace(respond_namespace, path='/respond/')
