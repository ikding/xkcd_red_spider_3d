"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/hello_spider_army.py
"""
from typing import List, Tuple, Union

import pyvista as pv
from pyvista import examples


def get_unit_cell_box() -> pv.PolyData:
    """Return a box unit. The box has length 1 in all 3 dimensions, and is
    centered at the origin.

    Having the box centered at origin will make it easier for rotating the
    spider on a box.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the box unit.
    """
    default_box = pv.Box()
    default_box.points /= 2
    return default_box


def get_unit_cell_spider() -> pv.PolyData:
    """Return a spider unit. The spider has legspan that is slightly smaller
    than the box face, and is in a position so it appears to be standing on the
    box unit.

    Having the spider unit standing on the box centered at origin will make it
    easier for rotating the spider on a box.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the spider unit.
    """
    default_spider = examples.download_spider()
    default_spider.points /= 6
    default_spider.translate([-0.5, -0.5, 0.4])
    default_spider.rotate_z(-110)
    return default_spider


def process_spider_box_unit_cell(
    spider: pv.PolyData = get_unit_cell_spider(),
    box: pv.PolyData = get_unit_cell_box(),
    scale: float = 1.0,
    rotation: List[Tuple[str, float]] = None,
    translation: List[Union[int, float]] = None,
) -> Tuple[pv.PolyData, pv.PolyData]:
    """Process the spider-box unit cell through operations including scaling,
    rotations, and translations.

    Args:
        spider (pv.PolyData, optional): Polydata containing the spider unit.
            Defaults to get_unit_cell_spider().
        box (pv.PolyData, optional): Polydata containing the box unit. Defaults
            to get_unit_cell_box().
        scale (float, optional): scaling factor. Defaults to 1.0.
        rotation (List[Tuple[str, float]], optional): list of steps for
            rotation, in the form of list of tuples, and the tuple containing
            the direction (``"x"``, ``"y"``, or ``"z"``) in the first element,
            and the degrees in the second direction. Example:
            ``[("x", 90), ("z", 180)]``. Under the hood, the
            `rotate_x <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_x>`_,
            `rotate_y <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_y>`_, and
            `rotate_z <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_z>`_
            methods in ``pv.PolyData`` are called. Defaults to None.
        translation (List[Union[int, float]], optional): Length of 3 list or
            array to translate the polydata. Under the hood, the
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


def main() -> pv.Plotter:
    """Main function for rendering the 3D scene for spider on a box.

    Args:
        None

    Returns:
        pv.Plotter: pyvista plotter for plotting the 3D scene.
    """
    plotter = pv.Plotter()
    spider_1, box_1 = process_spider_box_unit_cell(
        spider=get_unit_cell_spider(), box=get_unit_cell_box(), scale=1.0
    )
    spider_2, box_2 = process_spider_box_unit_cell(
        spider=get_unit_cell_spider(),
        box=get_unit_cell_box(),
        scale=1.2,
        rotation=[("y", 90)],
        translation=[2, 0, 0],
    )
    spider_3, box_3 = process_spider_box_unit_cell(
        spider=get_unit_cell_spider(),
        box=get_unit_cell_box(),
        scale=1.4,
        rotation=[("x", 90)],
        translation=[4, 0, 0],
    )
    spider_4, box_4 = process_spider_box_unit_cell(
        spider=get_unit_cell_spider(),
        box=get_unit_cell_box(),
        scale=1.6,
        rotation=[("z", 90)],
        translation=[6, 0, 0],
    )

    plotter.add_mesh(spider_1, color="red")
    plotter.add_mesh(spider_2, color="red")
    plotter.add_mesh(spider_3, color="red")
    plotter.add_mesh(spider_4, color="red")

    plotter.add_mesh(box_1, color="tan")
    plotter.add_mesh(box_2, color="tan")
    plotter.add_mesh(box_3, color="tan")
    plotter.add_mesh(box_4, color="tan")

    return plotter


if __name__ == "__main__":
    pv.set_plot_theme("document")
    p = main()
    p.show()
