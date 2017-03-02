from src.output.DefaultOutput import DefaultOutput


class CliOutput(DefaultOutput):

    def frequencyUpdated(self, value):
        print("Frequency updated: ", value, " kHz\n")