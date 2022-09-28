#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:39:27 2022

@author: cerri
"""
# Import packages
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from docx import Document
import numpy as np
from PIL import Image
import re

# Select docx and wordcloud image
document = Document('docx-example_Katz-Review-Draft.docx')
maskpath = 'docx-example-image.png'

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

# Parse docx
datastr=""
for para in document.paragraphs:
    datastr += para.text

# Set wordcloud params
mask = np.array(Image.open(maskpath))
stop_words = ['et','al'] + list(STOPWORDS)
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white',
                      colormap='Set2', collocations=False, stopwords = stop_words,
                      contour_width= 3, contour_color= 'black',
                      mask=mask).generate(datastr)
image_colors = ImageColorGenerator(mask)

plot_cloud(wordcloud)
