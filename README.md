# DigitalOwl NlpClient
Python client, that utilizes the [digitalowl.org](https://digitalowl.org) NLP API.

Take advantage of some of the modern NLP techniques in easy, fast and acessible way. Most of the time you won't need more than 10 lines of code to integrate this into your pipeline.

**The API is free for use**
## Install using pip
```pip install pysemantics```



## So what can it do?

#### With few words, this is a script/client that can be used to perform semantic analysis of text, or in order words analyse the text's meaning.

## Functionalities

### Text classification

Classify text or url into set of user defined categories.

**`client.classify(input='https://en.wikipedia.org/wiki/2020_United_States_presidential_election')`**

Output: 

    {'tags': ['politics', 'law'], 'originalTags': ['2012 democratic national convention']}

The url is downloaded, meaningful text is extracted and classified, if you alredy have the text available, you can directly pass it as input.

Full working code, with more explanations: [classify_example.py](https://github.com/bstoilov/digitalowl-pysemantics/blob/master/classify_example.py)


### Phrase/Word analysis

The underlying logic is based on NLP model called Word2Vec, if given the right training training data, it can start picking up contextual relations between words.
Meaning words that are used often together, or are used in similar way, are close by contextual meaning (contextual synonyms). 

**`client.analyse_sentence(sentence='apricot')`**

Output:

      {'pistachio': 0.7594164609909058, 'overripe': 0.7523329257965088, 'mango': 0.7421437501907349,
      'peach': 0.7410970330238342, 'rhubarb': 0.7401571273803711, 'pecan': 0.7379646897315979,
      'persimmon': 0.7368103265762329, 'strawberry': 0.731874942779541, 'unripe': 0.7294522523880005,
      'sorbet': 0.7278781533241272, 'walnut': 0.7244322299957275, 'tart': 0.7223066687583923,
      'beetroot': 0.7216348648071289, 'okra': 0.7172538042068481, 'pumpkin': 0.7165997624397278,
      'pineapple': 0.7146158814430237, 'lemongrass': 0.7138402462005615, 'papaya': 0.7137945294380188,
      'blueberry': 0.7127506136894226, 'marmalade': 0.7100027799606323}

The words that are close to apricot are other fruits and foods, these relations can be used in various NLP tasks.
Similar relations can be extracted for whole paragraphs full working code with more explanations: 
[analyse_sentence_example.py](https://github.com/bstoilov/digitalowl-pysemantics/blob/master/analyse_sentence_example.py)



### Semantic Similarity

Given two documents, words or just phrases, you can compare to what degree they are close by meaning.

`first = 'https://en.wikipedia.org/wiki/Impeachment_inquiry_against_Donald_Trump'`

`second = 'https://news.sky.com/story/ex-trump-adviser-fiona-hill-says-russia-gearing-up-to-interfere-in-2020-election-11866422'
`

`client.similarity(first=first, second=second)`

    {'similarity': 0.9516085802597031}

Full working example with documentation: [similarity_example.py](https://github.com/bstoilov/digitalowl-pysemantics/blob/master/similarity_example.py)

### Text Clusters

Automatically group documents, words or sentences.

Using the vectors we obtain from the API and the KMeans algorithm integrated into this client
we can group pieces of text or documents based on their meaning.

Full working example can be found here: [data_cluster_example.py](https://github.com/bstoilov/digitalowl-pysemantics/blob/master/data_cluster_example.py)


### Belong to group check

Using the client you are able to define a group of objects and then determine if certain object belongs to that group

define some group of animals:

`group = ['cat', 'dog', 'fox', 'horse', 'rhino']`

pick some random words, some of which are animals:

`targets = ['carrot', 'animal', 'monkey', 'ship', 'Canada', 'buffalo', 'crow', 'news', 'government', 'murder', 'chariot']`

`client.belong(group=group, targets=targets)`

Output: 

    ['animal', 'monkey', 'buffalo', 'crow', 'chariot']

Full working example: [groups_example.py](https://github.com/bstoilov/digitalowl-pysemantics/blob/master/groups_example.py)



##### In case you find any issues, please report them as issue. Any feedback is welcome, don't hesitate to contact me at borislav.stoilov@digitalowl.org


