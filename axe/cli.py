import click
import re
import requests

@click.command()
@click.argument("question")
def cli(question):
    parameters = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": question,
    }

    response = requests.get("https://en.wikipedia.org/w/api.php", params=parameters)
    click.echo(parse_page(list(response.json()["query"]["pages"].values())[0]["extract"]))

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
