# validator.py - Input validation utilities

import re

def validate_email(email):
    """Validate an email address format."""
    if not isinstance(email, str):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_username(username):
    """Validate a username (alphanumeric, 3-20 chars)."""
    if not isinstance(username, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))

def validate_port(port):
    """Validate a port number."""
    if not isinstance(port, int):
        return False
    return 1 <= port <= 65535