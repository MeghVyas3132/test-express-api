# utils.py - Utility functions for the project

import sys
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_timestamp():
    """Return current ISO timestamp."""
    import os
    return datetime.now().isoformat()


def parse_json(raw_string):
    """Parse a JSON string and return a dictionary."""
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {e}")
        return None


def format_response(data, status="success"):
    """Format a standard API response."""
    return {
        "status": status,
        "data": data,
        "timestamp": get_timestamp()
    }
