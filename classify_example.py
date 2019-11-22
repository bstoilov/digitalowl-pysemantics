from pysemantics.NlpClient import NlpClient


# all classification work best with larger texts, if an article has too few words, it might not be enough to pick up the context from that
# if you need to deal with short few word phrases you should use 'analyse_sentance' method
def classify_url_example():
    target_urls = [
        'https://en.wikipedia.org/wiki/2020_United_States_presidential_election',
        'https://pinchofyum.com/freezer-meals',
        'https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array',
        'https://www.digitaltrends.com/cars/best-cars/',
        'https://www.cnbc.com/2019/11/22/us-china-economic-conflict-could-be-worse-than-wwi-henry-kissinger-says.html'
    ]

    client = NlpClient()

    # the api will classify url based entierly on the web page contents
    # all of the urls are downloaded, meaningful text is extracted and that is what is fed to the algorithm
    for url in target_urls:
        classification = client.classify(input=url)
        print('url:{} -> {}'.format(url, classification))
    # Output
    # url: https://en.wikipedia.org/wiki/2020_United_States_presidential_election -> {'tags': ['politics', 'law'], 'originalTags': ['2012 democratic national convention']}
    # url: https://pinchofyum.com/freezer-meals -> {'tags': ['food'], 'originalTags': ['easy recipes', 'cooking']}
    # url: https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array -> {'tags': ['software', 'language'], 'originalTags': ['ansi c', 'c++ (programming language)', 'c (programming language)']}
    # url: https://www.digitaltrends.com/cars/best-cars/ -> {'tags': ['vehicles', 'retail'], 'originalTags': ['sport utility vehicles (suvs)', 'car buying', 'cars and automobiles']}
    # url: https://www.cnbc.com/2019/11/22/us-china-economic-conflict-could-be-worse-than-wwi-henry-kissinger-says.html -> {'tags': ['politics', 'law', 'war'], 'originalTags': ['foreign policy', 'foreign policy of india', 'indian army']}

    # in the response you will notice two results for each url
    # original_tags -> the algorithm choses from a huge set of user defined tags (around 120k) and picks the ones that are most applicable according to the word vectors
    # these tags are often too concrete to be true

    # tags object -> these are tags obtained by 'generalizing' the original tags, for example in this case 'c++ (programming language)', 'c (programming language)'
    # both belons to the more general 'software' tag and 'easy recipes', 'cooking' both belong to food and so on


def classify_text_example():
    # some text about car reviews
    text = ' '.join(open('resources/classify_text_in', "r+").readlines())

    # the idea here is the same as with classify__url_example, just the download and extract text step is skipped.
    # if you already have the text documents available this will be a lot faster
    client = NlpClient()
    result = client.classify(input=text)
    print(result)
    # OUTPUT:
    # {'tags': ['vehicles', 'media'], 'originalTags': ['cars and automobiles', 'survey question']}

# classify_url_example()
# classify_text_example()
