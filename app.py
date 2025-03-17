import streamlit as st
import os
import openai  # OpenAI API for embeddings
import pinecone  # Pinecone for vector storage
import fitz  # PyMuPDF for PDF text and annotation extraction
import hashlib # Used for generating unique document IDs
import datetime # For timestamp-based naming
import json  # For handling annotation metadata
