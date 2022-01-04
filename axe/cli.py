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
    for x in response.json()["query"]["pages"].values():
        content = x["extract"]

        content = content.split('</p>')

        tags = re.compile("<.*?>")
        content = map(lambda x: re.sub(tags, " ", x), content)

        content = next(filter(lambda x: x and not x.isspace(), content)) # Have to use this method rather than relying on HTML paragaph tags to extract the first paragraph due to malformed HTML

        whitespace = re.compile(" +")
        content = re.sub(whitespace, " ", content)

        breaks = re.compile("\n")
        content = re.sub(breaks, "", content)

        click.echo(content)
