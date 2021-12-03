#importing libraries
import requests
import json
#import rich functions and classes
from rich.console import Console
#import files
from decode_json import decode_json

#new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"

def find_game(access_token):
    """
    :return:
    User enters a search term. The API will return data if there is a match.
    """
    console.print("[italic yellow]Please enter a search term[/italic yellow]")
    search_term = input()

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # construct payload for request
    payload = json.dumps({
        "name": search_term
    })

    #display animation to show user that the request is being sent to the api
    with console.status(f"[purple]Now searching for {search_term}... 🔎[/purple]") as status:
        r = requests.get(f'{apiUrl}/findGame', headers=headers, data=payload)

    if r.status_code != 200:
        console.print("[bold red]No games found![/bold red] 🤷‍♂️ [bold red]Please try again![/bold red]")
        enter = input("Press any key to continue...")
    else:
        decode_json(r)