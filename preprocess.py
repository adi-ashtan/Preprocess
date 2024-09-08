import os
import matplotlib.pyplot as plt
import numpy as np


def plotfromflat(rawsignal_array, eleclist, fs=32000, xrange=False, yrange=False):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(len(eleclist),1 , figsize=(10,len(eleclist)*2))

    for i in range(len(eleclist)):
        ch = eleclist[i]
        raw = rawsignal_array[i]
        ax[i].plot(raw)
        ax[i].set_title('Channel #{}'.format(ch))
        if xrange :
            ax[i].set_xlim(xrange[0], xrange[1])
        if yrange:
            ax[i].set_ylim(yrange[0], yrange[1])

    plt.tight_layout()
    plt.show()

def getRawArray(datadir,elecList):
    res = []
    i = 0
    step = 0
    filelist = os.listdir(datadir)
    for infile in sorted(filelist):
        fid = open(datadir + '\\' + infile, 'rb')
        line = np.fromfile(fid, dtype=np.int16).tolist()
        step = len(line)
        res += line
        i+=1
        fid.close()
    res = np.reshape(res, (len(elecList),step))
    return res

if __name__ == "__main__":
    # change dir name to your directory
    dataDir = "C:\\Users\\Adi\\PycharmProjects\\Preprocess\\channels"
    elecList = list(range(0, 32))
    raw_array = getRawArray(dataDir,elecList)
    plotfromflat(raw_array, elecList)