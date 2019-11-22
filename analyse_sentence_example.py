from pysemantics.NlpClient import NlpClient


def contextual_synonyms():
    client = NlpClient()

    word = 'apricot'
    resp = client.analyse_sentence(sentence=word)
    print(resp['words'])
    # {'pistachio': 0.7594164609909058, 'overripe': 0.7523329257965088, 'mango': 0.7421437501907349,
    #  'peach': 0.7410970330238342, 'rhubarb': 0.7401571273803711, 'pecan': 0.7379646897315979,
    #  'persimmon': 0.7368103265762329, 'strawberry': 0.731874942779541, 'unripe': 0.7294522523880005,
    #  'sorbet': 0.7278781533241272, 'walnut': 0.7244322299957275, 'tart': 0.7223066687583923,
    #  'beetroot': 0.7216348648071289, 'okra': 0.7172538042068481, 'pumpkin': 0.7165997624397278,
    #  'pineapple': 0.7146158814430237, 'lemongrass': 0.7138402462005615, 'papaya': 0.7137945294380188,
    #  'blueberry': 0.7127506136894226, 'marmalade': 0.7100027799606323}

    # in the response we see other words that are often used in the same context and in similar way as 'apricot'
    # these are the so called contextual synonyms of 'apricot'


def analyse_sentence_example():
    client = NlpClient()

    sentence = 'Taking your pets to the vet should be made mandatory to all pet owners'
    resp = client.analyse_sentence(sentence=sentence)

    print(resp['words'])
    # output:
    # {'them': 0.5691992044448853, 'you': 0.5044294595718384, 'yours': 0.49882641434669495, 'theirs': 0.49810361862182617,
    #  'they': 0.49736160039901733, 'dog': 0.4872986376285553, 'himher': 0.4866429567337036, 'cats': 0.4748264253139496,
    #  'dogs': 0.47481757402420044, 'puppy': 0.4733749330043793, 'landlord': 0.4688832461833954,
    #  'parent': 0.4664549231529236, 'fleas': 0.4609288275241852, 'spouse': 0.45495110750198364,
    #  'themselves': 0.4534609317779541, 'cat': 0.45328179001808167, 'yourself': 0.4528433084487915,
    #  'insured': 0.45103758573532104, 'YOU': 0.45088881254196167, 'patient': 0.44211727380752563}

    # the output is an attempt to find the words that best describe contextually the sentence
    # this can be used to classify short phrases


# analyse_sentence_example()
# contextual_synonyms()
