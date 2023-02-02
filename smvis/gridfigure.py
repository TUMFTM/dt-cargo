from matplotlib import gridspec, pyplot as plt 
from .utils import valid_legend_modes

class GridFigure:

    def __init__(self, nrows, ncols, fig_width, fig_height, 
                 hspace=0, wspace=0, legend_wh_ratio=0.1, 
                 legend_mode=None, constrained_layout=False,
                 ratios=None):
        assert legend_mode is None or legend_mode in valid_legend_modes, f"legend mode invalid, please choose from: {valid_legend_modes}"
        # Fill properties
        self.nrows = nrows 
        self.ncols = ncols 
        self.fig_width = fig_width 
        self.fig_height = fig_height
        self.hspace = hspace 
        self.wspace = wspace 
        self.ratios = ratios 
        self.legend_wh_ratio = legend_wh_ratio
        self.legend_mode = legend_mode
        self.constrained_layout = constrained_layout

        # Create figures
        self.fig, self.axes, self.legend_ax = self._createFig()
        self.axes_list = self._axesDict2List()
        self.center = self._getCenter()
        self.bottom = self._getBottom()
        self.left = self._getLeft()
        self.right = self._getRight()
        self.top = self._getTop()
        self.size = self._getGridSize()

    
    def _createFig(self):

        # Create figure
        fig = plt.figure(constrained_layout=self.constrained_layout, figsize=(self.fig_width,self.fig_height))

        if self.legend_mode is None and self.ratios is not None:
            # no legend and manual ratios
            height_ratios = self.ratios['height']
            width_ratios = self.ratios['width']
            
        elif self.legend_mode is None and self.ratios is None:
            # no legend and equal ratios
            height_ratios = [1/self.nrows]*self.nrows
            width_ratios = [1/self.ncols]*self.ncols
        
        elif self.legend_mode is not None and self.ratios is None:
            # legend and equal ratios
            residual_size_proportion = 1-self.legend_wh_ratio

            if self.legend_mode=="left":
                width_ratios = [self.legend_wh_ratio]+self.ncols*[residual_size_proportion/self.ncols]
                height_ratios = [1/self.nrows]*self.nrows
                self.ncols += 1

            elif self.legend_mode=="right":
                width_ratios = self.ncols*[residual_size_proportion/self.ncols]+[self.legend_wh_ratio]
                height_ratios = [1/self.nrows]*self.nrows
                self.ncols += 1 
                
            elif self.legend_mode=="below":
                width_ratios = [1/self.ncols]*self.ncols
                height_ratios = self.nrows*[residual_size_proportion/self.nrows]+[self.legend_wh_ratio]
                self.nrows += 1 
                
            elif self.legend_mode=="above":
                width_ratios = [1/self.ncols]*self.ncols
                height_ratios = [self.legend_wh_ratio]+self.nrows*[residual_size_proportion/self.nrows]
                self.nrows += 1
        
        elif self.legend_mode is not None and self.ratios is not None:
            # legend and manual ratios
            residual_size_proportion = 1-self.legend_wh_ratio

            if self.legend_mode=="left":
                width_ratios = [self.legend_wh_ratio]+self.ratios['width']
                height_ratios = self.ratios['height']
                self.ncols += 1

            elif self.legend_mode=="right":
                width_ratios = self.ratios['width']+[self.legend_wh_ratio]
                height_ratios = self.ratios['height']
                self.ncols += 1 
                
            elif self.legend_mode=="below":
                width_ratios = self.ratios['width']
                height_ratios = self.ratios['height']+[self.legend_wh_ratio]
                self.nrows += 1 
                
            elif self.legend_mode=="above":
                width_ratios = self.ratios['width']
                height_ratios = [self.legend_wh_ratio]+self.ratios['height']
                self.nrows += 1
        
        # Define grid layout
        spec = gridspec.GridSpec(ncols=self.ncols,
                                nrows=self.nrows,
                                figure=fig,
                                height_ratios=height_ratios,
                                width_ratios=width_ratios,
                                hspace=self.hspace,
                                wspace=self.wspace)


        # Add axes to grid layout
        axes = {}
        
        legend_ax = None

        if self.legend_mode is not None: 
            if self.legend_mode=="left":
                row_offset = 0
                col_offset = 1
                row_cap = 0
                col_cap = 1
                legend_ax = fig.add_subplot(spec[0:self.nrows,0])

            elif self.legend_mode=="right":
                row_offset = 0
                col_offset = 0
                row_cap = 0
                col_cap = 1
                legend_ax = fig.add_subplot(spec[0:self.nrows,-1])
                
            elif self.legend_mode=="below":
                row_offset = 0
                col_offset = 0
                row_cap = 1
                col_cap = 0
                legend_ax = fig.add_subplot(spec[-1,0:self.ncols])
                
            elif self.legend_mode=="above":
                row_offset = 1
                col_offset = 0
                row_cap = 1
                col_cap = 0
                legend_ax = fig.add_subplot(spec[0,0:self.ncols])

        else:
            row_offset = 0
            col_offset = 0
            row_cap = 0
            col_cap = 0

        iter_rows = list(range(self.nrows))
        iter_cols = list(range(self.ncols))
        iter_rows = iter_rows[:len(iter_rows)-row_cap]
        iter_cols = iter_cols[:len(iter_cols)-col_cap]

        for row in iter_rows:
            for col in iter_cols:
                axes[(row, col)] = fig.add_subplot(spec[row+row_offset, col+col_offset])

        return fig, axes, legend_ax

    # Get size of axes grid
    def _getGridSize(self):
        nrows = max([k[0] for k in self.axes.keys()])+1
        ncols = max([k[1] for k in self.axes.keys()])+1
        return nrows, ncols

    # Get sublists of left boundary axes
    def _getLeft(self):
        return set([self.axes[k] for k in self.axes.keys() if k[1]==0])

    # Get sublists of top boundary axes
    def _getTop(self):
        return set([self.axes[k] for k in self.axes.keys() if k[0]==0])

    # Get sublists of right boundary axes
    def _getRight(self):
        _, ncols = self._getGridSize()
        return set([self.axes[k] for k in self.axes.keys() if k[1]==ncols-1])

    # Get sublists of bottom boundary axes
    def _getBottom(self):
        nrows, _ = self._getGridSize()
        return set([self.axes[k] for k in self.axes.keys() if k[0]==nrows-1])

    def _getCenter(self):
        
        nrows, ncols = self._getGridSize()
        bottom_axes = self._getBottom()
        top_axes = self._getTop()
        left_axes = self._getLeft()
        right_axes = self._getRight()

        if nrows==1:
            center_axes = [ax for ax in self.axes if (ax not in left_axes and ax not in right_axes)]
        elif ncols==1:
            center_axes = [ax for ax in self.axes if (ax not in top_axes and ax not in bottom_axes)]
        else:
            center_axes = [ax for ax in self.axes if (ax not in top_axes and ax not in bottom_axes and ax not in left_axes and ax not in right_axes)]
        
        return set(center_axes)

    def _axesDict2List(self):
        return list(self.axes.values())