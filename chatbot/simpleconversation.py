from collections.abc import Sequence
from operator import itemgetter

from dialog import Dialog


class SimpleConversation(Dialog, Sequence):
    """
    this is the most simple version of a conversation
    """
    def __init__(self, dialogs):
        self._dialogs = dialogs

    def __getitem__(self, idx):
        return self._dialogs[idx]

    def __len__(self):
        return len(self._dialogs)

    def listen(self, text, response=True, **kwargs):
        """
        simply return the best confidence response
        """
        responses = [
            dialog.listen(text, response, **kwargs)
            for dialog in self._dialogs
        ]
        return max(responses, key=itemgetter(1))

    def parse(self, text):
        return [dialog.parse(text) for dialog in self._dialogs]

    def interpret(self, sents, **kwargs):
        return [dialog.interpret(sents, **kwargs) for dialog in self._dialogs]

    def respond(self, sents, confidence, **kwargs):
        return [
            dialog.respond(sents, confidence, **kwargs)
            for dialog in self._dialogs
        ]
