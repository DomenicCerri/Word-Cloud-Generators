#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:39:27 2022

@author: cerri
"""

# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import re
import numpy as np
from PIL import Image

# select WhatsApp txt dump and cloud image
whatsapp = 'whatsapp-example-text-dump.txt'
maskpath = 'whatsapp-example-image.jpg'

# Define a function to plot word cloud
def plot_cloud(wordcloud, image_colors = None):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    if image_colors:
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation = "bilinear" )
    else:plt.imshow(wordcloud)
    # No axis details
    plt.axis("off");

# Parse WhatsApp .txt dump
datastr=""
with open(whatsapp,'r') as f:
    x = 0
    for line in f:
        if x < 1:
            x+=1
            continue
        thing = line.strip()
        thing = thing.split(':')[2:3]
        try:
            datastr += thing[0]
        except:
            continue
datastr= re.sub("\<.+?\> ", '',datastr)
datastr= re.sub("https?", '',datastr)
datastr= re.sub("[^a-zA-Z' ]", '', datastr)

# Set wordcloud parameters
mask = np.array(Image.open(maskpath))
stop_words = ['Thats'] + list(STOPWORDS)
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white',
                      colormap='Set2', collocations=False, stopwords = stop_words,
                      # contour_width= 3, contour_color= 'black',
                      mask=mask).generate(datastr)
image_colors = ImageColorGenerator(mask)

# Plot
plot_cloud(wordcloud,image_colors)
