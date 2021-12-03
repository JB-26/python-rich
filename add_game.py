#importing libraries
import requests
import json
#import rich functions and classes
from rich.console import Console
from rich.table import Table

#new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"

def add_game(access_token):
    """
    :param access_token:
    :return: Adds a game to the database
    """

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    console.print("[italic yellow]Please enter the following details[/italic yellow]")

    console.print("[yellow]Enter the [bold]name[/bold] of the game[/yellow]")
    add_name = input()

    console.print("[yellow]Enter the [bold]platform[/bold] of the game[/yellow]")
    add_platform = input()

    console.print("[yellow]Enter the [bold]publisher[/bold] of the game[/yellow]")
    add_publisher = input()

    console.print("[yellow]Enter the [bold]genre[/bold] of the game[/yellow]")
    add_genre = input()

    console.print("[yellow]Enter the [bold]year[/bold] when the game was released[/yellow]")
    add_year = int(input())

    # construct payload for request
    payload = json.dumps({
        "name": add_name,
        "platform": add_platform,
        "publisher": add_publisher,
        "genre": add_genre,
        "year": add_year
    })

    with console.status(f"[purple]Now adding {add_name}... 🎮[/purple]") as status:
        r = requests.post(f'{apiUrl}/addGame', headers=headers, data=payload)
    
    if r.status_code != 201:
        console.print("[bold red]An error occurred - please try again![/bold red] 🛑")
    else:
        console.print("[green]The following has been added![/green]")
        #make a new table
        table = Table(show_header=True, header_style="bold magenta")

        #configure table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name", justify="center")
        table.add_column("Genre", justify="center")
        table.add_column("Platform", justify="center")
        table.add_column("Publisher", justify="center")
        table.add_column("Year", justify="center")

        table.add_row(f"{add_name}", f"{add_genre}", f"{add_platform}", f"{add_publisher}", f"{add_year}")
        console.print(table)
        enter = input("Press any key to continue...")