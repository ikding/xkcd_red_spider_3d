"""Get a simple building."""
import os

import pyvista as pv

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


def get_buildings() -> pv.PolyData:
    """Return a set of buildings, which was downloaded from sketchfab and saved
    in project file.

    Returns:
        pv.PolyData: ``pv.Polydata`` containing the buildings.
    """
    default_buildings = pv.read(
        os.path.join(
            DATA_DIR, "buildings-and-skyscrapers", "source", "buildings.obj"
        )
    )
    default_buildings.rotate_x(90)
    default_buildings.translate([-4, -4, 0])
    return default_buildings


def main(color_buildings="lightgray") -> pv.Plotter:
    """Main function for rendering the 3D scene.

    Args:
        color_buildings (str, optional): color of the buildings. Defaults to
        "lightgray".

    Returns:
        pv.Plotter: pyvista plotter for plotting the 3D scene.
    """
    plotter = pv.Plotter()
    buildings = get_buildings()
    buildings.points *= 1
    buildings.translate([0, 0, -10])
    plotter.add_mesh(buildings, color=color_buildings, show_edges=True)

    return plotter


if __name__ == "__main__":
    pv.set_plot_theme("document")
    p = main()
    p.show()
