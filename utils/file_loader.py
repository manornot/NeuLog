import yaml

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
        return yaml.safe_load(file)