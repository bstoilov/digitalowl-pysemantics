import requests
import json
from sklearn.cluster import KMeans
from scipy import spatial
import numpy as np

COMMON_HEADERS = {'content-type': 'application/json'}


class NlpClient:
    def __init__(self, base_url='https://digitalowl.org/api/'):
        self.base_url = base_url

    def classify(self, input=''):
        data = {
            'input': input
        }

        return requests.post(self.base_url + 'classify/topic', headers=COMMON_HEADERS, data=json.dumps(data)).json()

    def similarity(self, first='', second=''):
        data = {
            'first': first,
            'second': second,
            'lang': 'en'
        }

        return requests.post(self.base_url + 'classify/similarity', headers=COMMON_HEADERS,
                             data=json.dumps(data)).json()

    def analyse_sentance(self, sentence):
        data = {
            'positive': sentence.split(' '),
            'negative': [],
            'lang': 'en'
        }

        return requests.post(self.base_url + 'wv/eval', headers=COMMON_HEADERS,
                             data=json.dumps(data)).json()

    def _obtain_vectors(self, sentences):
        data = {"sentances": sentences}
        res = requests.post(self.base_url + '/wv/vectors', headers=COMMON_HEADERS, data=json.dumps(data)).json()
        return res['vectors']

    def clusters(self, sentences, cluster_count):
        vectors = self._obtain_vectors(sentences)

        i = 0
        while i < len(vectors):
            if vectors[i] is None:
                sentences.pop(i)
                vectors.pop(i)
            i += 1

        X = np.array(vectors)
        kmeans = KMeans(n_clusters=cluster_count, random_state=0).fit(X)
        line_count = len(sentences)
        result = []
        i = 0
        while i < line_count:
            cluster = kmeans.labels_[i]
            result.append({'cluster': str(cluster), 'sentence': sentences[i]})
            i += 1
        return result

    def belong(self, group, targets, sim_factor):
        group_vectors = self._obtain_vectors(group)
        target_vectors = self._obtain_vectors(targets)
        belonging = []
        i = 0
        while i < len(target_vectors):
            target_vec = target_vectors[i]

            if target_vec is not None:
                j = 0
                while j < len(group_vectors):
                    cosine_dist = spatial.distance.cosine(target_vec, group_vectors[j])
                    sim = 1 - cosine_dist
                    if sim >= sim_factor:
                        belonging.append(targets[i])
                        break
                    j += 1
            i += 1

        return belonging
