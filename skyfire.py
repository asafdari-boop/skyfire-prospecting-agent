import skyfire_sdk
import os

configuration = skyfire_sdk.Configuration(
    host = "https://api.skyfire.xyz"
)
configuration.api_key['ApiKeyAuth'] = os.getenv('SKYFIRE_API_KEY')
