def transform(legacy_data):
    transformed_data = {}
    for key, value in legacy_data.items():
        for char in value:
            transformed_data[char.lower()] = key
        
    return transformed_data
