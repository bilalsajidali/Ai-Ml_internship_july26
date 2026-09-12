from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Load the embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# Embed three sentences
v1 = embed_model.get_text_embedding("I love cats")
v2 = embed_model.get_text_embedding("I adore cats")
v3 = embed_model.get_text_embedding("Pakistan won the match")

# Print first 5 numbers of each vector
print("I love cats:          ", v1[:5])
print("I adore cats:         ", v2[:5])
print("Pakistan won the match:", v3[:5])

# Print total size
print("\nTotal numbers per sentence:", len(v1))


# Convert to numpy arrays
v1 = np.array(v1).reshape(1, -1)
v2 = np.array(v2).reshape(1, -1)
v3 = np.array(v3).reshape(1, -1)

# Compare
print("\nSimilarity scores:")
print("'I love cats' vs 'I adore cats':          ", round(cosine_similarity(v1, v2)[0][0], 4))
print("'I love cats' vs 'Pakistan won the match':", round(cosine_similarity(v1, v3)[0][0], 4))