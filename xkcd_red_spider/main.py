"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/main.py
"""
import os
from typing import Dict, List, Tuple

import pyvista as pv

import xkcd_red_spider.utils as utils


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


# Hand-crafted spider army coords that mimic the xkcd comic: Red Spiders Cometh
# https://xkcd.com/126/
XKCD_SPIDER_ARMY_COORD = {
    (1, 0): None,
    (0, 3): [("z", -90), ("y", 180)],
    (-1, -2): [("z", 0), ("y", 180)],
    (3, -2): [("z", 0), ("y", 180)],
    (5, 2): [("z", 180), ("y", -90)],
    (6, -1): [("z", 90)],
    (8, 1): None,
    (10, -1): [("y", -90)],
    (-2, 2): [("z", -90)],
    (-4, 2): [("y", 90)],
    (-6, -1): [("y", 180)],
    (-8, 2): [("x", -90)],
    (-8, -2): [("y", 90)],
    (-10, -3): None,
}


# A nice default camera position that I found manually
DEFAULT_CAMERA_POSITION = [(-0.7, -26.7, -7.3), (-0.47, 0, -4.6), (0, -0.1, 1)]


def get_xkcd_spider_army(
    spider_army_coord: Dict[Tuple[int, int], List[Tuple[str, int]]] = None,
    extra_spider: bool = True,
) -> List[Tuple[pv.PolyData, pv.PolyData]]:
    """Generate the xkcd spider army through the army coordinates.

    Args:
        spider_army_coord (Dict[Tuple[int, int], List[Tuple[str, int]]], optional): Coordinates and
            rotation steps of the red spider army. Check XKCD_SPIDER_ARMY_COORD for the example
            setting. Defaults to None.
        extra_spider (bool, optional): whether or not to add extra spiders on two boxes, to improve
            fidelity with the original comic. Defaults to True.

    Returns:
        List[Tuple[pv.PolyData, pv.PolyData]]: list of (spider, box) ``pv.PolyData`` tuples.
    """
    if spider_army_coord is None:
        spider_army_coord = XKCD_SPIDER_ARMY_COORD

    spider_army = []
    for spider_unit_coord, spider_unit_rotation in spider_army_coord.items():
        spider_army.append(
            utils.process_spider_box_unit_cell(
                spider=utils.get_unit_cell_spider(),
                box=utils.get_unit_cell_box(),
                rotation=spider_unit_rotation,
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


def main(color_spider="red", color_box="tan", color_buildings="lightgray") -> pv.Plotter:
    """Main function for rendering the 3D scene for
    `red spider cometh xkcd comic <https://xkcd.com/126/>`_.

    Args:
        color_spider (str, optional): color of the spiders. Defaults to "red".
        color_box (str, optional): color of the boxes. Defaults to "tan".
        color_buildings (str, optional): color of the buildings. Defaults to "lightgray".

    Returns:
        pv.Plotter: pyvista plotter for plotting the 3D scene.
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
    pv.set_plot_theme("document")
    p = main()
    p.camera_position = DEFAULT_CAMERA_POSITION
    vtkjs_file_path = os.path.join(DATA_DIR, "red_spiders_cometh")
    if not os.path.isfile(vtkjs_file_path):
        p.export_vtkjs(vtkjs_file_path)
    p.show()
    print(p.camera_position)  # print the final camera position to the stdout
