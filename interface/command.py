class AbstractCommand(object):

    def __init__(self, **kwargs):
        if hasattr(self, "expected_args"):
            for arg in self.expected_args:
                if arg not in kwargs:
                    raise KeyError("Missing expected argument")

        for key, value in kwargs.items():
            setattr(self, key, value)

    def execute(self):
        raise NotImplemented()

    def pre_execute(self):
        print "No pre execute used"

    def post_execute(self):
        print "No post execute used"