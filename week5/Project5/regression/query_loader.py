import pandas as pd
from .exceptions import QueryError

def load_queries(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        raise QueryError(f"Error reading Excel file: {e}")

def replace_variables(query, variables):
    for key, val in variables.items():
        query = query.replace(f"{{{key}}}", str(val))
    return query
