from pysemantics.NlpClient import NlpClient
import requests
import json

test_data = 'test'

data = open(test_data, 'r')
data = data.readlines()

sentances = []

for s in data:
    sentances.append(s.replace('\n', ''))

client = NlpClient()

group = sentances

targets = ['topinambur', 'squashes', 'acorn', 'squash', 'bitter melon', 'butternut', 'banana']

belonging = client.belong(group=group, targets=targets, sim_factor=0.4)


print(belonging)
