# **OklamAI**
_Training a Neural Network on Kendrick Lamar's lyricism._

This project has three aims:

1. Scraping the internet for Kendrick Lamar's lyrics. 
2. Creating a RNN which is trained on these lyrics.

    and (Optional) 
3. Creating a twitter bot which routinely spews out new KDot lyrics.


**Note** For obvious reasons, the dataset contains profanity. I haven't made an attempt to editorialize. 


## **Part 1: Generating the Data**
I'm not aware of any text dataset which condenses all of Kendrick Lamar's verses. Before any RNN can be made, I need to collect all of his works into a single txt file. To keep things simple (and avoid any deviation from his lyrical style), I'm avoiding any of his features in other artists' songs. His oeuvre is considerably smaller than someone like, say, Jay-Z and it is still to be seen if the smaller size of the text corpus will result in poor  generalization. However, other artists' features in his songs will be kept. My assumption is that the features still adhere to lyrical themes and the rhythmic schemes of the whole song. 

* I'm not going to mention the websites I've scraped to obtain the text corpus. I haven't bothered to check if the websites I've used allow scraping.

* `text.py` provides a class `Song` which takes the form of lyrics. Lyrics for a specific song can be obtained by passing in the name of the song as a string. Make sure that the name is exact, down to the punctuation.
* `text.py` provides a class `Corpus` which creates the text corpus from a local store and divides it into sentences.

* The final text corpus contains 10454 lines 

**The text corpus used to train the network is located at `OklamAI/corpus/lyrics/KDOT.txt`**


**Notes:**
1. `OklamAI/corpus/lyrics/lyric_pages` contains the plain text files of all relevant songs. The name of the file is the title of the song.  
2. While my script _works_ per se, my IP address gets blocked after a few requests in a row. 
3. A solution is to use a rotating proxy that allocates a new IP address from a set of proxies stored in a proxy pool.
4. In the obtained set of proxies, some work and others don't depending on the protocol used by it. I've used a `try / except` clause to catch those that are relevant. Eventually, the file will have to be updated to a new batch of proxies.
   
## **Part 2: Creating a Word level RNN**
As rap lyrics have meaning dictated by specific structure and context, a word level RNN might be better at understanding and generating this kind of text.


Steps to be taken:

1. Importing the text data: This step also needs to remove puncutation from the text.
2. Vectorizing word characters into integers: In 
3. Batch and prefetch data
4. Building a RNN Model 
5. Training the RNN Model
6. Evaluating performance
7. Obtaining the next characters. 


### **2.1 Vectorizing the text corpus**
* The dataset consists of a large vocabulary. One hot encoding in this case would result in a sparse dataset with very high dimensionality. As an alternative, word embeddings would be a representation of the semantics of a word, efficiently encoding semantic information that might be relecant to the task at hand. 

* One hot encoding might be a decent ad hoc solution, but I intend to replace it with a better alternative.