import pandas as pd
import matplotlib.pyplot as plt

def plot_mask(series, mask, neg_kw={}, pos_kw={}):
    
    '''
    Display plot of series values with differnt lines for
    False and True values in mask.
    
    Parameters
    ----------
    series: pd.Series of int/float with pd.DatetimeIndex
    mask: pd.Series of bool with same index as series
    neg_kw, pos_kw: dict with arguments of pd.Series.plot()
    
    Returns
    ---------
    None
    
    '''
    series[~mask].reindex(index=series.index).plot(**neg_kw)
    series[mask].reindex(index=series.index).plot(**pos_kw)
    plt.legend()
    plt.show()
