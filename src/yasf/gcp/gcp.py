import json

from flask import Response
from ..models import GenericContext


def parse_args(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    event = {}
    if request_json:
        event['body'] = request_json
    if request_args:
        event['arguments'] = request_args

    event['path'] = request.path[1:]

    return event, GenericContext(event_id=None, raw_context=request)


def format_output(output: dict):
    body = output['body']
    status_code = output['statusCode']

    if isinstance(body, list):
        body = json.dumps(body)
        return Response(body, mimetype='application/json', status=status_code)

    return body, status_code
