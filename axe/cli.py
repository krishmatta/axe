import click

@click.command()
@click.argument("question")
def cli(question):
    click.echo(question)
