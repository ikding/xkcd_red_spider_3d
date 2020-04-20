"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/main.py
"""
import os

import pyvista as pv

import xkcd_red_spider.utils as utils


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


# A nice default camera position that I found manually
DEFAULT_CAMERA_POSITION = [(-0.7, -26.7, -7.3), (-0.47, 0, -4.6), (0, -0.1, 1)]


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
    # Use this line for high fidelity reproduction of comic
    spider_army = utils.get_xkcd_spider_army()
    # use this line for randomly-generated coords
    # spider_army = utils.get_xkcd_spider_army(
    #     spider_army_coord=utils.generate_random_spider_army_coord()
    # )

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
    if not os.path.isfile(vtkjs_file_path + ".vtkjs"):
        p.export_vtkjs(vtkjs_file_path)
    p.show()
    print(p.camera_position)  # print the final camera position to the stdout
