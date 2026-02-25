You need to install these dependencies
  langchain \
  langchain-community \
  langchain-openai \
  langchain-chroma \
  chromadb \
  python-dotenv \
  pypdf 

you can create a requirements.txt file and put all these. After that run uv add -r requirements.txt or pin install -r requirements.txt

In your .env file, provide the following

 OPENAI_API_KEY=your_openai_key
 CHROMA_TENANT=your_tenant_id
 CHROMA_DATABASE=your_database_name
 CHROMA_API_KEY=your_chroma_api_key
 
You can open Chromadb website to create a db, then you will find all these information