import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

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


def plot_circles(ax, xs, ys, rs, **kwargs):
    '''
    Add circles to existing axes.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
    
    xs : iterable
    X coordinates of the circles centers.
    
    ys : iterable
    Y coordinates of the circles centers.
    
    rs : iterable
    Circles radiuses.
    
    Returns
    -------
    None
    '''
    for x, y, r in zip(xs, ys, rs):
        c = Circle((x, y), r, **kwargs)
        ax.add_patch(c)
