import os 
import sys 
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma

# === CONFIGURATION ===
DATA_DIR = "data/"
PERSIST_DIR = "persist"
MODEL_NAME = "gpt-3.5-turbo"  # Change to "gpt-4" if needed
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_api_key_here")  # safer env usage
PERSIST = True  # Toggle for persistence

# === SET OPENAI API KEY ===
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def create_or_load_index():
    if PERSIST and os.path.exists(PERSIST_DIR):
        print("[INFO] Loading existing vectorstore index...")
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=OpenAIEmbeddings())
        return VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        print("[INFO] Creating new vectorstore index from documents...")
        loader = DirectoryLoader(DATA_DIR)
        kwargs = {"persist_directory": PERSIST_DIR} if PERSIST else {}
        return VectorstoreIndexCreator(vectorstore_kwargs=kwargs).from_loaders([loader])


def initialize_chain(index):
    return ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model=MODEL_NAME),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )


def main():
    # Parse initial query if provided
    initial_query = sys.argv[1] if len(sys.argv) > 1 else None
    chat_history = []

    # Build or load index
    index = create_or_load_index()
    chain = initialize_chain(index)

    # Chat loop
    while True:
        query = initial_query or input("\n[You] > ")
        if query.lower() in {"exit", "quit", "q"}:
            print("[System] Exiting chat. Goodbye!")
            break

        try:
            result = chain({"question": query, "chat_history": chat_history})
            response = result["answer"]
            print(f"[GPT] > {response}")
            chat_history.append((query, response))
        except Exception as e:
            print(f"[Error] Something went wrong: {e}")

        initial_query = None  # Clear CLI query after first run


if __name__ == "__main__":
    main()
