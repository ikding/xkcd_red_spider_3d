"""Utility function for making red spider on a box."""
import os
from typing import Dict, Tuple

import numpy as np
import pyvista as pv
from pyvista import examples


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


def get_unit_cell_spider() -> pv.PolyData:
    # default_spider = examples.download_spider()
    default_spider = pv.read(os.path.join(DATA_DIR, "spider.ply"))
    default_spider.points /= 3
    default_spider.translate([-1, -1, 0.8])
    default_spider.rotate_z(-110)
    return default_spider


def get_unit_cell_box() -> pv.PolyData:
    default_box = pv.Box()
    return default_box


def get_buildings() -> pv.PolyData:
    default_buildings = pv.read(
        os.path.join(DATA_DIR, "buildings-and-skyscrapers", "source", "buildings.obj")
    )
    default_buildings.rotate_x(90)
    default_buildings.translate([-4, -4, 0])
    return default_buildings


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
