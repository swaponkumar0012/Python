from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich import box
import time

def binary_search_visualized(arr, x):
    low = 0
    high = len(arr) - 1
    
    console = Console()
    
    # Create the layout
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    
    layout["header"].update(Panel(Align.center("[bold cyan]Binary Search Visualization[/bold cyan]"), style="blue"))

    step = 0
    
    with Live(layout, refresh_per_second=4, console=console) as live:
        while low <= high:
            step += 1
            mid = (low + high) // 2
            
            # Create the Visual Array
            table = Table(box=box.ROUNDED, show_header=False, show_edge=False, pad_edge=False)
            
            # Add columns for each element
            for _ in arr:
                table.add_column(justify="center", width=4)
            
            # 1. Row: Indicators (Low/High/Mid)
            indicators = []
            for i in range(len(arr)):
                if i == mid:
                    indicators.append("[bold yellow]M[/]")
                elif i == low:
                    indicators.append("[bold green]L[/]")
                elif i == high:
                    indicators.append("[bold red]H[/]")
                else:
                    indicators.append(" ")
            table.add_row(*indicators)

            # 2. Row: Array Values
            values = []
            for i, val in enumerate(arr):
                style = "white"
                if i == mid:
                    style = "bold white on blue" # Highlight Mid
                elif low <= i <= high:
                    style = "cyan" # Search space
                else:
                    style = "dim white" # Ignored space
                
                values.append(f"[{style}]{val}[/]")
            table.add_row(*values)
            
            # 3. Row: Indices
            indices = [f"[dim]{i}[/]" for i in range(len(arr))]
            table.add_row(*indices)
            
            # Update Layout
            narrative = f"""Step {step}:
Searching range: [{low}, {high}]
Mid point: {mid} (Value: {arr[mid]})
Target: {x}

[bold]{'Found!' if arr[mid] == x else f'{arr[mid]} < {x}, look right...' if arr[mid] < x else f'{arr[mid]} > {x}, look left...'}[/bold]
"""
            
            layout["main"].update(
                Panel(
                    Align.center(table),
                    title=f"Step {step}",
                    border_style="green"
                )
            )
            layout["footer"].update(Panel(narrative, title="Log"))
            
            time.sleep(1.5) # Pause to let user see
            
            if arr[mid] == x:
                layout["footer"].update(Panel(f"[bold green]Target {x} found at index {mid}![/]", title="Success", style="green"))
                time.sleep(2)
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                
        # Not found
        layout["main"].update(Panel(Align.center("[bold red]Element not found[/]"), title="Result", border_style="red"))
        time.sleep(2)
        return -1

if __name__ == "__main__":
    # Example Data
    data = [1, 3, 5, 7, 9, 11, 13, 20]
    target = 13
    
    # Run
    binary_search_visualized(data, target)
