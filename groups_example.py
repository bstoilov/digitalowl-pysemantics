from pysemantics.NlpClient import NlpClient


def belongs_to_group_example():
    # We define a group of words or sentence and then check which of the targets belong to the group
    # Each word from target is compared to the words in group if there is
    # pair that is similar enough the target is included in the result
    group = ['cat', 'dog', 'fox', 'horse', 'rhino']
    targets = ['carrot', 'animal', 'monkey', 'ship', 'canada', 'buffalo', 'crow', 'news', 'government', 'murder',
               'chariot']

    client = NlpClient()
    # belonging is the array of items that belong to the specified group
    # you can pass sim_factor arg to control the similarity of items, it can range from 0 to 1
    # 0 meaning 'nothing in common', 1 meaning 'exactly the same', default is 0,5
    belonging = client.belong(group=group, targets=targets)

    print(belonging)
    # OUTPUT:
    # ['animal', 'monkey', 'buffalo', 'crow', 'chariot']

    # In a sense we defined a group that can recognize animals, we see that anything that is not an animal is excluded
    # NOTE: don't expect accurate results at all times because the algorithm relies on contextual similarity
    # for example if we add 'chariot' to the targets we will see it in the result because the phrase 'horse chariot' is very common


belongs_to_group_example()
