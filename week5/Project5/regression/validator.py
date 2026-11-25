from .db_utils import run_query

def validate_primary_key(query):
    return {"Validation": "Primary Key", "Result": run_query(query)}

def validate_duplicate_key(query):
    return {"Validation": "Duplicate Key", "Result": run_query(query)}

def validate_count(query):
    return {"Validation": "Count Check", "Result": run_query(query)}
