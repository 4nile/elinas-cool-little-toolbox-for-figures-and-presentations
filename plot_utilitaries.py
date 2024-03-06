import matplotlib.pyplot as plt
import matplotlib as mpl
from itertools import cycle
import matplotlib.colors as mc
import colorsys
import numpy as np

palette=['#ff7ac1', '#e40303', '#ff8c00', '#ffd800',\
            '#008026', '#1b7485', '#004dff', '#7932f4', '#750787']
colors = cycle(palette)

markers = ['o', 'v', '^', 's', 'D']
mark=cycle(markers)

line_list = ['-',':','--','-.',(0, (3, 3, 1, 3, 1, 3)), (0, (3, 1, 1, 1))]

palette =['#ff7ac1', '#e40303', '#ff8c00', '#ffd800',\
            '#008026', '#1b7485', '#004dff', '#4D4295']

paletteT = ['#19255C', '#5861b4', '#a1c8d1', '#f1bf6e', '#de6502', '#82161f']

palettev = ['#af008a','#0000FF', '#88FEFF', '#F8EC53', '#FF0000']


def couleur(index, Len, palette):
    n = len(palette) - 1
    cmin = np.floor(index/Len*n)
    cmax = np.ceil(index/Len*n)
        
    if cmin != cmax:
        x = (index/Len*n - cmax) / (cmin - cmax)
        cmin = mc.to_rgb(palette[int(cmin)])
        cmax = mc.to_rgb(palette[int(cmax)])      
    
        return (x*cmin[0]+(1-x)*cmax[0], x*cmin[1]+(1-x)*cmax[1], x*cmin[2]+(1-x)*cmax[2])
    else:
        return palette[int(cmin)]

def adjust_lightness(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    return couleur(int(amount*100), 100, ['white', color, 'black'])

def color_marker(color, alpha=0.6):
    cola = mc.to_rgb(color)
    cola = [cola[0], cola[1], cola[2], alpha]
    return color, cola


rainbowcmap = [mc.to_rgb(couleur(i, 256, palette)) for i in range(256)]
tempcmap = [mc.to_rgb(couleur(i, 256, paletteT)) for i in range(256)]
speedcmap = [mc.to_rgb(couleur(i, 256, palettev)) for i in range(256)]
mycmapR = mc.ListedColormap(rainbowcmap)
mycmapT = mc.ListedColormap(tempcmap)
mycmapV = mc.ListedColormap(speedcmap)

def set_size(w, h, ax=None):
    if not ax: ax=plt.gca()

    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom

    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    
    ax.figure.set_size_inches(figw,figh)