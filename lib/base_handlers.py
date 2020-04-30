import re
import requests

class __abs_handler():
    '''
    abstract class for
    creating base handlers.
    '''
    def __init__(self, handler_name, regex):
        self.handler_name = handler_name
        self.regex = regex

    @staticmethod
    def __get_event_text(event):
        return event.args.get("text","") if type(event.args) == dict else ""

    def __call__(self, event, debug=False):
        if self.has_command(event):
            if debug:
                print(f"[DEBUG] {self.handler_name} detected.")
            self.do_action()

    def has_command(self, event):
        text = self.__get_event_text(event)
        match = re.search(self.regex, text, re.IGNORECASE)
        return bool(match)

    # abstract methods that
    # must be implemented.
    def do_action(self):
        pass

class request_handler(__abs_handler):
    '''
    create commands
    that sends requests.
    '''
    def __init__(self, handler_name, regex, method, request):
        super().__init__(self, handler_name, regex)
        self.method = method.lower()
        self.request = request

    def do_action(self):
        if(self.method == "get"):
            action = requests.get
        elif(self.method == "post"):
            action = requests.post
        elif(self.method == "put"):
            action = requests.put
        elif(self.method == "delete"):
            action = requests.delete
        else:
            raise Exception("Invalid request method.")
        assert action, "Could not make the request."
        action(**self.request)

class function_handler(__abs_handler):
    '''
    create commands
    that execute functions.
    '''
    def __init__(self, handler_name, regex, function):
        super().__init__(self, handler_name, regex)
        self.function = function
    
    def do_action(self):
        self.function()