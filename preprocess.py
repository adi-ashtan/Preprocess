import os
import matplotlib.pyplot as plt
import logging


def plotfromflat(rawsignal_array, eleclist, fs=32000, xrange=False, yrange=False):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(len(eleclist),1 , figsize=(10,len(eleclist)*2))

    for i in range(len(eleclist)):
        ch = eleclist[i]
        raw = rawsignal_array[ch::32]
        ax[i].plot(raw)
        ax[i].set_title('Channel #{}'.format(ch))
        if xrange :
            ax[i].set_xlim(xrange[0], xrange[1])
        if yrange:
            ax[i].set_ylim(yrange[0], yrange[1])

    plt.tight_layout()
    plt.show()

def getRawArray(datadir):
    res = []

    return res

if __name__ == "__main__":
    dataDir = "C:\\Users\\Adi\\PycharmProjects\\Preprocess\\channels"
    elecList = list(range(0, 5))
    raw_array = getRawArray(dataDir)
    plotfromflat(raw_array, elecList)