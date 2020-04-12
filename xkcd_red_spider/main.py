"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/main.py
"""
from typing import Dict, List, Tuple

import pyvista as pv
from pyvista import examples

import xkcd_red_spider.utils as utils


XKCD_SPIDER_ARMY_COORD = {
    (1, 0): None,
    (0, 3): [("z", -90), ("y", 180)],
    (-1, -2): [("z", 0), ("y", 180)],
    (3, -2): [("z", 0), ("y", 180)],
    (4, 0): [("z", 180), ("y", -90)],
    (6, -1): [("z", 90)],
    (8, 1): None,
    (10, -1): [("y", -90)],
    (-2, 2): [("z", -90)],
    (-4, 2): [("y", 90)],
    (-6, -1): [("y", 180)],
    (-8, 2): [("x", -90)],
    (-7, -2): [("y", 90)],
    (-10, -3): None,
}


def get_xkcd_spider_army(
    spider_army_coord: Dict[Tuple[int, int], List[Tuple[str, int]]] = XKCD_SPIDER_ARMY_COORD,
    extra_spider: bool = True,
) -> List[Tuple[pv.PolyData, pv.PolyData]]:
    """[summary]

    [extended_summary]

    Args:
        spider_army_coord (Dict[Tuple[int, int], List[Tuple[str, int]]], optional): [description].
        Defaults to XKCD_SPIDER_ARMY_COORD.
        extra_spider (bool, optional): [description]. Defaults to True.

    Returns:
        List[Tuple[pv.PolyData, pv.PolyData]]: [description]
    """
    spider_army = []
    for spider_unit_coord, spider_unit_rotatation in spider_army_coord.items():
        spider_army.append(
            utils.process_spider_box_unit_cell(
                spider=utils.get_unit_cell_spider(),
                box=utils.get_unit_cell_box(),
                rotation=spider_unit_rotatation,
                translation=list(spider_unit_coord) + [0],
            )
        )

    # Add two extra spiders for fidelity with xkcd comic
    if extra_spider and (spider_army_coord == XKCD_SPIDER_ARMY_COORD):
        spider_army += [
            utils.process_spider_box_unit_cell(
                spider=utils.get_unit_cell_spider(),
                box=utils.get_unit_cell_box(),
                rotation=[("x", 90)],
                translation=[-1, -2, 0],
            ),
            utils.process_spider_box_unit_cell(
                spider=utils.get_unit_cell_spider(),
                box=utils.get_unit_cell_box(),
                rotation=[("z", 180)],
                translation=[-4, 2, 0],
            ),
        ]

    return spider_army


def main(color_spider="red", color_box="tan", color_buildings="white") -> pv.Plotter:
    """[summary]

    [extended_summary]

    Args:
        color_spider (str, optional): [description]. Defaults to "red".
        color_box (str, optional): [description]. Defaults to "tan".
        color_buildings (str, optional): [description]. Defaults to "white".

    Returns:
        pv.Plotter: [description]
    """
    plotter = pv.Plotter()

    spider_army = get_xkcd_spider_army()
    buildings = utils.get_buildings()
    buildings.points *= 1
    buildings.translate([0, 0, -10])

    for unit in spider_army:
        plotter.add_mesh(unit[0], color=color_spider)  # spider
        plotter.add_mesh(unit[1], color=color_box, show_edges=True)  # box
    plotter.add_mesh(buildings, color=color_buildings, show_edges=True)

    return plotter


if __name__ == "__main__":
    p = main()
    p.show()
