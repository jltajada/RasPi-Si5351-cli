import click
from src.input.DefaultInput import DefaultInput

class CliInput(DefaultInput):

    def start(self):
        while True:
            click.echo("Waiting for pressing h or l or q to abort...")
            c = click.getchar()
            click.echo()
            if c == 'h':
                self.down()
            elif c == 'l':
                self.up()
            else:
                click.echo("Abort!")
                break


