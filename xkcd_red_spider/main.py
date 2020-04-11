"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/main.py
"""
import pyvista as pv
from pyvista import examples

import xkcd_red_spider.utils as utils


def main(color_spider="red", color_box="tan", color_buildings="white"):
    """[summary]

    [extended_summary]
    """
    plotter = pv.Plotter()

    spider_army = {}

    spider_army[(1, 0)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        translation=[1, 0, 0]
    )

    spider_army[(0, 3)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", -90), ("y", 180)],
        translation=[0, 3, 0],
    )

    spider_army[(-1, -2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", 0), ("y", 180)],
        translation=[-1, -2, 0]
    )

    spider_army[(3, -2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", 0), ("y", 180)],
        translation=[3, -2, 0]
    )

    spider_army[(4, 0)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", 180), ("y", -90)],
        translation=[4, 0, 0]
    )

    spider_army[(6, -1)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", -90)],
        translation=[6, -1, 0]
    )

    spider_army[(8, 1)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        translation=[8, 1, 0]
    )

    spider_army[(10, -1)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("y", -90)],
        translation=[10, -1, 0],
    )

    spider_army[(-2, 2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("z", -90)],
        translation=[-2, -2, 0],
    )

    spider_army[(-4, 2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("y", 90)],
        translation=[-4, 2, 0],
    )

    spider_army[(-6, -1)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("y", 180)],
        translation=[-6, -1, 0],
    )

    spider_army[(-7, 2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("x", -90)],
        translation=[-7, 2, 0],
    )

    spider_army[(-7, -2)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        rotation=[("y", 90)],
        translation=[-7, -2, 0],
    )

    spider_army[(-9, -3)] = utils.process_spider_box_unit_cell(
        spider=utils.get_unit_cell_spider(),
        box=utils.get_unit_cell_box(),
        translation=[-9, -3, 0],
    )

    buildings = utils.get_buildings()
    buildings.points *= 2
    buildings.translate([0, 0, -10])

    for unit in spider_army.values():
        plotter.add_mesh(unit[0], color=color_spider)
        plotter.add_mesh(unit[1], color=color_box, show_edges=True)
    plotter.add_mesh(buildings, color=color_buildings, show_edges=True)
    plotter.show()


if __name__ == "__main__":
    main()
