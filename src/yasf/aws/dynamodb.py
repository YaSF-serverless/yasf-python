import boto3

DYNAMO_DB_RESOURCE = boto3.resource('dynamodb')


def put_item(table_name: str, key: str, item: dict):
    table = DYNAMO_DB_RESOURCE.Table(table_name)
    table.put_item(Item=item)


def delete_item(table_name: str, key_name: str, key_value: str):
    table = DYNAMO_DB_RESOURCE.Table(table_name)
    table.delete_item(Key={key_name: key_value})


def get_item(table_name: str, key_name: str, key_value: str):
    table = DYNAMO_DB_RESOURCE.Table(table_name)
    return table.get_item(Key={key_name: key_value})['Item']


def update_item(table_name: str, key_name: str, key_value: str, item: dict):
    table = DYNAMO_DB_RESOURCE.Table(table_name)
    db_item = table.get_item(Key={key_name: key_value})['Item']
    db_item.update(item)
    table.put_item(Item=db_item)
    return db_item


def list_items(table_name: str):
    table = DYNAMO_DB_RESOURCE.Table(table_name)
    return table.scan()['Items']
