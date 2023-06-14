# Pinecone client Python helper

This project aims to enhance the Python Pinecone client by providing a collection of simple and reusable functions. These functions include error handling and some extra verbosity to give an idea of what is going on. With this approach, the project ensures that graceful error messages are displayed when an issue arises.

 > Find the complete reference on [Pinecone's docs](https://docs.pinecone.io/docs/python-client#reference).

 ## Quickstart

 Clone this repository:

 ```sh
 git clone https://github.com/soos3d/pinecone-client-helper-python.git
 ```

 Install the Pinecone Python client and python-dotenv packages.

 ```sh
 pip install pinecone-client python-dotenv
 ```

 Add your Pinecone API key and environment to the `.env.sample` file and rename `.env`

 ```env
 # Pinecone config
PINECONE_API_KEY="YOUR_API_KEY"
PINECONE_ENVIRONMENT="us-west1-gcp-free" # Your environment
INDEX_DIMENSION="1536"  # This is the dimension for the OpenAI embedding model text-embedding-ada-002
INDEX_METRIC="cosine"
```

The file has a `main` function to test a few endpoints.

```sh
python3 pinecone_client.py
```

You will get a similar response.

```sh
[]
Creating index named test...
Index test created.
['test']
Deleting test index...
test deleted
```

> Please note that these functions have yet to be deeply tested, and it's only meant to be a helper. Feel free to contribute!

## Usage

To use these functions in your project, import the file at the top and include the environment variables.

```py
import os
import pinecone_client

from dotenv import load_dotenv
load_dotenv()

# Init API key, environment, and dimentions
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
INDEX_DIMENSION = os.getenv('INDEX_DIMENSION')
INDEX_METRIC = os.getenv('INDEX_METRIC')

# Initialize Pinecone
pinecone_client.pinecone_init(PINECONE_API_KEY, PINECONE_ENVIRONMENT)

# Create an index
index_name = 'my-index'
pinecone_client.create_index(index_name, int(INDEX_DIMENSION), INDEX_METRIC)
```

Or only import the functions you need.

```py
import os
from pinecone_client import pinecone_init, create_index

from dotenv import load_dotenv
load_dotenv()

# Init API key, environment, and dimentions
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
INDEX_DIMENSION = os.getenv('INDEX_DIMENSION')
INDEX_METRIC = os.getenv('INDEX_METRIC')

# Initialize Pinecone
pinecone_init(PINECONE_API_KEY, PINECONE_ENVIRONMENT)

# Create an index
index_name = 'my-index'
create_index(index_name, int(INDEX_DIMENSION), INDEX_METRIC)
```

> Note that you must pass the index dimension as `int` if you use environment variables.