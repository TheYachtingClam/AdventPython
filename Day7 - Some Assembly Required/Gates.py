class Gate(object):
    pass


class AndGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1]
        second_pass = values[0].split('AND')
        self.inputGate1Name = second_pass[0]
        self.inputGate2Name = second_pass[1]

    def __str__(self):
        return "AndGate inputGate1 = {0}, inputGate2 = {1}, outputGate = {2}".format(self.inputGate1Name,
                                                                                     self.inputGate2Name,
                                                                                     self.outputGateName)


class OrGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1]
        second_pass = values[0].split('OR')
        self.inputGate1Name = second_pass[0]
        self.inputGate2Name = second_pass[1]

    def __str__(self):
        return "OrGate inputGate1 = {0}, inputGate2 = {1}, outputGate = {2}".format(self.inputGate1Name,
                                                                                    self.inputGate2Name,
                                                                                    self.outputGateName)


class LeftShift(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1]
        second_pass = values[0].split('LSHIFT')
        self.inputGateName = second_pass[0]
        self.inputValue = second_pass[1]

    def __str__(self):
        return "LeftShift inputGate = {0}, inputValue = {1}, outputGate = {2}".format(self.inputGateName,
                                                                                      self.inputValue,
                                                                                      self.outputGateName)


class RightShift(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1]
        second_pass = values[0].split('RSHIFT')
        self.inputGateName = second_pass[0]
        self.inputValue = second_pass[1]

    def __str__(self):
        return "RightShift inputGate = {0}, inputValue = {1}, outputGate = {2}".format(self.inputGateName,
                                                                                       self.inputValue,
                                                                                       self.outputGateName)


class NotGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1]
        second_pass = values[0].split('NOT')
        self.inputGateName = second_pass[1]

    def __str__(self):
        return "NotGate inputGate = {0}, outputGate = {1}".format(self.inputGateName, self.outputGateName)


class InputGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.inputValue = values[0]
        self.outputGateName = values[1]

    def __str__(self):
        return "InputGate inputValue = {0}, outputGate = {1}".format(self.inputValue, self.outputGateName)


def create_gate(line):
    if 'AND' in line:
        return AndGate(line)
    elif 'OR' in line:
        return OrGate(line)
    elif 'NOT' in line:
        return NotGate(line)
    elif 'LSHIFT' in line:
        return LeftShift(line)
    elif 'RSHIFT' in line:
        return RightShift(line)
    else:
        return InputGate(line)
