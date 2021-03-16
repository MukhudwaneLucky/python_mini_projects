import re

from dialog import Dialog


class Greeting(Dialog):
    """
    keeps track of the participants entering or leaving the conversation
    and responds with appropriate salutations. this is an example of rules
     based system that keeps track of state and uses regular expressions
      and logic to handle the dialog
    """

    PATTERNS = {
        'greeting': r'hello|hi|hey|good morning|good evening',
        'introduction': r'my name is ([a-z\-\s]+)',
        'goodbye': r'goodbye|bye|ttyl',
        'rollcall': r'roll call|who\'s here?',
    }

    def __init__(self, participants=None):
        self.participants = {}

        if participants is not None:
            for participant in participants:
                self.participants[participant] = None

        self._patterns = {
            key: re.compile(pattern, re.I)
            for key, pattern in self.PATTERNS.items()
        }

    def parse(self, text):
        matches = {}
        for key, pattern in self._patterns.items():
            match = pattern.match(text)
            if match is not None:
                matches[key] = match
        return matches

    def interpret(self, sents, **kwargs):
        if len(sents) == 0:
            return sents, 0.0, kwargs

        user = kwargs.get('user', None)

        if 'introduction' in sents:
            name = sents['introduction'].groups()[0]
            user = user or name.lower()
            # determine if name has changed
            if user not in self.participants or self.participants[user] != name:
                kwargs['name_changed'] = True
            # update the participants
            self.participants[user] = name
            kwargs['user'] = user
        # determine if a greeting has been made
        if 'greeting' in sents:
            # if we don't have a name for the user
            if not self.participants.get(user, None):
                kwargs['request_introduction'] = True
        # determine if goodbye has been made
        if 'goodbye' in sents and user is not None:
            # remove participants
            self.participants.pop(user)
            kwargs.pop('user', None)
        # if we've seen anything we're looking for, we're pretty confident
        return sents, 1.0, kwargs

    def respond(self, sents, confidence, **kwargs):
        """
            gives a greeting or a goodbye depending on what's appropriate
        """
        if confidence == 0:
            return None
        name = self.participants.get(kwargs.get('user', None), None)
        name_changed = kwargs.get('name_changed', False)
        request_introduction = kwargs.get('request_introduction', False)

        if 'greeting' in sents or 'introduction' in sents:
            if request_introduction:
                return "Hello, what is your name?"
            else:
                return "Hello, {}!".format(name)
        if 'goodbye' in sents:
            return "Talk to you later!"
        if 'rollcall' in sents:
            people = list(self.participants.values())
            if len(people) > 1:
                roster = ", ".join(people[:-1])
                roster += " and {}.".format(people[-1])
                return "Currently in the conversation are " + roster
            elif len(people) == 1:
                return "It's just you and me right now, {}.".format(name)
            else:
                return "So lonely in here by myself ... wait who is that?"
        raise Exception(
            "expected response to be returned, but could not find rule"
        )
