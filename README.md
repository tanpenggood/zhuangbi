# Zhuangbi

Just for zhuangbi.

## Gif

```bash
python zhuangbi.py
```

![](./zhuangbi.gif)

## Feature

1. **黑客数字雨**：顶部持续滚动的绿色随机字符流
2. **随机进度条**：同时显示 3 个不同进度的任务
3. **伪日志系统**：随机生成警告/成功/调试信息
4. **ASCII艺术**：每隔 2 秒切换酷炫的 ASCII 图案
5. **跨平台支持**：完美兼容 Windows/Linux/MacOS 的终端
6. **优雅退出**：`Ctrl+C` 时显示终止提示

## Usage

1. **安装依赖** (需要 Python 3.7+)
   ```bash
   pip install rich
   ```

2. **运行程序**
   ```bash
   python zhuangbi.py
   ```
   或创建快捷命令：
   ```bash
   # Linux/MacOS
   echo 'alias zhuangbi="python /path/to/zhuangbi.py"' >> ~/.bashrc

   # Windows (PowerShell)
   New-Alias zhuangbi "python C:\path\to\zhuangbi.py"
   ```