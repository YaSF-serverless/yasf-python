import importlib
import os

nosqldb_clients = {
    "AWS": ".aws.dynamodb",
    "GCP": ".gcp.firestore"
}

provider = os.getenv('PROVIDER')
client_path = nosqldb_clients[provider]

client = importlib.import_module(client_path, "yasf")
