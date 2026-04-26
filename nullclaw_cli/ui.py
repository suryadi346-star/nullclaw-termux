from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def display_welcome():
    console.print(Panel(
        "[bold cyan]NullClaw AI[/bold cyan] v1.0.0\n"
        "[dim]Terminal AI Assistant for Termux (No Proot)[/dim]\n"
        "[yellow]Commands: exit | clear[/yellow]",
        title="[bold green]🐾 Welcome[/bold green]",
        border_style="green"
    ))

def display_response(text: str):
    console.print(Markdown(text), style="cyan")
