import pydantic_core

def jsonModelValidate(jsonDatasetMetadata, allow_partial=True):
    return pydantic_core.from_json(jsonDatasetMetadata, allow_partial=allow_partial)