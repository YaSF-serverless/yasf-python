from google.cloud import firestore

FIRESTORE_DB = firestore.Client()


def put_item(table_name: str, key: str, item: dict):
    doc_ref = FIRESTORE_DB.collection(table_name).document(key)
    doc_ref.set(item)


def delete_item(table_name: str, key_name: str, key_value: str):
    doc_ref = FIRESTORE_DB.collection(table_name).document(key_value)
    doc_ref.delete()


def get_item(table_name: str, key_name: str, key_value: str):
    doc_ref = FIRESTORE_DB.collection(table_name).document(key_value)
    return doc_ref.get().to_dict()


def update_item(table_name: str, key_name: str, key_value: str, item: dict):
    doc_ref = FIRESTORE_DB.collection(table_name).document(key_value)
    doc_ref.update(item)
    return doc_ref.get().to_dict()


def list_items(table_name: str):
    collection = FIRESTORE_DB.collection(table_name).stream()
    return [item.to_dict() for item in collection]
