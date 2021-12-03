# importing libraries
import requests
import json
# import rich functions and classes
from rich.console import Console
from rich.table import Table

# new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"


def delete_game(access_token):
    """
    :return:
    Deletes a game from the database
    """

    console.print(
        "[yellow]Enter the [bold]ID[/bold] of the game in the database you want to delete[/yellow]")
    console.print(
        "[bold red]WARNING! This will remove the game and cannot be recovered![/bold red]")
    delete_id = int(input())
    # construct payload for request
    payload = json.dumps({
        "id": delete_id
    })

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    with console.status(f"[purple]Now deleting Game ID: {delete_id}... 🎮[/purple]") as status:
        r = requests.delete(f'{apiUrl}/deleteGame',
                            headers=headers, data=payload)

    if r.status_code != 200:
        console.print(
            "[bold red]An error occurred - please try again![/bold red] 🛑")
    else:
        console.print('[red]Game deleted![/red]')
        json_response = r.json()
        result = json_response.get('The following has been deleted')
        result = result.get('Game')
        print('The following has been deleted from the database:')
        # make a new table
        table = Table(show_header=True, header_style="bold magenta")

        # configure table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=12)
        table.add_column("Name", justify="center")
        table.add_column("Genre", justify="center")
        table.add_column("Platform", justify="center")
        table.add_column("Publisher", justify="center")
        table.add_column("Year", justify="center")

        table.add_row(f"{result['ID: ']}", f"{result['Name: ']}", f"{result['Genre: ']}",
                      f"{result['Platform: ']}", f"{result['Publisher: ']}", f"{result['Year']}")

        console.print(table)
        check = input('Enter any key to continue')
