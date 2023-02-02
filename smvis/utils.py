from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

               
# COLORS
def toHex(rgb_tuple):
    return '#%02x%02x%02x' % rgb_tuple

# FONT
def setFont(font_path):
    
    fontmng = mpl.font_manager

    fontmng.fontManager.addfont(font_path)
    prop = fontmng.FontProperties(fname=font_path)

    plt.rcParams.update({
        "font.family":prop.get_name()
    })

def setFontSize(axes, size):

    for ax in axes:
        legend_texts = ax.get_legend().get_texts() if ax.get_legend() is not None else []
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                    ax.get_xticklabels() + ax.get_yticklabels()+legend_texts):
            item.set_fontsize(size)

# RENDERING
def setLatexRendering(on):
    if on: 
        plt.rcParams.update({
            "text.usetex": True
        })
    if not on:
        plt.rcParams.update({
            "text.usetex": False
        })

## LEGEND HANDLES

# Generate a round legend handle
genRoundLegendHandle = lambda color, markersize: Line2D([0], [0], marker='o', color='w', label='Circle', markerfacecolor=color, markersize=markersize)

# Generate a rect legend handle
genRectLegendHandle = lambda color: Patch(color=color)

# Generate a line legend handle
genLineLegendHandle = lambda color: Line2D([0], [1],color=color, label='Line')

# list of valid arguments vor legend_mode
valid_legend_modes = ["above", "below", "left", "right"]