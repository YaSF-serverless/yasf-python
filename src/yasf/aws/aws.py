import json
from ..models import GenericContext


def parse_args(event: dict, context):
    context = GenericContext(event_id=context.aws_request_id, raw_context=context)

    body = event.get("body", {})
    if type(body) == str:
        body = json.loads(body)

    standard_event = {
        "body": body,
    }

    standard_event['arguments'] = event.get('queryStringParameters', {})
    standard_event['pathParameters'] = event.get('pathParameters', {})
    standard_event['path'] = event.get('rawPath', '/')[1:]

    return standard_event, context


def format_output(output: dict):
    return output
