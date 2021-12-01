#importing libraries
import requests
import json
from rich import columns
from rich import panel
from rich.console import Console
from rich.panel import Panel
from rich import inspect

#new console object
console = Console()

# variable for URL to API
apiUrl = "https://mighty-cliffs-81365.herokuapp.com/"

def main():
    """
    Main function
    """

    console.print(Panel.fit("Welcome to the Video Game API!", style="bold cyan"))
    token = access_token()

    console.print(Panel.fit("Hello, [red]World!", title="Welcome", subtitle="Thank you"))


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

        console.print("[italic yellow]Now logging into the Video Game API...[/italic yellow]")
        console.print("[bold red]If this is the first time you are logging in - it might be slow![/bold red]")
        
        #display animation to show user that the credentials are being sent to the api
        with console.status("[purple]Logging in...[/purple]") as status:
            r = requests.post(f'{apiUrl}/login', headers=headers_login, data=payload)

        if r.status_code == 200:
            #get access token from response
            json_response = r.json()
            inspect(json_response, docs=False)
            return json_response['access_token']
        else:
            console.print("[bold red]Login failed! Please try again![/bold red]")


if __name__ == "__main__":
    main()