class GateInterface(object):
    def teststring(self):
        return False


class AndGate(GateInterface):
    pass


class OrGate(GateInterface):
    pass


class LeftShift(GateInterface):
    pass


class RightShift(GateInterface):
    pass


class NotGate(GateInterface):
    pass
