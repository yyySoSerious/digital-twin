from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)
openai = OpenAI()

vector_store = openai.vector_stores.create(
    name="digital_twin_knowledge_base"
)

knowledge_dir= Path("src/knowledge_base")
for file_path in knowledge_dir.iterdir():
    if file_path.name.startswith("."):
        continue
    
    if file_path.is_file():
        print(f"Uploading {file_path.name} to vector store...")

        file = openai.files.create(
            file=open(file_path, "rb"),
            purpose="assistants"
        )

        result = openai.vector_stores.files.create_and_poll(
            vector_store_id=vector_store.id,
            file_id=file.id
        )

        print(f"{file_path.name}: {result.status}")

print("Vector store ID:", vector_store.id)