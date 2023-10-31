# vector_store_setup.py

from langchain.vectorstores import Chroma

from .config import get_env_variable
from .constants import CHROMA_SETTINGS
from .embeddings_setup import setup_embeddings_model


def setup_chroma_vector_store():
    """to handle the setup of the Chroma vector store.
    This will help keep the database-related code organized.
    """
    persist_directory = get_env_variable("PERSIST_DIRECTORY")
    embeddings_model = setup_embeddings_model()
    client_settings = CHROMA_SETTINGS
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings_model,
        client_settings=client_settings,
    )
