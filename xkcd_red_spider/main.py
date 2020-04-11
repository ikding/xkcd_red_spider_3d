"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/main.py
"""
import pyvista as pv
from pyvista import examples

import xkcd_red_spider.utils as utils


def main():
    """[summary]

    [extended_summary]
    """
    spider, box = utils.get_spider_box_unit_cell()
    plotter = pv.Plotter()
    plotter.add_mesh(spider, 'r')
    plotter.add_mesh(box, color="tan", show_edges=True)
    plotter.show()


if __name__ == "__main__":
    main()
