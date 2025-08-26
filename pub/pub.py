from sklearn.datasets import fetch_20newsgroups


class pub:
    def __init__(self):
        self.interesting_categories = ['alt.atheism',
                                       'comp.graphics',
                                       'comp.os.ms-windows.misc',
                                       'comp.sys.ibm.pc.hardware',
                                       'comp.sys.mac.hardware',
                                       'comp.windows.x',
                                       'misc.forsale',
                                       'rec.autos',
                                       'rec.motorcycles',
                                       'rec.sport.baseball']

        self.not_interesting_categories = ['rec.sport.hockey',
                                           'sci.crypt',
                                           'sci.electronics',
                                           'sci.med',
                                           'sci.space',
                                           'soc.religion.christian',
                                           'talk.politics.guns',
                                           'talk.politics.mideast',
                                           'talk.politics.misc',
                                           'talk.religion.misc']

        self.newsgroups_interesting = self.get_one_message_per_category(self.interesting_categories)
        self.newsgroups_not_interesting = self.get_one_message_per_category(self.not_interesting_categories)

    def get_one_message_per_category(self,categories):
        messages = {}
        for cat in categories:
            newsgroup = fetch_20newsgroups(subset='all', categories=[cat])
            if newsgroup.data:
                messages[cat] = newsgroup.data[0]
        return messages

    def get_interesting(self):
        return self.newsgroups_interesting

    def get_not_interesting(self):
        return self.newsgroups_not_interesting
