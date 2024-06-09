import numpy as np
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from pycocotools.coco import COCO


def encode_caption(caption, model):
    vector = np.mean([model.wv[token] for token in tokens if token in model.wv], axis=0)
    return vector

#use if error
'''import nltk
nltk.download('punkt')'''

annotation_file = 'annotations/captions_train2017.json'

coco = COCO(annotation_file)

image_ids = coco.getImgIds()

tokenized_captions = []

for image_id in image_ids:
    annotations = coco.loadAnns(coco.getAnnIds(imgIds=image_id))
    for annotation in annotations:
        caption_text = annotation['caption']
        tokens = word_tokenize(caption_text.lower())
        tokenized_captions.append(tokens)

model = Word2Vec(tokenized_captions, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec_model.model")
loaded_model = Word2Vec.load("word2vec_model.model")

'''encoded_captions = [encode_caption(caption, model) for caption in tokenized_captions[:10]]

for i, encoded_caption in enumerate(encoded_captions):
    print(f"Кодированное описание {i + 1}:", encoded_caption)'''
print(tokenized_captions[:10])
