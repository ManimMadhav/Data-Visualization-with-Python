""" make sure you got these libraries installed
    or be smart and use Colab """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


df=pd.read_csv("cope.csv")
#print(df)
#create a list of words
text=df['Abstract'].tolist()
# join the list and lowercase all the words
text= " ".join(text).lower()

#create the wordcloud object
wordcloud=WordCloud(stopwords=STOPWORDS,colocations=True).generate(text)
#plot the wordcloud object
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()
