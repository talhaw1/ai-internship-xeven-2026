"""
Configuration Manager System
"""

import json

config = {}


# 🔹 Load Config
def load_config(filename="config.json"):
    global config
    try:
        with open(filename, "r") as file:
            config = json.load(file)
        print("Config loaded successfully.")
    except FileNotFoundError:
        print("Config file not found. Using default config.")
        config = {}


# 🔹 Validate Required Keys
def validate_config():
    required_keys = ["database", "api", "features"]

    for key in required_keys:
        if key not in config:
            print(f"Missing key: {key}")


# 🔹 Get Config Value Safely
def get_config_value(section, key, default=None):
    return config.get(section, {}).get(key, default)


# 🔹 Update Config
def update_config(section, key, value):
    if section not in config:
        config[section] = {}

    config[section][key] = value
    print(f"Updated {section}.{key} = {value}")


# 🔹 Save Config
def save_config(filename="config.json"):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)

    print("Config saved successfully.")


# 🔥 DEMO EXECUTION

load_config()

validate_config()

# Safe access
db_host = get_config_value("database", "host", "127.0.0.1")
print("Database Host:", db_host)

# Update values
update_config("database", "port", 3306)
update_config("features", "enable_signup", True)

# Add new section
update_config("logging", "level", "DEBUG")

# Save changes
save_config()