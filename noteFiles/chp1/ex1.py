# Exercise 1: Try to produce a figure with a given (and exact) pixel size (e.g.
# 512x512 pixels). How would you specify the size and save the figure?

import matplotlib.pyplot as plt

def figure(dpi):
    fig = plt.figure(figsize=(512/dpi,512/dpi))
    ax = plt.subplot(1,1,1)
    text = "Text rendered at 10pt using %d dpi" % dpi
    ax.text(0.5, 0.5, text, ha="center", va="center",
    fontname="Serif",
    fontsize=10, fontweight="light")
    plt.savefig("figure-dpi-%03d.png" % dpi, dpi=dpi)
figure(50), figure(100), figure(300), figure(600)
