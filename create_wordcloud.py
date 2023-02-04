import os

from os import path
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
def generate_wordcloud(text, image_path,out_path):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(text).read()

    mask = np.array(Image.open(image_path))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=mask,
                stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(out_path)

    # show
    plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    print(sys.argv)
    text = sys.argv[1]
    image_path = sys.argv[2]
    out_path = sys.argv[3]
    print(text, image_path, out_path)
    generate_wordcloud(text, image_path,out_path)
    print("Wordcloud generated!")