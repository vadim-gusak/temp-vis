from temp_vis.data import get_mesh_data, load_temperatures
from temp_vis.temperatures import get_temperatures_by_points
from temp_vis.graphics import make_graphic


def start_visualization(stl_path: str, temperatures_path: str, opacity=1):
    print('Script starts')

    mesh_data = get_mesh_data(stl_path)
    temperatures_data_from_file = load_temperatures(temperatures_path)

    if (mesh_data is None) or (temperatures_data_from_file is None):
        print('Input files error!')
        return

    vertices, I, J, K = mesh_data
    x, y, z = vertices.T
    temperatures_by_points = get_temperatures_by_points(
        temperatures_data_from_file, x, y, z
    )

    data_for_graphic = x, y, z, I, J, K, temperatures_by_points, opacity
    make_graphic(data_for_graphic)
