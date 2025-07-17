# Pi5-BuzzLab-tools

本仓库演示如何在 **树莓派&nbsp;Pi&nbsp;5** 上驱动蜂鸣器。

示例不依赖 `gpiozero`，而是直接使用 `lgpio` 库控制 GPIO。

## 接线说明

示例使用带有三根线的蜂鸣器（VCC、GND、Signal）。

- **VCC**：接树莓派的 5V 引脚（例如物理引脚&nbsp;2 或 4）
- **GND**：接树莓派的任意 GND 引脚（例如物理引脚&nbsp;6）
- **Signal**：连接到用于控制的 GPIO 引脚（示例代码默认为物理引脚&nbsp;11，对应 GPIO17）

仓库中的 `doc/device.jpg` 提供了典型的接线示意图，可供参考。

## 环境准备

建议在虚拟环境中安装依赖并使用 `lgpio` 控制蜂鸣器：

```bash
python3 -m venv venv
source venv/bin/activate
pip install lgpio
```

完成上述步骤后即可运行示例。

## 运行方式

在命令行中运行示例，指定蜂鸣次数、间隔以及 GPIO 引脚：

```bash
python3 main.py --times 3 --interval 0.5 --pin 17
```

其中 `--times` 表示蜂鸣的次数，`--interval` 表示两次蜂鸣之间的间隔秒数，`--pin` 指定蜂鸣器连接到的 GPIO 引脚（默认 17）。
