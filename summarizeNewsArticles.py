#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:59:43 2021

@author: vincenthall

@source: https://youtu.be/z4DQYprjPSs "Summarize news articles with Machine Learning in Python" by NeuralNine

"""

import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article    

nltk.download('punkt')

url = 'https://theisleofthanetnews.com/2021/01/25/impact-of-covid-forces-sad-closure-of-sandwich-wildlife-park/'
#url = 'https://www.walesonline.co.uk/whats-on/shopping/debenhams-closing-swansea-cardiff-newport-19696076'
#url = 'https://timesofindia.indiatimes.com/entertainment/english/hollywood/news/christopher-nolan-had-an-amazing-experience-in-india/articleshow/80232124.cms'
#url = 'https://www.newscientist.com/article/mg24933170-900-the-superconductor-breakthrough-that-could-mean-an-energy-revolution/'
# url = 'https://www.bbc.co.uk/news/world-55795297'


def summarise():
    """Given a url, this should give a brief summary and sentiment analysis. """
    
    print("urltext: "); print(urltext)
    url = urltext.get('1.0', 'end').strip() 
    
    # url = url.replace('"', '')  # Doesn't work :-(
         
    article = Article(url)
    
    article.download()
    article.parse()
    article.nlp()
    
    
    # Let the algorithm change these fields.
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    sumry.config(state='normal')
    sentiment.config(state='normal')

    
    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    # print("\n\n***** Authors")
    # print(article.authors)
    # print("******\n\n")
    author.insert('1.0',article.authors)
    
    
    # print("\n\n***** publish date before deletion:")
    # print(article.publish_date)
    # print("******\n\n")
    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)

    sumry.delete('1.0','end')
    sumry.insert('1.0',article.summary)
    
    analysis = TextBlob(article.text)
    # analysis = TextBlob("Your face is ugly.") 
    # print("/n/n ******** I'm entering my own text! article is commented out! ********/n/n/n/")
    #print(analysis.sentiment)
    
    sentiment.delete('1.0','end')
    # sentiment.insert('1.0',article.title)
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


    # Don't let the user change them.
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    sumry.config(state='disabled')
    sentiment.config(state='disabled')
    
    # print(f'Title: {article.title}') not for the function version.
    # print(f'Authors: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Summary: {article.summary}')
    
    # Now do the sentiment analysis
    

    
    #the individual elements of sentiment
    #print(analysis.polarity) 
    #print(analysis.subjectivity)
    
    """The sentiment function of textblob returns two properties, polarity, and subjectivity. 
    Polarity is float which lies in the range of [-1,1] where 1 means positive statement and 
    -1 means a negative statement.
    Subjective sentences generally refer to personal opinion, emotion or judgment 
    whereas objective refers to factual information. Subjectivity is also a float which lies 
    in the range of [0,1].
    """
    

# Not good analysis: The algo gives positive for bad news a few times. Clearly bad news.
# Although: "He is not lucky anymore" gets a -0.16667, good.
# Hmm: "an increase in luck" gets 0.0! no good. as does "a rise in luck" and "a rise in wealthy", "He broke his leg."
# Oh dear! That is definitely not a good thing!

# "He is happy enough." gets a 0.4, okay good.
# wealth is irrelevant to sentiment.

# "My mother died today." is zero!
# "My mother is a moron." -0.8, and subjectivity: 1
# "My mother is a genius." gets NOTHING?!
# as does "My mother is an asshole."!??!?!
# ("My mother is a stupid clown." gets -0.79999 and subj=1, good.
# Your face is ugly: -0.7 and 1.0.



root = tk.Tk()
root.title("News summariser")
root.geometry('1200x600')


tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()


aulabel = tk.Label(root, text="Author")
aulabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

publabel = tk.Label(root, text="Date Published")
publabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

sumlabel = tk.Label(root, text="Summary")
sumlabel.pack()
sumry = tk.Text(root, height=20, width=140)
sumry.config(state="disabled", bg="#dddddd")
sumry.pack()

 
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

urllabel = tk.Label(root, text="URL") #", no quotes please.")
urllabel.pack()
urltext = tk.Text(root, height=1, width=140)
urltext.pack()

btn = tk.Button(root, text="Summarise", command=summarise)
btn.pack()

root.mainloop()











