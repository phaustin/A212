import numpy as np
from a212libs.utils import read_data
import numpy.testing as ntest

def LineFitWt(x, y, dy):
    """
    Use pine chapter 7 equations in section 7.3.2 to do
    a weighted linear regression

    Parameters
    ----------
    
    x: array (any shape) float
      x (independent) values for regression

    y: array (same shape as x) float
      y (dependent) values for regression

    dy: array (same shape as x) float
      uncertainty estimate in y

    Returns
    -------

    slope: float
       regression slope

    intercept: float
       regression intercept

    slope_uncertainty: float
       sigma squared for slope estimate

    intercept_uncertainty: float
       sigma squared for intercept estimate
    
    Example
    -------

    see test function below

    """
    x = x.ravel()
    y=y.ravel()
    dy = dy.ravel()
    if len(x) != len(y):
        raise ValueError('x and y must have same number of elements')
    if len(y) != len(dy):
        raise ValueError('y and dy must have the same number of elements')
    x = x.astype(np.float)
    y = y.astype(np.float)
    dy = dy.astype(np.float)
    
    dy2 = dy**2.
    denom= np.sum(1/(dy**2.))  # Pine 7.14
    xnumerator = np.sum(x/dy2)
    ynumerator = np.sum(y/dy2)
    xhat = xnumerator/denom
    yhat = ynumerator/denom
    bnum = np.sum((x - xhat)*y/dy2)
    bdenom = np.sum((x - xhat)*x/dy2)
    slope = bnum/bdenom
    yint = yhat - slope*xhat
    #
    # add pine 7.16
    #
    slope_uncertainty = 1./np.sum((x - xhat)*x/dy2)
    intercept_uncertainty = slope_uncertainty*\
          np.sum(x**2./dy2)/np.sum(1./dy2)
    return slope,yint,slope_uncertainty,intercept_uncertainty


def test_fit():
    data_string = """
    time   velocity   uncertainty
    2.23          139               16
    9.37           96                9
    11.64           62               17
    16              20               25
    23.21          -55               10
    """
    df_data = read_data(data_string)
    time = df_data['time'].values
    velocity = df_data['velocity'].values
    dy = df_data['uncertainty'].values
    slope_w,yint_w, var_slope, var_inter = LineFitWt(time,velocity,dy)
    ntest.assert_almost_equal([slope_w,yint_w,var_slope,var_inter],
                              [-9.9656001,179.924646 ,0.5982539,140.7892905])

if __name__ == "__main__":
    print('running linfit tests')
    test_fit()
