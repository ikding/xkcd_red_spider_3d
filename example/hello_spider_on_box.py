"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/hello_spider_on_box.py
"""
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


def main() -> pv.Plotter:
    """Main function for rendering the 3D scene for spider on a box.

    Args:
        None

    Returns:
        pv.Plotter: pyvista plotter for plotting the 3D scene.
    """
    plotter = pv.Plotter()
    spider = get_unit_cell_spider()
    box = get_unit_cell_box()

    plotter.add_mesh(spider, color="red")  # spider
    plotter.add_mesh(box, color="tan", show_edges=True)  # box

    return plotter


if __name__ == "__main__":
    pv.set_plot_theme("document")
    p = main()
    p.show()
