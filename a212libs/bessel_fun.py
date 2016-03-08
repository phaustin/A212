import numpy as np
import numpy.testing as ntest
import doctest


def bessel(x, order):
    """
    Evaluate the spherical bessel function for orders 0,1, or 2


    Parameters
    ----------

    x: array (any shape) or scalar (float32, float64  or complex)
       values to evaluate bessel function 
    order: int
       order of bessel function between 0-2

    Returns
    -------

    output of bessel function of order order with original shape
    preserved

    Example
    -------

    >>> bessel([1.,2.,3.],2)
    array([ 0.06203505,  0.19844795,  0.2986375 ])


    References
    ----------

    https://en.wikipedia.org/wiki/Bessel_function#Spherical_Bessel_functions:_jn.2C_yn

    """


    x = np.atleast_1d(x)
    the_shape = x.shape
    if x.dtype not in [np.float32, np.float64, np.complex]:
        raise ValueError(
            "expected dtype of float32,float64 or complex, got {}",
            format(x.dtype))

    #
    # here are our bessel functions
    #

    def j_0(y):
        out = np.sin(y) / y
        return out

    def j_1(y):
        out = np.sin(y) / (y**2) - np.cos(y) / (y)
        return out

    def j_2(y):
        out = ((3 / (y**2)) - 1) * (np.sin(y) / y) - ((3 * np.cos(y)) / y**2)
        return out

    #
    # index the three functions with their orders
    #

    order_dict = {0: j_0, 1: j_1, 2: j_2}

    #
    # catch erroneous order
    #
    avail_orders = list(order_dict.keys())
    if order not in avail_orders:
        raise ValueError(
            "expected order parameter of {} got {}".format(avail_orders,order))
    #
    # loop over all items in the array,
    # putting the output into a new array of
    # the same dtype and shape.  Return none if
    # we get a 0
    #

    out = np.empty([x.size], dtype=x.dtype)
    for count, val in enumerate(x.flat):
        if val == 0.:
            out[count] = None
        else:
            out[count] = order_dict[order](val)
    out.shape = the_shape
    if out.size == 1:
        out = out[0]
    return out


def test_bessel():
    out = bessel([1., 2., 3.], 2)
    ntest.assert_almost_equal(out, [0.06203505, 0.19844795, 0.2986375])


if __name__ == "__main__":

    print('running bessel tests')
    test_bessel()
    doctest.testmod()

    do_plot = False
    if do_plot:
        from matplotlib import pyplot as plt
        plt.close('all')
        fig, ax = plt.subplots(1, 1)
        x = np.linspace(0, 20, 100)
        for order in [0, 1, 2]:
            ax.plot(x, bessel(x, order), label='j{}x'.format(order))
        ax.legend()
        plt.show()
