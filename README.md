## 🔧 pnd_models

This repository contains PNDbotics model files for simulation and control, including URDF/MJCF descriptions, mesh assets, and more.

---

### ⚠️ Link Orientation Notice (Toe Link Flip Issue)

If you're using the reinforcement learning (RL) examples provided in our [Wiki documentation](https://your.wiki.url), please double-check the following to ensure correct simulation behavior:

#### ✅ URDF Configuration

In the `toe_left` and `toe_right` link definitions, make sure the following configuration is set:

```xml
<collision name="toe_*">
  <origin rpy="1.57 0 0" xyz="0 0 0"/>
</collision>
```

This orientation ensures the correct alignment of toe links in simulation.

#### ✅ Isaac Gym Configuration

In the corresponding `*_config.py` file used for Isaac Gym training, be sure to set:

```python
flip_visual_attachments = True
```

> The default value is `False`, which may cause visual misalignment of the toe components in some models.

---

## models

| model name     | mujoco image                                                      |
| -------------- | ----------------------------------------------------------------- |
| adam_inspire   | ![adam_inspire image](./adam_inspire/imgs/adam_inspire.png)       |
| adam_lite      | ![adam_lite image](./adam_lite/imgs/adam_lite.png)                |
| adam_lite_agx  | ![adam_lite_agx image](./adam_lite_agx/imgs/adam_lite_agx.png)    |
| adam_sp        | ![adam_sp image](./adam_sp/imgs/adam_sp.png)                      |
| adam_sp_agx_ir | ![adam_sp_agx_ir image](./adam_sp_agx_ir/imgs/adam_sp_agx_ir.png) |
| adam_standard  | ![adam_standard image](./adam_standard/imgs/adam_standard.png)    |
| adam_u         | ![adam_u image](./adam_u/imgs/adam_u.png)                         |

## FAQ

