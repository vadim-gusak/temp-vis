import json
from stl.mesh import Mesh
import numpy


def get_mesh_data(path: str):
    try:
        mesh = Mesh.from_file(path)
    except (FileNotFoundError, TypeError) as e:
        print(e)
        mesh = None

    return stl2mesh3d(mesh)


def stl2mesh3d(stl_mesh):
    p, q, r = stl_mesh.vectors.shape
    vertices, ixr = numpy.unique(
        stl_mesh.vectors.reshape(p * q, r), return_inverse=True, axis=0
    )
    I_ = numpy.take(ixr, [3 * k for k in range(p)])
    J = numpy.take(ixr, [3 * k + 1 for k in range(p)])
    K = numpy.take(ixr, [3 * k + 2 for k in range(p)])

    return vertices, I_, J, K


def load_temperatures(path: str):
    try:
        with open(path, 'r') as f:
            data = f.read()
    except FileNotFoundError as e:
        print(e)
        return None

    try:
        temperatures_map = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print(e)
        return None

    return temperatures_map
