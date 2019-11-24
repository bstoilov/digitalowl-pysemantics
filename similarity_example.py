from pysemantics.NlpClient import NlpClient


def similarity_example():
    # first and second can be two urls, two texts, or one url and one text
    first = 'https://en.wikipedia.org/wiki/Impeachment_inquiry_against_Donald_Trump'
    second = 'https://news.sky.com/story/ex-trump-adviser-fiona-hill-says-russia-gearing-up-to-interfere-in-2020-election-11866422'

    client = NlpClient()
    similarity = client.similarity(first=first, second=second)

    print(similarity)

    # Output:
    # {'similarity': 0.9516085802597031}

    # two different articles, writen by different authors, but they are about the same topic
    # we don't compare syntactic similarity here, we compare semantic similarity
    # the meaning of both text is quite similar, in fact everything with similarity more
    # than 0.6 is quite similar


similarity_example()
