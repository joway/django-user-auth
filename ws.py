# Set Django Environment
import os
from wsrequest import WebSocketRequest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")


message = '{"method": "GET", "url": "/api/projects/"}'
request = WebSocketRequest(message)
response = request.get_response()

print(response.content)