from functools import lru_cache

from yaml import safe_load

from ansible_collections.arista.avd.plugins.plugin_utils.schema.default_schemas import DEFAULT_SCHEMAS


@lru_cache
def create_store():
    store = {}
    for id, schema_file in DEFAULT_SCHEMAS.items():
        with open(schema_file, "r", encoding="UTF-8") as file:
            schema_file_data = safe_load(file.read())
            store[id] = schema_file_data

    return store
