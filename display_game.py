# importing libraries
import requests
# import rich functions and classes
from rich.console import Console
#import files
from decode_json import decode_json

# new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"


def display_game(access_token):
    """
    :param:
    The access token from the API when logging in
    :return:
    Shows games that are on the API
    """

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # display animation to show user that the request is being sent to the api
    with console.status("[purple]Fetching games...[/purple]") as status:
        r = requests.get(f'{apiUrl}/displayGames', headers=headers)

    decode_json(r)
