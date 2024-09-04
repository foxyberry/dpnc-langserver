import os
from dotenv import load_dotenv, dotenv_values


def load_environment_variables(env_path: str = '.env', additional_vars: dict = None):
    """
    Load environment variables from the specified .env file and optionally set additional variables.
    
    Args:
    - env_path (str): The path to the .env file.
    - additional_vars (dict): Additional environment variables to set.
    
    Returns:
    - dict: A dictionary containing the loaded environment variables.
    """
    # Load the environment variables from the file
    env_vars = dotenv_values(env_path)
    
    # Clear existing environment variables that are being reloaded
    for key in env_vars:
        if key in os.environ:
            del os.environ[key]

    # Explicitly reload the .env file
    load_dotenv(env_path)
    
    # Set additional environment variables if provided
    if additional_vars:
        for key, value in additional_vars.items():
            os.environ[key] = value

    return {**env_vars, **(additional_vars or {})}