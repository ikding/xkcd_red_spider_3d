"""Utility function for making red spider on a box."""
from typing import Dict, Tuple

import numpy as np
import pyvista as pv
from pyvista import examples


def get_spider_box_unit_cell() -> Tuple[pv.PolyData, pv.PolyData]:
    """[summary]

    [extended_summary]

    Returns:
        Tuple[pv.PolyData, pv.PolyData]: [description]
    """
    default_spider = examples.download_spider()
    default_box = pv.Box()
    default_box.points *= 3
    default_spider.translate([-3, -3, 2.5])
    default_spider.rotate_z(-20)

    return (default_spider, default_box)


def scale_rotate_spider_box_unit_cell(
    spider: pv.PolyData, box: pv.PolyData, scale: float = 1.0, rotation: Dict[str, float] = None
) -> Tuple[pv.PolyData, pv.PolyData]:
    """[summary]

    [extended_summary]

    Args:
        spider (pv.PolyData): [description]
        box (pv.PolyData): [description]
        scale (float, optional): [description]. Defaults to 1.0.
        rotation (Dict[str, float], optional): [description]. Defaults to None.

    Returns:
        Tuple[pv.PolyData, pv.PolyData]: [description]
    """
    spider.points *= scale
    box.points *= scale

    if rotation is None:
        rotation = {}

    if "x" in rotation:
        spider.rotate_x(rotation["x"])
    if "y" in rotation:
        spider.rotate_y(rotation["y"])
    if "z" in rotation:
        spider.rotate_z(rotation["z"])

    return (spider, box)
