#importing libraries
import requests
import json
#import rich functions and classes
from rich.console import Console
from rich import inspect

#new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"

def access_token():
    """
    :return:
    The JWT from the API to access endpoints
    """
    while True:
        console.print("Please enter the [bold red]username[/bold red]")
        username = input()

        console.print("Please enter the [bold red]password[/bold red]")
        password = input()

        #construct payload for request
        payload = json.dumps({
            "username": username,
            "password": password
        })

        #construct headers
        headers_login = {
            'Content-Type': 'application/json'
        }

        console.print("[bold red]If this is the first time you are logging in - it might be slow![/bold red]")

        #display animation to show user that the credentials are being sent to the api
        with console.status("[purple]Logging in...[/purple]") as status:
            r = requests.post(f'{apiUrl}/login', headers=headers_login, data=payload)

        if r.status_code == 200:
            #get access token from response
            json_response = r.json()
            inspect(json_response, docs=False)
            console.print("[bold green]Success! :clap:[/bold green]")
            return json_response['access_token']
        else:
            console.print("[bold red]Login failed![/bold red] 🛑 [bold red]Please try again![/bold red]")
