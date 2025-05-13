# pnd_models

PNDbotics model files (urdf/mjcf + meshes, etc)

### 连杆翻转问题

如果您使用了wiki中提供的RL例程
请确认urdf中toe_left 以及 toe_right中的为以下值  
collision name="toe_*"  
origin rpy="1.57 0 0" xyz="0 0 0"  
请在isaac_gym的代码里 *_config 中的
`flip_visual_attachments = False`改为`flip_visual_attachments = True`  

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

