"""
embedder_tests.py - Test for embedding service and MongoDB storage.
"""
import os
from dotenv import load_dotenv
from rag.loader import extract_pdf
from rag.embedder import EmbeddingService
from pymongo import MongoClient
from rag.storing_mongodb import storing_mongodb

load_dotenv() 

GEMINI_API_KEY =os.getenv("GOOGLE_API_KEY")

service = EmbeddingService()

"""
mongo_uri = os.getenv("MONGODB_URI")
if not mongo_uri:
    raise ValueError("⚠️ MONGODB_URI not found in environment variables")

mongo_client = MongoClient(mongo_uri)
db = mongo_client["catastrophe_db"]
collection = db["documents"]

print("✅ Connected to MongoDB")

#collection.delete_many({})
documents = ["docs/Acidentes_e_crises.pdf", "docs/af_aldeiasegura_folhetotrip_pt.pdf",
            "docs/anr2019-versãofinal.pdf", "docs/Avaliacao_riscos.pdf",
             "docs/eBook_Praticas-Escolares-de-ERR.pdf", "docs/eBook-Catastrofes-Naturais_cap01.pdf",
             "docs/flyer_o_que_fazer_vf.pdf",
             "docs/gestão-do-risco-de-inundação_documento_apoio_boas_praticas.pdf",
             "docs/i023736.pdf", "docs/i032107.pdf", "docs/nt_05_2020.pdf", "docs/nt_06_2020.pdf"
             "docs/patrimoniomundial.pdf", "docs/PCML_Pontos_de_Encontro_30OUT2024_VF_MCM.pdf",
             "docs/PerigosidadeEstrutural-2020-2030-A3.pdf",
             "docs/reference-guide-for-evacuation-planning-in-case-of-tsunami_anepc.pdf"]

for d in documents:
    storing_mongodb(d, collection=collection)

print("✅ Stored document embeddings into MongoDB")"""
