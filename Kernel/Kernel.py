from os import stat


import numpy as np
class Kernel:
    @staticmethod
    def Gaussian(len, std):
        ax = np.linspace(-(len - 1) / 2., (len - 1) / 2., len)
        gauss = np.exp(-0.5 * np.square(ax) / np.square(std))
        kernel = np.outer(gauss, gauss)
        return kernel / np.sum(kernel)

