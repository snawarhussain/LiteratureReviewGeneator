import argparse

import jinja2
import requests
import certifi
import json
import pandas as pd
import os
from paper import Paper

template = """
# Paper List
{% for paper in papers %}
## {{ paper.title }}

- Authors: {{ paper.authors }}
- Year: {{ paper.year }}
### Abstract: 
{{ paper.abstract }}

{% endfor %}
"""
template2 = """
# Collected Papers
{% for paper in papers %}
## {{paper.title}}

<br>
<a ><font size=2.5>{{paper.authors}}</font></a>
<br>
<font size=2.5>In {{paper.source}} {{paper.year}} </font>
<br><a href="{{paper.url}}"><img src="data/paper.png"></a> 
<a href="https://img.shields.io/badge/OpenAccess-{{paper.OA}}-9cf" align="bottom"><img src="https://img.shields.io/badge/OpenAccess-{{paper.OA}}-9cf"></a>

## Anstract
{{paper.abstract}}

{% endfor %}
"""

def write_papers(papers, header_file=None, end_file=None, TYPE='md'):
    mtd_str = 'write_' + TYPE.lower()
    content = ''
    # add header file
    if header_file and os.path.exists(header_file):
        with open(header_file, 'r') as hfile:
            content = hfile.read()

    content += '\n<br>\n\n'
    if (TYPE == 'md'):
        content += '<table>'
    for paper in papers:
        content = getattr(paper, mtd_str)(content)
    if (TYPE == 'md'):
        content += '</table>'
    content += '\n<br>\n\n'
    content += '\n<br>\n\n'
    if end_file and os.path.exists(end_file):
        with open(end_file, 'r') as efile:
            content += efile.read()

    return content


def search_articles(year, keyword, api_key):
    try:
        url = f'https://api.springernature.com/meta/v2/json?api_key={api_key}&q=keyword{keyword}' \
              f'%20year%3A{year}&s=1&p=10'
        response = requests.get(url, verify=certifi.where())

        if response.status_code == 200:
            data = json.loads(response.text)
            records = data['records']
            return records

        else:
            print(f'Failed to search articles: {response.status_code} {response.text}')
    except requests.exceptions.RequestException as error:
        print(f'An error occurred while searching articles: {error}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for articles on Springer Nature.')
    parser.add_argument('-y', '--year', type=int, help='Year of publication')
    parser.add_argument('-a', '--api-key', type=str, help='Springer Nature API key')
    parser.add_argument('-t', '--type', choices=['md'], help='type of output file (md)', default='md')
    parser.add_argument('-o', '--output', default=None, help='name of the output file')
    parser.add_argument('keywords', type=str, nargs='+', help='insert Keywords to search for')
    args = parser.parse_args()

    keywords_ = " ".join(args.keywords)

    springer_keyword = "%3A" + keywords_.replace(" ", "%20")
    print(springer_keyword)
    results = search_articles(args.year, springer_keyword, args.api_key)
    try:
        if results:
            print(results)
            df = pd.DataFrame(results)

            # save the dataframe to a CSV file
            df.to_csv('data.csv', index=False)

        else:
            print('Article search failed.')
        TYPE = args.type  # html, md
        if not args.output:
            if args.type == 'md':
                args.output = 'README'

        outputFile = f'{args.output}.{args.type}'
        WORK_DIR = 'data/'
        header_file = os.path.join(WORK_DIR, 'header.%s' % TYPE)
        end_file = os.path.join(WORK_DIR, 'end.%s' % TYPE)
        header_file = open("header.md", "r")
        header = header_file.read()
        header_file.close()

        footer_file = open("end.md", "r", encoding='utf-8')
        footer = footer_file.read()
        footer_file.close()

        df = pd.read_csv('data.csv')

        papers = []
        for column, row in df.iterrows():
            paper = Paper(row)
            paper.parsedPaper()
            papers.append(paper.to_dict())

        rendered = jinja2.Template(template2).render(papers=papers )
        rendered = header + rendered + footer
        with open("final_paper.md", "w", encoding="utf-8") as file:
            file.write(rendered)
    except requests.exceptions.RequestException as error:
        print(f'An error occurred while searching articles: {error}')