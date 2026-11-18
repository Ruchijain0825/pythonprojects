from sentence_transformers import SentenceTransformer
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


model = SentenceTransformer('all-MiniLM-L6-v2')
print('Model loaded. Output embedding size:', model.get_sentence_embedding_dimension())
tickets = [
    "How do I cancel my subscription?",
    "I want to stop being billed every month.",
    "The app crashes when I upload a large file.",
    "Uploading a big video makes the app freeze.",
    "Can I get a refund for last month's payment?",
    "I forgot my password and can't log in.",
    "Reset my password please, I'm locked out.",
    "Does the app support dark mode?",
]

for i, t in enumerate(tickets):
    print(f'{i}: {t}')
    embeddings = model.encode(tickets, convert_to_numpy=True, normalize_embeddings=True)

print('Embeddings shape:', embeddings.shape)  # (num_tickets, embedding_dim)
print('\nFirst embedding (first 10 values shown):')
print(embeddings[0][:10])


tok = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
base_model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

sample = tickets[0]
inputs = tok(sample, return_tensors='pt')
with torch.no_grad():
    output = base_model(**inputs)

token_embeddings = output.last_hidden_state[0]  # (num_tokens, hidden_dim)
print('Tokens:', tok.convert_ids_to_tokens(inputs['input_ids'][0]))
print('Per-token embedding shape:', token_embeddings.shape)
print('After mean-pooling -> single sentence vector of shape:', token_embeddings.mean(dim=0).shape)


coords = PCA(n_components=2, random_state=42).fit_transform(embeddings)

plt.figure(figsize=(8, 6))
plt.scatter(coords[:, 0], coords[:, 1])
for i, t in enumerate(tickets):
    plt.annotate(f'{i}', (coords[i, 0], coords[i, 1]))
plt.title('2D projection of ticket embeddings (PCA)')
plt.xlabel('PC1'); plt.ylabel('PC2')
plt.show()

for i, t in enumerate(tickets):
    print(i, '-', t)