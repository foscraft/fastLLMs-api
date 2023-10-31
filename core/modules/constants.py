from chromadb.config import Settings

from .config import get_env_variable

# Define the folder for storing database
PERSIST_DIRECTORY = get_env_variable("PERSIST_DIRECTORY")

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=PERSIST_DIRECTORY,
    anonymized_telemetry=False,
)
