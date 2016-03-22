import pandas as pd
def read_h5(h5filename,key):
    with pd.HDFStore(h5filename,'r') as store:
        out=store[key]
    return out

