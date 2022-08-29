
### Important Links

#### Imae Embeddings

Article: Image Embeddings
- https://rom1504.medium.com/image-embeddings-ed1b194d113e

Article: Learning Computer Vision
- https://towardsdatascience.com/learning-computer-vision-41398ad9941f

Article: Introduction Feature Detection
- https://medium.com/@deepanshut041/introduction-to-feature-detection-and-matching-65e27179885d

Dataset: Flowers (from Ternsor Flow)
- https://www.tensorflow.org/datasets/catalog/tf_flowers

#### Setence Embeddings

- https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2
- 

### Work Items

#### WORK-01: Setence Transformation Work
1. Use spacy (lg module for English) and see the word vectors and do vector operations like ‘king’ - ‘man’ + ‘woman’ and see what word comes out
2. Use sentence_transformer (again use big module there like paraphrase-multilingual-mpnet-base-v2
 and generate sentence embeddings/vectors
3. Use cosine_transform function to and find out similar sentences

THEN:
1. Find a image module which can dump image vectors (do survey and let us know)
2. Do similar things as cosine_similiarity of images using multiple images

#### WORK-02: Find Similar Setences

If calculated embeddings/vectors of size 768 for each sentence, take any dataset that has English descriptions (if you don’t find decent one let me know) and then for 200 sentences that you picked 
1. Dump embeddings to a TSV file for all sentences
2. Use google embedding projector to see them on canvas (just UI)
3. See whether you can give similar sentences for each sentence as number (1 is cosine similar to 5, 21, 44 blah). 
4. You can also see Euclidean distance or similarity and try this as well

#### WORK-03: Find Similar Images

KNN, EfficientNet, FAISS, etc. (see Image Embeddings section above for links)

#### WORK-O4: Image Transformation and Generation

Concepts: Diffusion, CLIP, GLIDE, Latent Diffusion, Stable Diffusion, Diffusers

1. https://github.com/openai/CLIP
2. https://github.com/openai/glide-text2im
3. https://github.com/openai/guided-diffusion
4. https://github.com/CompVis/latent-diffusion
5. https://github.com/huggingface/diffusers

And after all that you can try:
https://github.com/CompVis/stable-diffusion this requires key


https://en.wikipedia.org/wiki/Zero-shot_learning
https://en.wikipedia.org/wiki/One-shot_learning
