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


# run
if __name__ == '__main__':
    print("Starting Chatbot...")
