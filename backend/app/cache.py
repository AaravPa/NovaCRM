import redis
import os
import json
from datetime import timedelta
from typing import Any, Optional

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

def cache_get(key: str) -> Optional[Any]:
    try:
        value = redis_client.get(key)
        if value:
            return json.loads(value)
    except Exception as e:
        print(f"Cache get error: {e}")
    return None

def cache_set(key: str, value: Any, ttl: int = 3600):
    try:
        redis_client.setex(
            key,
            ttl,
            json.dumps(value)
        )
    except Exception as e:
        print(f"Cache set error: {e}")

def cache_delete(key: str):
    try:
        redis_client.delete(key)
    except Exception as e:
        print(f"Cache delete error: {e}")

def cache_clear_pattern(pattern: str):
    try:
        keys = redis_client.keys(pattern)
        if keys:
            redis_client.delete(*keys)
    except Exception as e:
        print(f"Cache clear error: {e}")
