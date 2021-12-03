#importing libraries
#import rich functions and classes
from rich.table import Table
from rich.console import Console

#new console object
console = Console()

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
    table.add_column("Name", justify="center")
    table.add_column("Genre", justify="center")
    table.add_column("Platform", justify="center")
    table.add_column("Publisher", justify="center")
    table.add_column("Year", justify="center")

    # decode JSON
    json_response = json_data.json()
    games = json_response.get('Games')

    # iterate through response
    for i in range(len(games)):
        new_dict = games[i]['Game']
        #add response to table
        table.add_row(f"{new_dict['ID: ']}", f"{new_dict['Name: ']}", f"{new_dict['Genre: ']}", f"{new_dict['Platform: ']}", f"{new_dict['Publisher: ']}", f"{new_dict['Year']}")
    console.print(table)
    enter = input("Press any key to continue...")