# **OklamAI**
_Training a Neural Network on Kendrick Lamar's lyricism._

This project has three aims:

    1. Scraping the internet for Kendrick Lamar's lyrics. 
    2. Creating a RNN which is trained on these lyrics.
    (Optional) 3. Creating a twitter bot which routinely spews out new KDot lyrics.


**Note** For obvious reasons, the dataset contains profanity. I haven't made an attempt to edit it. 



## **Part 1: Generating a Text Corpus**
I'm not aware of any text dataset which condenses all of Kendrick Lamar's verses. Before any RNN can be made, I need to collect all of his works into a single txt file. To keep things simple (and avoid any deviation from his lyrical style), I'm avoiding any of his features in other artists' songs. His oeuvre is considerably smaller than someone like, say, Jay-Z and it is stil to be seen if the smaller size of the text corpus will result in poor  generalization. 

_Note: I'm not going to mention the websites I've scraped to obtain the text corpus. I haven't bothered to check if the websites I've used allow scraping._



## **Appendix: Notes**

1. \<!DOCTYPE html\>: HTML documents must start with a type declaration
2. HTML documents are contained between \<html\> and \</html\> 
3. The visible part of a HTML document is between \<body\> and \</body\>
4. HTML headings are defined with the \<h1\> to \<h6\> tags. 
5. I've used  the XPath to locate the desired text from a webpage
6. lyrics are contanied in `list(div_1)[17].text`


