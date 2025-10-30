class AIConfig:
    HUGGINGFACE_API_KEY = "your-api-key"
    OPENAI_API_KEY = "your-api-key"
    ANTHROPIC_API_KEY = "your-api-key"
    
    # Vector store settings
    FAISS_INDEX_PATH = "vectorstores/faiss"
    
    # Model settings
    DEFAULT_LLM_MODEL = "gpt-3.5-turbo"
    DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"