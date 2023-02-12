<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="data/logo.png" alt="Logo" width="80" height="80">
  </a>

<h1 align="center"> &#9997; Literature Review Made Easy &#9997; </h1>


Welcome to this comprehensive literature review report, generated with the help of an advanced program that saves you time and effort. This report provides a summary of the latest research on a specific topic, using the latest available data collected through the Springer Nature API.
</div>

## Generating a Literature Review with Springer Nature API and Python

Are you tired of manually searching for relevant research papers for your literature review? Look no further! With the help of the Springer Nature API and Python, you can easily generate a literature review in just a few steps.

## How it works
The program makes use of the Springer Nature API to retrieve information about academic papers that match the given keywords and year. It then generates a markdown file that displays the relevant papers with all their attributes, such as the authors, title, abstract, and more.
you can see the example document generated [here](./final_paper.md)
## Getting Started

1. Clone the repository containing the program from Github.
2. Make sure you have a Springer Nature API key. You can apply for one [here](https://dev.springernature.com/).
3. Open your terminal or command prompt and navigate to the cloned repository.
4. Run the program by typing the following command:

This program takes in three important inputs:

1. Springer Nature API key
2. Year of publication
3. Keywords related to your research area

The API key allows you to access the vast repository of papers available on the Springer Nature platform. The year of publication and keywords help you narrow down your search to find only the most relevant papers.

To use this program, you first need to clone the Git repository where the program is uploaded. This can easily be done by opening up the Windows terminal and running the following command:
```python

git clone https://github.com/[user-name]/[repo-name].git
```
Once you have cloned the repository, navigate to the directory where the program is stored and run the following command:

```python
springer_nature_API.py -y [YEAR] -a [API_KEY] [KEYWORDs]
```
Example use case:
```
springer_nature_API.py -y 2022 -a 1231231581sds23810231 deep animal ethology
```

The program will then start executing and will generate a markdown file with all the relevant papers. Each paper is displayed with its title, authors, publication year, and a link to the original paper (which is shown in the paper logo). The program also indicates if a paper is open access or not.

With this program, you can now save hours of time and effort in conducting a literature review. The output file can be easily converted into a beautiful and professional-looking document with the help of a markdown rendering tool such as pandoc or markdown-pdf.


This repository is inspired by [Cat Papers](https://github.com/junyanz/CatPapers) with some code borrowed from [Lan Fei Liu](https://github.com/lanfeiliu/SpringerAPI-ElsevierAPI_LiteratureReviewTable).

<h1 align="center"> 👀 Follow me 👀 </h1>

<div align="center">
Find out about what i am currently working on
<br>
<br>
  <strong><a href="https://github.com/snawarhussain">Github - </a></strong>
  <strong><a href="https://www.instagram.com/snawar_hussain/">Instagram</a></strong>


<h1 align="center"> ️🤝 Collaborations are Welcome 🤝 </h1>

</div>
