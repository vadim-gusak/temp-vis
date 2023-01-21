from plotly import graph_objects


def make_graphic(data_for_graphic):
    x, y, z, I, J, K, temperatures, opacity = data_for_graphic

    mesh3D = graph_objects.Mesh3d(
        x=x,
        y=y,
        z=z,
        i=I,
        j=J,
        k=K,
        flatshading=True,
        colorbar_title='Temperature',
        color='gold',
        intensity=temperatures,
        showscale=True,
        opacity=opacity
    )

    layout = graph_objects.Layout(paper_bgcolor='rgb(112,112,112)',
                                  title_text='TEST',
                                  title_x=0.5,
                                  font_color='white',
                                  width=1600,
                                  height=800,
                                  scene_camera=dict(
                                      eye=dict(x=2.25, y=-2.25, z=1)
                                  ),
                                  scene_xaxis_visible=False,
                                  scene_yaxis_visible=False,
                                  scene_zaxis_visible=False,
                                  scene=dict(aspectratio=dict(
                                      x=4,
                                      y=1,
                                      z=1
                                  )))

    fig = graph_objects.Figure(data=[mesh3D], layout=layout)
    fig.show()
