from stevedore import ExtensionManager

class HelloFunction:
    def __init__(self, namespace, name):
        em = ExtensionManager(
            namespace=namespace,
            invoke_on_load=True)

        self.__replay_func = None
        for ep in em:
            if ep.name == name:
                self.__replay_func = ep.entry_point.load()

    def say(self):
        return self.__replay_func
