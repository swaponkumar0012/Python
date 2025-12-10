from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.tree import Tree
from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.style import Style
import time

# Graph Definition (from DFS.py)
graph = [
    [0, 1, 0, 1, 0],  # 0 connected to 1, 3
    [1, 0, 1, 0, 1],  # 1 connected to 0, 2, 4
    [0, 1, 0, 0, 0],  # 2 connected to 1
    [1, 0, 0, 0, 1],  # 3 connected to 0, 4
    [0, 1, 0, 1, 0]   # 4 connected to 1, 3
]
n = len(graph)
visited = [False] * n

# Rich UI Setup
console = Console()
layout = Layout()

layout.split_row(
    Layout(name="tree", ratio=1),
    Layout(name="info", ratio=1)
)

main_tree = Tree("[bold white]Start DFS(0)[/]")
visited_log = []

def generate_table():
    table = Table(title="Adjacency Matrix")
    table.add_column("Node", justify="center", style="bold cyan")
    for i in range(n):
        table.add_column(str(i), justify="center", width=3)
    
    for i in range(n):
        row = [str(i)]
        for j in range(n):
            style = "bold green" if graph[i][j] else "dim"
            row.append(f"[{style}]{graph[i][j]}[/]")
        table.add_row(*row)
    return table

def update_ui(current_node, status_msg):
    # Tree Panel
    layout["tree"].update(
        Panel(main_tree, title="Recursion Tree", border_style="green")
    )
    
    # Info Panel content
    info_text = Text()
    info_text.append(f"Current Node: {current_node}\n", style="bold yellow")
    info_text.append(f"Status: {status_msg}\n\n", style="bold white")
    info_text.append("Visited: " + str(visited_log), style="bold blue")
    
    layout["info"].update(
        Panel(
            console.render_str(f"{generate_table()}\n\n") + info_text,
            title="State",
            border_style="blue"
        )
    )

def dfs_recursive(u, tree_node):
    visited[u] = True
    visited_log.append(u)
    
    # Visual: Add node to tree
    current_node_branch = tree_node.add(f"[bold red]Node {u}[/]")
    update_ui(u, "Visiting...")
    time.sleep(1.0)
    
    for v in range(n):
        if graph[u][v] == 1:
            if not visited[v]:
                update_ui(u, f"Found neighbor {v}, recursing down...")
                time.sleep(0.8)
                dfs_recursive(v, current_node_branch)
                update_ui(u, f"Backtracked to {u} from {v}")
                time.sleep(0.8)
            else:
                # Optional: Show visited neighbors
                # current_node_branch.add(f"[dim]Node {v} (Visited)[/]")
                pass

if __name__ == "__main__":
    with Live(layout, refresh_per_second=4, console=console):
        update_ui(0, "Starting DFS...")
        time.sleep(1)
        dfs_recursive(0, main_tree)
        
        update_ui("-", "DFS Completed!")
        # Keep result on screen
        time.sleep(5)
