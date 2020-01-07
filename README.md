[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15Un9BXO6CBonPoJ5uQFpBfgpD5qk2hRz)

# Simple Wikipedia Dataset Topic Extraction 
Ryan Arnouk

**Natural Language Processing LDA model designed to extract topics trained on 70, 000 articles from Simple Wikipedia.**

Work and research can be found in `Wikipedia_Dataset_Topic_extraction.ipynb`

Parsing file can be found in `parse.py`

Pickled model can be found in `model.pkl`

## Expirementing
Using 1000 topics can be found in the `1000 topics testing` folder. 

## Latent Dirichlet Allocation (LDA) in Topic Modelling
### Explanation
In natural language processing (NLP) latent Dirichlet allocation is a generative statistical model. This means the model can extract topics in an unlabeled dataset by frequency and distribution of words, to extract topics. 

LDA assumes all the words in a document are related and tries to figure out how each document could have been created. We need to just tell the model how many topics to construct to generate topic and word distributions over a corpus. Using this can allow us to identify similar documents within the corpus. 

Meaning, LDA Is useful for finding accurate mixtures of topics within a document. 

When using LDA you would choose a fixed number of topics (k) to discover from the dataset. In my case, I chose 200 to represent all the topics from the Simple Wikipedia Dataset. 

### Assumptions
- Documents with similar topics will use similar groups of words
- Document definitions/modeling: 
  - Documents are probability distributions over latent topics
  - Topics are probability distributions over words. 

Instead of focusing purely on frequency of words in a topic LDA focuses also on the distribution between words accross topics.  


### Plate Notation
A simple way to visually represent all the dependencies in the models parameters: 

