class DefaultOutput(object):



    def frequencyUpdated(self, value):
        pass


    def update(self, model):
        self.lastFreq = model.getFrequency()
        self.frequencyUpdated(self.lastFreq)
