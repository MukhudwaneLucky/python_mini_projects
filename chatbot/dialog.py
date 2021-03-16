import abc


class Dialog(abc.ABC):
    """
    A dialog listens for utterances, parses and interprets them, then updates its
    internal state. it can then formulate  a response on demand
    """

    def listen(self, text, response=True, **kwargs):
        """
        :param text: a text utterances is passed in and parsed
        :param response: interpret method determines how to respond
        :param kwargs:
        :return: if a response is requested, generate a text response
         based on the most recent input and current dialog state
        """
        # parse the input
        sents = self.parse(text)
        # interpret the input
        sents, confidence, kwargs = self.interpret(sents, **kwargs)
        # determine the response
        if response:
            reply = self.respond(sents, confidence, **kwargs)
        else:
            reply = None

        # return initiative
        return reply, confidence

    @abc.abstractmethod
    def parse(self, text):
        """
        every dialog might need its own parsing strategy
        some may need dependency vs constituency
        others may require regular expression or chunkers
        """
        return []

    @abc.abstractmethod
    def interpret(self, sents, **kwargs):
        """
        interprets the utterance passed in as a list of parsed sentences
        updates the internal state of the dialog, computes a confidence
        of the interpretation. may also return arguments specific to the response
        """
        return sents, 0.0, kwargs

    @abc.abstractmethod
    def respond(self, sents, confidence, **kwargs):
        """
        creates a response given the input utterances and the current state
        of the dialog, along with an arguments passed in from the listen
        or the interpret methods
        """
