# -*- coding: utf-8 -*-
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

from PyQt5 import QtCore


def colormap_jet():
    cmap_array = np.array([[0, 0, 143, 255], [0, 0, 159, 255], [0, 0, 175, 255], [0, 0, 191, 255], [0, 0, 207, 255],
                           [0, 0, 223, 255], [0, 0, 239, 255], [0, 0, 255, 255], [0, 16, 255, 255], [0, 32, 255, 255],
                           [0, 48, 255, 255], [0, 64, 255, 255], [0, 80, 255, 255], [0, 96, 255, 255], [0, 112, 255, 255],
                           [0, 128, 255, 255], [0, 143, 255, 255], [0, 159, 255, 255], [0, 175, 255, 255], [0, 191, 255, 255],
                           [0, 207, 255, 255], [0, 223, 255, 255], [0, 239, 255, 255], [0, 255, 255, 255],
                           [16, 255, 239, 255],
                           [32, 255, 223, 255], [48, 255, 207, 255], [64, 255, 191, 255], [80, 255, 175, 255],
                           [96, 255, 159, 255], [112, 255, 143, 255], [128, 255, 128, 255], [143, 255, 112, 255],
                           [159, 255, 96, 255], [175, 255, 80, 255], [191, 255, 64, 255], [207, 255, 48, 255],
                           [223, 255, 32, 255], [239, 255, 16, 255], [255, 255, 0, 255], [255, 239, 0, 255],
                           [255, 223, 0, 255], [255, 207, 0, 255], [255, 191, 0, 255], [255, 175, 0, 255], [255, 159, 0, 255],
                           [255, 143, 0, 255], [255, 128, 0, 255], [255, 112, 0, 255], [255, 96, 0, 255], [255, 80, 0, 255],
                           [255, 64, 0, 255], [255, 48, 0, 255], [255, 32, 0, 255], [255, 16, 0, 255], [255, 0, 0, 255],
                           [239, 0, 0, 255], [223, 0, 0, 255], [207, 0, 0, 255], [191, 0, 0, 255], [175, 0, 0, 255],
                           [159, 0, 0, 255], [143, 0, 0, 255], [128, 0, 0, 255]], dtype=np.ubyte)
    return cmap_array


class ImagePlot:

    def __init__(self, window_title: str, active: bool = True, black_and_white: bool = False, rgb: bool = False):
        """Plots images using pyqtgraph

        Parameters
        ----------
        window_title : str
            The title of the window
        active : bool
            True is window should be active (the default is True).
        black_and_white : bool
            If True plot image in black and white (the default is False).
        rgb : bool
            If True, expect images to have 3 channels (RGB)
        """
        self.active = active
        self.rgb = rgb

        # Set title
        self.window_title = window_title

        # Create window
        self.window = pg.GraphicsLayoutWidget()
        self.window.setWindowTitle(window_title)

        # Set colormap
        jet_c = colormap_jet()
        pos = np.linspace(0, 63, 64) / 64
        cmap = pg.ColorMap(pos, jet_c)
        self.jet = cmap.getLookupTable(0.0, 1.0, 256)

        # Set plot
        self.image = pg.ImageItem()
        if not black_and_white and not rgb:
            self.image.setLookupTable(self.jet)

        self.plot = self.window.addPlot()
        self.plot.addItem(self.image)
    
    def imshow(self, data, clim=None):
        self.window.setWindowTitle('{}'.format(self.window_title))
        self.window.show()
    
        # Set image
        #self.image.setImage(np.flipud(np.rot90(data),3))
        self.image.setImage(np.rot90(np.fliplr((np.flipud(data)))))
    
        # Set color limits
        if not self.rgb:
            if clim is None:
                clim = [np.min(data), np.max(data)]
            self.image.setLevels(clim)         
        else:
            self.window.setWindowTitle('{}'.format(self.window_title))
    
        QtCore.QCoreApplication.processEvents()
    
    def setWindowSize(self, x_size=800, y_size=600):
        """
        Sets the window size to [x_size, y_size]
        """
    
        self.window.resize(x_size, y_size)