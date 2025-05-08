import mujoco
import numpy as np
from PIL import Image

model = mujoco.MjModel.from_xml_path('adam_lite/scene.xml')
data = mujoco.MjData(model)

width, height = 512, 3072
renderer = mujoco.Renderer(model, height, width)

cam = mujoco.MjvCamera()
cam.azimuth = 160
cam.elevation = -20
cam.distance = 4
cam.lookat[:] = [-1.5, 0.5, 0.3]

mujoco.mj_forward(model, data)

renderer.update_scene(data, camera=cam)
image = renderer.render()

img = Image.fromarray(image)
img.save('adam.png')