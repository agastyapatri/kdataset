# **OklamAI**
_Training a Neural Network on Kendrick Lamar's lyricism._

This project has three aims:

1. Scraping the internet for Kendrick Lamar's lyrics. 
2. Creating a RNN which is trained on these lyrics.

    and (Optional) 
3. Creating a twitter bot which routinely spews out new KDot lyrics.


**Note** For obvious reasons, the dataset contains profanity. I haven't made an attempt to editorialize. 


## **Part 1: Generating the Data**
I'm not aware of any text dataset which condenses all of Kendrick Lamar's verses. Before any RNN can be made, I need to collect all of his works into a single txt file. To keep things simple (and avoid any deviation from his lyrical style), I'm avoiding any of his features in other artists' songs. His oeuvre is considerably smaller than someone like, say, Jay-Z and it is still to be seen if the smaller size of the text corpus will result in poor  generalization. 

* I'm not going to mention the websites I've scraped to obtain the text corpus. I haven't bothered to check if the websites I've used allow scraping.

* `song.py` provides a class `Song` which takes the form of lyrics. Lyrics for a specific song can be obtained by passing in the name of the song as a string. Make sure that the name is exact, down to the punctuation.

**The text corpus used to train the network is located at `OklamAI/corpus/lyrics/KDOT.txt`**


**Notes:**
1. `OklamAI/corpus/lyrics/lyric_pages` contains the plain text files of all relevant songs. The name of the file is the title of the song.  
2. While my script _works_ per se, my IP address gets blocked after a few requests in a row. 
3. A solution is to use a rotating proxy that allocates a new IP address from a set of proxies stored in a proxy pool.
4. In the obtained set of proxies, some work and others don't depending on the protocol used by it. I've used a `try / except` clause to catch those that are relevant.
   
## **Part 2: Creating a Chararcter level RNN**
Andrej Karpathy has an excellent blog post where he creates a Chararcter Level RNN and trains it on a dataset of Shakespeare's works.



