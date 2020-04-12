"""Utility functions for making a spider army unit (red spider on a box)."""
import os
from typing import Dict, List, Tuple, Union

import numpy as np
import pyvista as pv
from pyvista import examples


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


def get_unit_cell_box() -> pv.PolyData:
    """Return a box unit. The box has length 1 in all 3 dimensions, and is centered at the origin.

    Having the box centered at origin will make it easier for rotating the spider on a box.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the box unit.
    """
    default_box = pv.Box()
    default_box.points /= 2
    return default_box


def get_unit_cell_spider() -> pv.PolyData:
    """Return a spider unit. The spider has legspan that is slightly smaller than the box face, and
    is in a position so it appears to be standing on the box unit.

    Having the spider unit standing on the box centered at origin will make it easier for rotating
    the spider on a box.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the spider unit.
    """
    default_spider = pv.read(os.path.join(DATA_DIR, "spider.ply"))
    default_spider.points /= 6
    default_spider.translate([-0.5, -0.5, 0.4])
    default_spider.rotate_z(-110)
    return default_spider


def get_buildings() -> pv.PolyData:
    """Return a set of buildings, which was downloaded from sketchfab and saved in project file.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the buildings.
    """
    default_buildings = pv.read(
        os.path.join(DATA_DIR, "buildings-and-skyscrapers", "source", "buildings.obj")
    )
    default_buildings.rotate_x(90)
    default_buildings.translate([-4, -4, 0])
    return default_buildings


def process_spider_box_unit_cell(
    spider: pv.PolyData = get_unit_cell_spider(),
    box: pv.PolyData = get_unit_cell_box(),
    scale: float = 1.0,
    rotation: List[Tuple[str, float]] = None,
    translation: List[Union[int, float]] = None,
) -> Tuple[pv.PolyData, pv.PolyData]:
    """Process the spider-box unit cell through operations including scaling, rotations, and
    translations.

    Args:
        spider (pv.PolyData, optional): Polydata containing the spider unit. Defaults to
            get_unit_cell_spider().
        box (pv.PolyData, optional): Polydata containing the box unit. Defaults to
            get_unit_cell_box().
        scale (float, optional): scaling factor. Defaults to 1.0.
        rotation (List[Tuple[str, float]], optional): list of steps for rotation, in the form of
            list of tuples, and the tuple containing the direction (``"x"``, ``"y"``, or ``"z"``)
            in the first element, and the degrees in the second direction. Example:
            ``[("x", 90), ("z", 180)]``. Under the hood, the
            `rotate_x <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_x>`_,
            `rotate_y <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_y>`_, and
            `rotate_z <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_z>`_
            methods in ``pv.PolyData`` are called. Defaults to None.
        translation (List[Union[int, float]], optional): Length of 3 list or array to translate the
            polydata. Under the hood, the
            `translate <https://docs.pyvista.org/core/common.html#pyvista.Common.translate>`_
            method in ``pv.PolyData`` is called. Defaults to None.

    Returns:
        Tuple[pv.PolyData, pv.PolyData]: A tuple of ``pv.Polydata`` containing the spider and box.
    """
    spider.points *= scale
    box.points *= scale

    if isinstance(rotation, list):
        for step in rotation:
            if step[0] == "x":
                spider.rotate_x(step[1])
            if step[0] == "y":
                spider.rotate_y(step[1])
            if step[0] == "z":
                spider.rotate_z(step[1])

    if isinstance(translation, list):
        spider.translate(translation)
        box.translate(translation)

    return (spider, box)
