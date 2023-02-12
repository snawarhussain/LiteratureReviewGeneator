import pandas as pd
import os
import ast


class Paper:
    def __init__(self, data):
        self.OA = 'No'
        self.source = None
        self.url = None
        self.title = 'cat'
        self.year = 1900
        self.PublicationName = None
        self.openaccess = None
        self.authors = None
        self.doi = None
        self.abstract = None
        self.keywords = None
        self.data = data

    # def Paper_Content(self):
    #     self.PublicationName = None
    #     self.openaccess = None
    #     self.authors = None
    #     self.df = df
    #     self.doi = None
    #     self.abstract = None
    #     self.keywords = None
    #     self.title =None

    def kWord(self):
        kw = self.data['keyword']
        string = kw.strip("[]").replace("'", "").replace(",", "")
        words = string.split()
        self.keywords = ", ".join(words)

    def tt(self):
        title = self.data['title']
        string = title.strip("[]").replace("'", "").replace(",", "")
        words = string.split()
        self.title = " ".join(words)

    def abs(self):
        abstract = self.data['abstract']
        string = abstract.strip("[]").replace("\\", "'\\\\'").replace(",", "")
        words = string.split()
        self.abstract = " ".join(words)

    def yr(self):
        date = self.data['publicationDate']
        year = date.split('-')
        self.year = year[0]

    def authrs(self):
        authors = self.data['creators']
        list_of_dicts = ast.literal_eval(authors)
        creators = [d['creator'] for d in list_of_dicts if 'creator' in d]
        self.authors = " ".join(creators[0:2])
        # self.authors = creators[0:2]

    def link(self):
        url = self.data['url']
        list_of_dicts = ast.literal_eval(url)
        url = list_of_dicts[0]['value']
        self.url = url
        # self.authors = creators[0:2]
    def PN(self):
        source = self.data['publicationName']

        self.source = source
        # self.authors = creators[0:2]

    def Oa(self):
        oaflag = self.data['openaccess']
        if oaflag:
            self.OA = 'Yes'


    def parsedPaper(self):
        self.kWord()
        self.tt()
        self.abs()
        self.yr()
        self.authrs()
        self.link()
        self.PN()
        self.Oa()

    def to_dict(self):
        dict_ = {'title': self.title,
                 'keyword': self.keywords,
                 'authors': self.authors,
                 'year': self.year,
                 'abstract': self.abstract,
                 'url': self.url,
                 'source': self.source,
                 'OA': self.OA
                 }
        return dict_


#
# #
# if __name__ == '__main__':
#     df = pd.read_csv('data.csv')
#     for column, row in df.iterrows():
#         paper = Paper(row)
#         paper.parsedPaper()
#         parsed = paper.to_dict()
#
#         print(parsed)
