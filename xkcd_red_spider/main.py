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

    rotated_spider, rotated_box = utils.scale_rotate_spider_box_unit_cell(
        spider=spider, box=box, rotation=[("z", -90), ("y", 180)]
    )

    buildings = utils.get_buildings()
    buildings.points *= 2
    buildings.translate([0, 0, -10])
    plotter = pv.Plotter()
    plotter.add_mesh(rotated_spider, 'r')
    plotter.add_mesh(rotated_box, color="tan", show_edges=True)
    plotter.add_mesh(buildings, color="white", show_edges=True)
    plotter.show()


if __name__ == "__main__":
    main()
