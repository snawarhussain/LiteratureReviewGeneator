## Introduction
As a researcher, you may find it difficult to keep track of the latest research developments in your field. To help you in your research, I have created a literature review program that can be used to generate a summary of relevant papers from the Springer Nature API.

## Getting Started
To use this program, you will need to have a Springer Nature API key. You can get an API key by signing up for a free account on the Springer Nature Developer Portal (https://dev.springernature.com/signup).

Next, clone the git repository where you have uploaded the program to your local machine. You can do this by running the following command in the Windows terminal:

```python

git clone https://github.com/snawarhussain/LiteratureReviewGeneator

```

Running the Program
To run the program, navigate to the directory where the program is located and run the following command:
```python
springer_nature_API.py -y [YEAR] -a [API_KEY] [KEYWORDs]
```

Replace [YOUR_API_KEY] with your actual Springer Nature API key, [YEAR] with the year of the papers you are interested in, and [KEYWORDS] with a comma-separated list of keywords related to your research. For example:

```
springer_nature_API.py -y 2022 -a 1231231581sds23810231 deep animal ethology
```


## Output
The program will generate a Markdown file with a summary of the relevant papers, including the paper title, authors, abstract, and a link to the original paper. If the paper is open access, this will also be indicated.

## Implementing from Scratch

If you are interested in implementing this program from scratch, here are the general steps you need to follow:

Register on the Springer Nature website to obtain an API key.

Use the requests library to send a GET request to the Springer Nature API with your API key and the specified search parameters (year range and keywords).

Parse the JSON response to extract the relevant information for each paper, such as title, authors, publication year, and open-access status.

Use the jinja2 library to create a markdown template that can be populated with the extracted information.

Use the render() function to render the template and generate the final markdown file.

With these steps in mind, you can easily create your own Literature Review Automation program and save yourself time and effort in conducting literature reviews.


## Conclusion
This literature review program can help you save time and stay up-to-date with the latest research developments in your field. By providing a summary of relevant papers, you can quickly assess the current state of research and identify areas for future exploration.