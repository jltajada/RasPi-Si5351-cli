import click
from src.Model import Model
from src.output.CliOutput import CliOutput
from src.input.CliInput import CliInput

@click.command()
@click.option('-s', '--step', default=100, help="Step frequency")
@click.option('-f','--freq', prompt='Selected frequency[kHz]', help="Requested frequency in kHz.", type=int)
@click.option('-v','--verbose', is_flag=True, help="More verbose output")

@click.option('-i','--input', type=click.Choice(['cli']),help="Input method", required=True)
@click.option('-o','--output', type=click.Choice(['cli']), help="Output method", required=True)
def normalRun(step,freq,input,output,verbose):
    model = Model(freq, step)
    inputMethod, outputMethod = None, None

    if input=='cli':
        inputMethod = CliInput(model)

    if output=='cli':
        outputMethod = CliOutput()

    model.registerOutput(outputMethod)
    model.start()
    inputMethod.start()


if __name__ == '__main__':
    normalRun()
