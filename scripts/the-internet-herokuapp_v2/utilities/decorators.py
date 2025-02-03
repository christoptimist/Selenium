from selenium.common.exceptions import StaleElementReferenceException
from functools import wraps
import logging

def retry_on_stale_element(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = kwargs.get("logger", None) or args[2] if len(args) > 2 else logging.getLogger(__name__)
            """
                Retry the function if a Stale Element Reference Exception is raised
            """
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException:
                    logger.error(f"Stale element reference exception on attempt {attempt + 1}")
                    if attempt == max_retries - 1:
                        logger.error("Max retries reached, raising exception")
                        raise
                return func(*args, **kwargs)
            return wrapper
        return decorator