![Plate Notation](https://upload.wikimedia.org/wikipedia/commons/d/d3/Latent_Dirichlet_allocation.svg)

By Bkkbrad - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=3610403


M represents total number of documents within corpus 

N denotes number of words in a document

Outside parameters: 
Dirchilet priors
- α = the parameter of the Dirichlet prior on the per-document topic distributions
    - High alpha denotes higher likelihood that each document is going to contain a mixture of the documents. 
    - Low alphas suggest that each document will only contain 1 or 2 topics
- β = is the parameter of the Dirichlet prior on the per-topic word distribution
    - High beta means each topic will contain a mixture of most of the words
    - Low beta means each topic will only contain a mixture of a few words.      
- Theta: Topic distribution for the document 
- z notates each topic, making each document a mixture of these topics. 
- w stands for word 

<img src="https://miro.medium.com/max/800/1*_NdnljMqi8L2_lAYwH3JDQ.gif" alt="Dirichlet Distribution" width="500px" height="500px"/>

1000 samples from a Dirichlet distribution using an increasing alpha value.

### How LDA Works
**LDA Works Backwards**

LDA runs in reverse, by starting with a corpus of documents and generating topics. In order to understand how LDA assumes the documents topics it is important to understand the generative process: 

LDA assumes documents are created in the same way: 
1. Determine number of words in document
2. Choose a topic mixture for the document over a fixed set of topics (k)
  a. Topic A: 20%
  b. Topic B: 20%
  c. Topic C: 60%
3. Generate topics in a document by: 
  a. First pick a topic a document in the topic distribution above. 
  b. Pick a word based on the topic distribution. 

Since we have a corpus of documents, we want LDA to learn the topic representation of K topics in each document and the word distribution of each topic. 

LDA **backtracks** from the document level to identify topics that have likely generated the corpus. 

Steps: 
- Randomly assign each word in each document to one of the K topics. 
- For each document d: 
  - Assume all the topic assignments except the current one are correct
  - Calculate two proportions: 
    - Proportion of words in document d that are currently assigned to topic t 
    - Proportion of assignments to topic t over all documents that come from this word. 

  - Multiply the two proportions and assign w a new topic based on that probability. 
- Eventually a state would be reached where assignments make sense. 

### LDA Pros vs Cons

Pros: 
- Has been shown to produce good results over main domains
- Effective, easy to understand tool. 

Cons: 
- Must know the number of topics K in advance (something that I struggled with in this project creating my own dataset) I would be forced to estimate a good number of topics for my needs. 
- Topic distribution cannot capture correlations among topics which makes it hard for me to group topics together as one. For example, linked lists and arrays are hard for me to group as simple computer science. 
- In my experience, it is a very tedious process discovering the optimal number of topics. There is not a very good explanation on the best way to determine the number of topics.  


### Topic Modelling vs Topic Classification
**Or LDA vs Neural Network** 

Difference between **identify one topic vs classify one topic**

Originally, when working on this project I was under the impression I would use text classification and a neural network. However, I soon realized that this would be ineffective, based on the fact that despite having a define set of topic I would want to have returned I would not have any idea of the input text. Since I would have no idea what text or what subject the text inputted into the model would be, it would make more sense for me to try and extract the topic from any text instead of trying to classify an endless text from an endless amount of topics. If I was developing my model to be more niche in one subject, a neural network would definitely help improve my accuracy. 

Sources: 

https://www.youtube.com/watch?v=DWJYZq_fQ2A

https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation

https://www.quora.com/Latent-Dirichlet-Allocation-LDA-What-is-the-best-way-to-determine-k-number-of-topics-in-topic-modeling

https://datascience.stackexchange.com/questions/962/what-is-difference-between-text-classification-and-topic-models


## Import Dataset
In my case, I am importing a Simple Wikipedia Dataset I already preprocessed from the XML file dump Wikipedia has publicly available. Parsing code available in *parse.py*

## Preprocessing 
The steps we need to do to preprocess our data is as follows: 

- Tokenization: 
  - Words with less than 3 characters must be removed. (Helps clear random words that may provide noise in the classifier)
- All stop words are removed: Stop words are commonly used words like the, a, an, in that the classifier needs to be programmed to ignore to help keep noise levels in the classifier minimal. 
- Capitalization: Lowercase all the data
- Stemming: Remove suffixes from words. 
- Lemmatization: Words in third person are changed to first person and verbs in past and future tenses are changed to present. 
- Vectorization: Convert words to vectors. Machine Learning can only read numbers so we must translate it to numbers. 
  - Types of vectorization includes: 
    - Bag of words (the technology used in this project) 
    - TFIDF
    - Word2Vec
    - GloVe

### Vectorization 
**Bag of Words** 
Now we are able to vectorize the data: Vectorization is converting the words to numbers. 

Bag-of-words is a representation of text that describes the occurence of words in a document. Containing the following: 
1. A vocabulary of known words. 
2. A measure of the presence of known words. 

It is called *bag* of words because information about order or structure is discarded and the model is simply concerned whether words occur in the document and not where in the document. 


https://machinelearningmastery.com/gentle-introduction-bag-words-model/

## Model
Below, we execute the LDA on our corpus. 

First, we assign `bow_corpus` to the bag of words version of the document. This step converts the document which is a list of words into bag of words. 

### Running the Model
Parameters of `gensim.models.LdaMulticode`

bow_corpus = bag of words docs file

num_topics = the number of topics we want to get from our corpus. 

id2word = dictionary created above

passes = number of passes through corpus during training 

iterations = max number of iterations through the corpus when inferring topic 
distribution of a corpus 

workers = number of worker processed to be used for parallelization

More information can be found here: 
https://radimrehurek.com/gensim/models/ldamulticore.html

Load into a pickle file to cache model and not need to rerun every time seperatly. 

**Selecting Parameters:**
In my case I was limited in time to really expirement with tweaking all of the parameters, in the future instead of choosing something random and expirementing quickly to see what worked the best I will try and graph my results in order to see the best parameters that give me the most accurate results. Passing in an unseen document to the classifier and having no conclusive way to get the optimal number of topics really makes it a pain to tweak the parameters and becomes a game of trial and error. I ended up making this classifier with 350 topics and `model2.pkl` with 1000 topics and I am looking into expirementing with them to see what is more effective. 

Testing with 1000 topics expirement can be found in `/1000 topics testing`