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


def update_game(access_token):
    """
    :return: Updates a game in the database
    """
    console.print("[italic yellow]Please enter a game ID[/italic yellow]")
    update_id = int(input())

    console.print(
        "[italic yellow]Enter the field that you wish to update (i.e. Name, Genre, Platform[/italic yellow]")
    update_field = input().lower()

    console.print(
        "[italic yellow]Enter the value you want to update with[/italic yellow]")
    update_value = input()

    # construct payload for request
    payload = json.dumps({
        "id": update_id,
        "field": update_field,
        "value": update_value
    })

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # display animation to show user that the request is being sent to the api
    with console.status(f"[purple]Now updating game ID: {update_id}... 🔎[/purple]") as status:
        r = requests.put(f'{apiUrl}/updateGame', headers=headers, data=payload)

    if r.status_code != 200:
        console.print(
            "[bold red]An error occurred - please try again![/bold red] 🛑")
    else:
        console.print("[bold green]Update complete! ✅[/bold green]")
        json_response = r.json()
        result = json_response.get('Game updated:')
        result = result.get('Game')
        print('New updated entry:')
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
