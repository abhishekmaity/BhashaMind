import redis
import json
import os

r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def cache_summary(key, value=None):
    if value:
        r.set(key, json.dumps(value), ex=3600)
    else:
        data = r.get(key)
        return json.loads(data) if data else None
