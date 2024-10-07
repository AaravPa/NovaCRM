from functools import wraps
from time import time
import logging

logger = logging.getLogger(__name__)

def measure_performance(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time()
        result = await func(*args, **kwargs)
        elapsed = time() - start
        logger.info(f"{func.__name__} took {elapsed:.3f}s")
        
        if elapsed > 1.0:
            logger.warning(f"Slow query: {func.__name__} ({elapsed:.3f}s)")
        
        return result
    
    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        logger.info(f"{func.__name__} took {elapsed:.3f}s")
        
        if elapsed > 1.0:
            logger.warning(f"Slow operation: {func.__name__} ({elapsed:.3f}s)")
        
        return result
    
    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
