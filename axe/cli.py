import click
import re
import requests

@click.command()
@click.argument("question")
def cli(question):
    click.echo(parse_page(query(search(question))))

def search(question):
    parameters = {
        "action": "opensearch",
        "format": "json",
        "search": question,
    }

    response = requests.get("https://en.wikipedia.org/w/api.php", params=parameters)

    if(len(response.json()[1]) == 1):
        return response.json()[1][0]

    for index, value in enumerate(response.json()[1]):
        click.echo(f"{index + 1}) {value}")

    input_value = click.prompt("Please enter the corresponding number of the article you want to choose", type=int)
    return response.json()[1][input_value - 1]

def query(title):
    parameters = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
    }
    
    response = requests.get("https://en.wikipedia.org/w/api.php", params=parameters)
    return list(response.json()["query"]["pages"].values())[0]["extract"]

def parse_page(extract):
    extract = extract.split('</p>')

    tags = re.compile("<.*?>")
    extract = map(lambda x: re.sub(tags, " ", x), extract)

    extract = next(filter(lambda x: x and not x.isspace(), extract)) # Have to use this method rather than relying on HTML paragaph tags to extract the first paragraph due to malformed HTML

    whitespace = re.compile(" +")
    extract = re.sub(whitespace, " ", extract)

    breaks = re.compile("\n")
    extract = re.sub(breaks, "", extract)

    return extract
