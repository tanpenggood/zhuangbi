import sys
import random
import signal
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from rich.live import Live

console = Console()
running = True

def handle_signal(signum, frame):
    global running
    running = False
    console.print("\n[red]Zhuangbi process terminated![/red]")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

# --------------------------
# 各种装逼效果组件
# --------------------------
def hacker_matrix():
    """黑客帝国数字雨效果"""
    chars = "01ABCDEF%&*^%$"
    while running:
        console.print(
            "".join(random.choice(chars) for _ in range(80)),
            style="bold green",
            end="\r"
        )
        sleep(0.1)

def progress_effect():
    """随机进度条效果"""
    with Progress(transient=True) as progress:
        tasks = [
            progress.add_task(f"[cyan]Hacking {random.choice(['FBI', 'Pentagon', 'NASA'])}...", total=100)
            for _ in range(3)
        ]
        while running:
            for task in tasks:
                progress.update(task, advance=random.uniform(0.1, 2))
            sleep(0.1)

def fake_logs():
    """伪代码日志"""
    logs = [
        ("DEBUG", "Decrypting mainframe..."),
        ("WARNING", "Firewall detected! Bypassing..."),
        ("INFO", "Injecting [red]Trojan.exe[/red]"),
        ("SUCCESS", "Root access granted!")
    ]
    while running:
        level, msg = random.choice(logs)
        console.print(f"[{level}] {msg}", style={
            "DEBUG": "dim",
            "WARNING": "yellow",
            "INFO": "blue",
            "SUCCESS": "bold green"
        }[level])
        sleep(random.uniform(0.2, 1.5))

def ascii_art():
    """随机ASCII艺术"""
    arts = [
        r"""
         _    _ _    _ __  __
        | |  | | |  | |  \/  |
        | |__| | |  | | \  / |
        |  __  | |  | | |\/| |
        | |  | | |__| | |  | |
        |_|  |_|\____/|_|  |_|
        """,
        r"""
        ░█▀▀░█▀█░█▀▀░█▀▀░▀█▀
        ░█▀▀░█░█░█▀▀░█▀▀░░█░
        ░▀░░░▀▀▀░▀▀▀░▀░░░▀▀▀
        """
    ]
    with Live(console=console, refresh_per_second=2) as live:
        while running:
            live.update(Panel(random.choice(arts), style="bold purple"))
            sleep(2)

# --------------------------
# 主程序
# --------------------------
def zhuangbi_start():
    console.print("[bold red]Initializing Zhuangbi System...[/bold red]\n")
    with ThreadPoolExecutor() as executor:
        executor.submit(hacker_matrix)
        executor.submit(progress_effect)
        executor.submit(fake_logs)
        executor.submit(ascii_art)
        while running:
            sleep(0.1)

if __name__ == "__main__":
    zhuangbi_start()
