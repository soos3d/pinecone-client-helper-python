import os
import pinecone
from dotenv import load_dotenv

# Initialize Pinecone with your API key and project environment
def pinecone_init(api_key, environment):
    try:
        pinecone.init(api_key=api_key, environment=environment)
    except Exception as e:
        print(f'An error occurred during initialization: {e}')

# Create an index with a specified name, dimension, and optional metadata configuration
def create_index(index_name, dimension, metric, metadata_config=None):
    try:
        print(f'Creating index named {index_name}...')
        pinecone.create_index(index_name, dimension, metric=metric, metadata_config=metadata_config)
        print(f'Index {index_name} created.')
    except Exception as e:
        print(f'An error occurred while creating the index {index_name}: {e}')

# Return a list [] of all indexes in the current project
def list_indexes():
    try:
        return pinecone.list_indexes()
    except Exception as e:
        print(f'An error occurred while listing indexes: {e}')

# Return information about a specified index
def describe_index(index_name):
    try:
        return pinecone.describe_index(index_name)
    except Exception as e:
        print(f'An error occurred while describing the index {index_name}: {e}')

# Delete an index
def delete_index(index_name):
    try:
        print(f'Deleting {index_name} index...')
        pinecone.delete_index(index_name)
        print(f'{index_name} deleted')
    except Exception as e:
        print(f'An error occurred while deleting {index_name}: {e}')

# Change the number of replicas for a specified index
def scale_replicas(index_name, new_number_of_replicas):
    try:
        pinecone.configure_index(index_name, replicas=new_number_of_replicas)
    except Exception as e:
        print(f'An error occurred while scaling replicas for {index_name}: {e}')

# Return statistics about a specified index
def describe_index_stats(index_name):
    try:
        index = pinecone.Index(index_name)
        return index.describe_index_stats()
    except Exception as e:
        print(f'An error occurred while getting statistics for the index {index_name}: {e}')

# Insert or update (upsert) vectors in a specified index
def upsert_vectors(index_name, vectors, namespace):
    try:
        print('Upserting vectors...')
        index = pinecone.Index(index_name)
        return index.upsert(vectors=vectors, namespace=namespace)
    except Exception as e:
        print(f'An error occurred while upserting vectors to {index_name}: {e}')

# Query a specified index with metadata filtering
def query_index(index_name, namespace, top_k, include_values, include_metadata, vector, filter):
    try:
        index = pinecone.Index(index_name)
        return index.query(
            namespace=namespace,
            top_k=top_k,
            include_values=include_values,
            include_metadata=include_metadata,
            vector=vector,
            filter=filter
        )
    except Exception as e:
        print(f'An error occurred while querying the index {index_name}: {e}')

# Delete vectors by ID from a specified index
def delete_vectors(index_name, ids, namespace):
    try:
        print('Deleting vectors...')
        index = pinecone.Index(index_name)
        return index.delete(ids=ids, namespace=namespace)
    except Exception as e:
        print(f'An error occurred while deleting vectors from {index_name}: {e}')

# Fetch vectors by ID from a specified index
def fetch_vectors(index_name, ids, namespace):
    try:
        index = pinecone.Index(index_name)
        return index.fetch(ids=ids, namespace=namespace)
    except Exception as e:
        print(f'An error occurred while fetching vectors from {index_name}: {e}')

# Update vectors by ID in a specified index
def update_vectors(index_name, id, values, set_metadata, namespace):
    try:
        print('Updating Vectors...')
        index = pinecone.Index(index_name)
        return index.update(
            id=id,
            values=values,
            set_metadata=set_metadata,
            namespace=namespace
        )
    except Exception as e:
        print(f'An error occurred while updating vectors in {index_name}: {e}')

# Create a collection from an existing index
def create_collection(collection_name, index_name):
    try:
        print(f'Creating {collection_name} collection...')
        pinecone.create_collection(collection_name, index_name)
        print('Collection created.')
    except Exception as e:
        print(f'An error occurred while creating collection {collection_name} from {index_name}: {e}')

# Return a list of all collections in the current project
def list_collections():
    try:
        return pinecone.list_collections()
    except Exception as e:
        print(f'An error occurred while listing collections: {e}')

# Return information about a specified collection
def describe_collection(collection_name):
    try:
        return pinecone.describe_collection(collection_name)
    except Exception as e:
        print(f'An error occurred while describing the collection {collection_name}: {e}')

# Delete a specified collection
def delete_collection(collection_name):
    try:
        print(f'Deleting collection {collection_name}...')
        pinecone.delete_collection(collection_name)
        print('Collection deleted.')
    except Exception as e:
        print(f'An error occurred while deleting the collection {collection_name}: {e}')

def main():

    load_dotenv()  # take environment variables from .env.

    # Init API key, environment, and dimentions
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
    INDEX_DIMENSION = os.getenv('INDEX_DIMENSION')
    INDEX_METRIC = os.getenv('INDEX_METRIC')

    # Init Pinecone client
    pinecone_init(PINECONE_API_KEY, PINECONE_ENVIRONMENT)

    # List indexes
    indexes_list = list_indexes()
    print(indexes_list)

    # Create a new index 
    index_name = "test"
    create_index(index_name, int(INDEX_DIMENSION), INDEX_METRIC)

    # List indexes again
    indexes_list = list_indexes()
    print(indexes_list)

    # Describe the index
    info = describe_index(index_name)
    print(info)

    # Delete the new index
    delete_index(index_name)

if __name__ == "__main__":
    main()