"""Main script to kick off a pyvista 3D visualization window.

To run::
    python xkcd_red_spider/hello_spider.py
"""
import pyvista as pv
from pyvista import examples


if __name__ == "__main__":
    pv.set_plot_theme("document")
    plotter = pv.Plotter()
    spider = examples.download_spider()

    plotter.add_mesh(spider, color="red")  # spider
    plotter.show()
