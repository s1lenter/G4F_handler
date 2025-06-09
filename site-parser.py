import requests
import json

response = requests.get(
  url="https://openrouter.ai/api/v1/auth/key",
  headers={
    "Authorization": f"Bearer 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"
  }
)

print(json.dumps(response.json(), indent=2))
