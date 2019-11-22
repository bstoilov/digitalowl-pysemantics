from pysemantics.NlpClient import NlpClient
from random import shuffle

def example_clusters():
    # the idea is to automatically group phrases (words in this case) into
    # into previously specified number of groups, by the meaning of each phrase
    # For this we will use sentence vectors from digitalowl.org and the KMEans algorithm from sklearn

    # in this example we will chose 3 groups of objects, namely vechicles, vegetables and sport
    cluster_count = 3
    vegetables = ['greens', 'leaves', 'asparagus', 'stems', 'beans', 'seeds', 'beetroot', 'broccoli', 'flowers',
                  'brussels', 'cabbages', 'capsicums', 'carrots', 'cauliflower', 'celeriac', 'celery', 'chilli',
                  'peppers', 'chokos', 'cucumber', 'eggplant']

    vehicles = ['engine', 'wheels', 'car', 'truck', 'tires', 'gasoline', 'fuel']

    sport = ['tennis', 'football', 'cricket', 'chess', 'baseball', 'swimming']

    # merge and shuffle the data into one single array
    all = vegetables + vehicles + sport
    shuffle(all)

    # the client will help us process the vectors, but you can directly call '_obtain_vectors' and use other method
    # the clusters function uses kmeans to build 3 groups of data out of the data we provided
    client = NlpClient()
    cluster_data = client.clusters(sentences=all, cluster_count=cluster_count)

    for cluster_id in cluster_data:
        print('Cluster {} - {}'.format(cluster_id, cluster_data[cluster_id]))


    # OUTPUT:
    # Cluster 2 - ['greens', 'cucumber', 'peppers', 'capsicums', 'beetroot', 'cauliflower', 'cabbages', 'chilli', 'stems', 'seeds', 'celeriac', 'flowers', 'leaves', 'beans', 'asparagus', 'broccoli', 'celery', 'brussels', 'carrots','eggplant']
    # Cluster 1 - ['tennis', 'baseball', 'football', 'swimming', 'chess', 'cricket']
    # Cluster 0 - ['wheels', 'engine', 'tires', 'fuel', 'car', 'truck', 'gasoline']

    # we can see that we obtained the initial arrays, the word 'chokos' is missing from the vegetables group
    # this is because it is not recognized by the digitalowl.org api, it simply wasn't mentioned in its training data
    # so this word is ignored.

example_clusters()