# importing libraries
# import rich functions and classes
from rich.console import Console
from rich.panel import Panel
# import functions from files
from access_token import access_token
from delete_game import delete_game
from display_game import display_game
from find_game import find_game
from update_game import update_game
from add_game import add_game

# new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"


def main():
    """
    Main function
    """

    console.print(
        Panel.fit("Welcome to the Video Game API!", style="bold cyan"))
    token = access_token()

    while True:
        console.print(Panel.fit("[italic yellow]Please type the letters that are highlighted in green to access data from the API[/italic yellow]\n[bold green]D[/bold green]isplay games\n[bold green]F[/bold green]ind game\n[bold green]U[/bold green]pdate game\n[bold green]A[/bold green]dd game\n[bold green]De[/bold green]lete game\n[bold green]Q[/bold green]uit", title="Video Game API - Menu 🎮", subtitle="By Joshua Blewitt"))

        console.print("[brown]Enter your choice[/brown]")
        choice = input().upper()

        # it is a switch statement I swear
        if choice == 'D':
            display_game(token)
        elif choice == 'F':
            find_game(token)
        elif choice == 'U':
            update_game(token)
        elif choice == 'A':
            add_game(token)
        elif choice == 'DE':
            delete_game(token)
        elif choice == 'Q':
            console.print("[red]Goodbye![/red]")
            break
        else:
            console.print(
                "[bold red]Your command was invalid! Please try again![/bold red]")


if __name__ == "__main__":
    main()
