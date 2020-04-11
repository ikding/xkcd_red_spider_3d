"""Utility function for making red spider on a box."""
import os
from typing import Dict, List, Tuple, Union

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


def process_spider_box_unit_cell(
    spider: pv.PolyData,
    box: pv.PolyData,
    scale: float = 1.0,
    rotation: List[Tuple[str, float]] = None,
    translation: List[Union[int, float]] = None,
) -> Tuple[pv.PolyData, pv.PolyData]:
    """[summary]

    [extended_summary]

    Args:
        spider (pv.PolyData): [description]
        box (pv.PolyData): [description]
        scale (float, optional): [description]. Defaults to 1.0.
        rotation (List[Tuple[str, float]], optional): [description]. Defaults to None.
        translation (List[Union[int, float]], optional): [description]. Defaults to None.

    Returns:
        Tuple[pv.PolyData, pv.PolyData]: [description]
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
