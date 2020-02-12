import numpy as np
import pandas as pd

def log_bins(x, bin_count, semilog=False):
    '''Returns bins with logarithmic scale.
    x: 1d array-like
    bin_count : int
    semilog : bool
    '''
    upper_bound = np.ceil(np.log10(x.max()))
    bins = np.logspace(0, upper_bound, bin_count)
    if semilog:
        bins = np.hstack([[0], bins])
    return bins
    
x = pd.Series(2**np.random.randint(10, size=1000))
x.hist(bins=log_bins(x, 50, semilog=True))
plt.xscale('symlog')
