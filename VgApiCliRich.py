#importing libraries
import requests
import json
#import rich functions and classes
from rich import columns
from rich import panel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
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

    while True:
        console.print(Panel.fit("[italic yellow]Please type the letters that are highlighted in green to access data from the API[/italic yellow]\n[bold green]D[/bold green]isplay games\n[bold green]F[/bold green]ind game\n[bold green]U[/bold green]pdate game\n[bold green]A[/bold green]dd game\n[bold green]De[/bold green]lete game\n[bold green]Q[/bold green]uit", title="Video Game API - Menu 🎮", subtitle="By Joshua Blewitt"))

        console.print("[brown]Enter your choice[/brown]")
        choice = input().upper()
        
        #it is a switch statement I swear
        if choice == 'D':
            display_game(token)
        elif choice == 'F':
            print("Find game")
        elif choice == 'U':
            print("Update game")
        elif choice == 'A':
            print("Add game")
        elif choice == 'DE':
            print('Delete game')
        elif choice == 'Q':
            console.print("[red]Goodbye![/red]")
            break
        else:
            console.print("[bold red]Your command was invalid! Please try again![/bold red]")

def decode_json(json_data):
    """
    :param json_data:
    :return:
    Decodes JSON response from API
    """

    #make a new table
    table = Table(show_header=True, header_style="bold magenta")

    #configure table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=12)
    table.add_column("Genre")
    table.add_column("Name", justify="right")
    table.add_column("Platform", justify="right")
    table.add_column("Publisher", justify="right")
    table.add_column("Year", justify="right")

    # decode JSON
    json_response = json_data.json()
    games = json_response.get('Games')

    # iterate through response
    for i in range(len(games)):
        new_dict = games[i]['Game']
        print(f"{new_dict['ID: ']}, {new_dict['Genre: ']}, {new_dict['Name: ']}, {new_dict['Platform: ']}, {new_dict['Publisher: ']}, {new_dict['Year']}")
        table.add_row(f"{new_dict['ID: ']}", f"{new_dict['Genre: ']}", f"{new_dict['Name: ']}", f"{new_dict['Platform: ']}", f"{new_dict['Publisher: ']}", f"{new_dict['Year']}")
    console.print(table)
    enter = input("Press any key to continue...")

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

def display_game(access_token):
    """
    :param:
    The access token from the API when logging in
    :return:
    Shows games that are on the API
    """

    print('Fetching games from the API...')

    # construct headers
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    #display animation to show user that the request is being sent to the api
    with console.status("[purple]Fetching games...[/purple]") as status:
        r = requests.get(f'{apiUrl}/displayGames', headers=headers)
    
    decode_json(r)


if __name__ == "__main__":
    main()