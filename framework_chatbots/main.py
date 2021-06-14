# import program modules
import abc


class Dialog(abc.ABC):
    """
        A Dialog listens for utterances, parses and interprets them,
        then updates its internal state. It can then formulate a
        response on demand.
    """

    def listen(self, text, response=True, **kwargs):
        """
            A text utterance is passed in and parsed. It is then passed to
            the interpret method to determine the response. If a response
            is requested, the respond method is used to generate a text
            response based on the most recent input and the current state.
            :param text     -> text as a string
            :param response -> a boolean indicating if initiative has passed to
                            the Dialog and a response is required. if False, Dialog
                            listens and updates internal state
            :param **kwargs   -> arbitrary keyword arguments which may contain other
                            contextual info like user, session id or transcription score
            :return a response if required, None if not, and a confidence score (0.0 - 1.0)
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
            Every dialog may need its own parsing strategy, some dialogs may need
            dependency vs constituency parses, others may simply require regular
            expressions or chunkers.
        :param text: a string as input
        :return: a list of data structures specific to the needs of the particular
                Dialog behavior
        """
        return []


# run
if __name__ == '__main__':
    print("Starting Chatbot...")
