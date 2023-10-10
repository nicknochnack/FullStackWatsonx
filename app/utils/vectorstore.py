import chromadb
import uuid
from pypdf import PdfReader
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from typing import Any 


class VectorStore(BaseModel): 
    chunk_size: int = 1000
    chunk_overlap: int = 200 
    embedding_model: str = 'sentence-transformers/all-MiniLM-L12-v2'

    collection_name: str = 'langchain'
    collection: Any 

    def __init__(self, file_path, persist_store="assets/whispervectorstore/", **kwargs) -> chromadb.Collection:
        super().__init__(**kwargs)

        client = chromadb.PersistentClient(path=persist_store)
        client.delete_collection(self.collection_name)
        collection = client.create_collection(name=self.collection_name, metadata={"hnsw:space": "cosine"})

        chunks = self.chunk_file(file_path, self.chunk_size, self.chunk_overlap)
        embeddings = self.create_embeddings(chunks)
        ids = [str(uuid.uuid1()) for x in range(len(chunks))]
        collection.add(ids, embeddings.tolist(), documents=chunks)

        self.collection = collection

    def chunk_file(self, file_path, chunk_size, chunk_overlap):
        reader = PdfReader(file_path)
        number_of_pages = len(reader.pages)

        texts = []
        for pageno in range(number_of_pages): 
            page = reader.pages[pageno]
            texts.append(page.extract_text())
        texts = ' '.join(texts)

        chunk_size = 1000
        chunk_overlap = 200

        chunks = [] 
        while len(texts) > 0: 
            if len(texts) < chunk_size: 
                chunks.append(texts)
                texts = ''
            else: 
                chunks.append(texts[0:1000])
                texts = texts[chunk_size-chunk_overlap:]

        return chunks 

    def create_embeddings(self, chunks): 
        model = SentenceTransformer('thenlper/gte-small')
        embeddings = model.encode(chunks)

        return embeddings

    def query(self, prompt): 
        query_embedding = self.create_embeddings(prompt).tolist()
        query_results = self.collection.query(query_embedding, n_results=3)
        return '\n\n '.join(query_results['documents'][0])

