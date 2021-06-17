# import program modules
import abc
from collections.abc import Sequence
from operator import itemgetter

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
            :param text: text as a string
            :param response: a boolean indicating if initiative has passed to
                            the Dialog and a response is required. if False, Dialog
                            listens and updates internal state
            :param kwargs: arbitrary keyword arguments which may contain other
                            contextual info like user, session id or transcription score
            :return: a response if required, None if not, and a confidence score (0.0 - 1.0)
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

    @abs.abstractmethod
    def interpret(self, sents, **kwargs):
        """
            Interprets the utterance passed in as a list of parsed sentences,
            updates the internal state of the dialog, computes a confidence
            of the interpretation. May also return arguments specific to the
            response mechanism.
        :param sents: an incoming list of parsed sentences
        :param kwargs: arbitrary keyword arguments
        :return: interpreted parsed sentences that have been filtered based
                whether they require a response, a confidence score, updated
                keyword arguments to influence respond method
        """
        return sents, 0.0, kwargs

    @abs.abstractmethod
    def respond(self, sents, confidence, **kwargs):
        """
            Creates a response given the input utterances and the current
            state of the dialog, along with any arguments passed in from
            the listen or the interpret methods.
        :param sents:       interpreted sentences
        :param confidence:  a confidence score
        :param kwargs:      arbitrary keyword arguments
        :return: a text-based response
        """
        return None


class SimpleConversation(Dialog, Sequence):
    """
        Simple version of a conversation. Inherits the behaviour of
        Dialog class. Main role is to maintain state across a sequence
        of dialogs.
    """

    def __init__(self, dialogs):
        self._dialogs = dialogs

    def __getitem__(self, idx):
        return self._dialogs[idx]

    def __len__(self):
        return len(self._dialogs)

    def listen(self, text, response=True, **kwargs):
        """
            Returns the best confidence response. The result is a list of
            (responses, confidence) tuples. The SimpleConversation will
            simply return the response with the highest confidence by
            using the itemgetter operator to retrieve the max by the
            second element of the tuple.
        """
        responses = [
            dialog.listen(text, response, **kwargs)
            for dialog in self._dialogs
        ]
        # responses is a list of (response, confidence) pairs
        return max(responses, key=itemgetter(1))

# run
if __name__ == '__main__':
    print("Starting Chatbot...")
