import numpy as np
import matplotlib.pyplot as plt

# Plot a profile of the data
def profile_data(x, y, nbins, xlow, xhigh, colors, plabels, title="", xlabel="", ylabel=""):
    assert(len(y)==len(colors)==len(plabels))
    
    bins = np.linspace(xlow, xhigh, nbins+1)
    bin_center = [(bins[i]+bins[i+1])/2. for i in range(len(bins)-1)]
    
    for i, ydata in enumerate(y):
        means, err = [], []
        for ibin in range(nbins):
            bin_entries = ydata[(x>bins[ibin]) & (x<=bins[ibin+1])]
            means.append(bin_entries.mean())
            err.append(np.std(bin_entries)/np.sqrt(len(bin_entries)))

        plt.xlim(xlow, xhigh)  
        plt.scatter(bin_center, means, marker='o', color=colors[i], label=plabels[i])
        plt.errorbar(bin_center, means, yerr=err, color=colors[i], fmt="none")
    plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()