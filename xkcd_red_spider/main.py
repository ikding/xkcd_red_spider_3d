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
    spider = utils.get_unit_cell_spider()
    box = utils.get_unit_cell_box()
    buildings = utils.get_buildings()
    buildings.translate([0, 0, -5])
    plotter = pv.Plotter()
    plotter.add_mesh(spider, 'r')
    plotter.add_mesh(box, color="tan", show_edges=True)
    plotter.add_mesh(buildings, color="white")
    plotter.show()


if __name__ == "__main__":
    main()
