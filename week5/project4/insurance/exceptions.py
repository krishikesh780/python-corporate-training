class CustomerNotFoundError(Exception):
    """Raised when a customer is not found by policy number"""
    pass

class FileReadError(Exception):
    """Raised when there is an issue reading the file"""
    pass

class FileWriteError(Exception):
    """Raised when there is an issue writing to the file"""
    pass
