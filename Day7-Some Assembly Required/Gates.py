class Gate(object):
    def clear_gate(self):
        self.outputGateCalculated = False


class AndGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1].strip()
        self.outputGate = 0
        self.outputGateValue = 0
        second_pass = values[0].split('AND')
        self.inputGate1Name = second_pass[0].strip()
        self.inputGate1 = 0
        self.inputGate2Name = second_pass[1].strip()
        self.inputGate2 = 0
        self.outputGateCalculated = False

    def __str__(self):
        return "AndGate inputGate1 = {0}, inputGate2 = {1}, outputGate = {2}".format(self.inputGate1Name,
                                                                                     self.inputGate2Name,
                                                                                     self.outputGateName)

    def hookup(self, gate_list):
        if not self.inputGate1Name.isdigit():
            input_gate1_attach = filter(filter_for_output_gate(self.inputGate1Name), gate_list)
            self.inputGate1 = input_gate1_attach[0]

        if not self.inputGate2Name.isdigit():
            input_gate2_attach = filter(filter_for_output_gate(self.inputGate2Name), gate_list)
            self.inputGate2 = input_gate2_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        if self.inputGate1Name.isdigit():
            value1 = int(self.inputGate1Name)
        else:
            value1 = self.inputGate1.calculate_gate()

        if self.inputGate2Name.isdigit():
            value2 = int(self.inputGate2Name)
        else:
            value2 = self.inputGate2.calculate_gate()
        self.outputGateValue = value1 & value2
        self.outputGateCalculated = True
        return self.outputGateValue


class OrGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1].strip()
        self.outputGate = 0
        self.outputGateValue = 0
        second_pass = values[0].split('OR')
        self.inputGate1 = 0
        self.inputGate1Name = second_pass[0].strip()
        self.inputGate2 = 0
        self.inputGate2Name = second_pass[1].strip()
        self.outputGateCalculated = False

    def __str__(self):
        return "OrGate inputGate1 = {0}, inputGate2 = {1}, outputGate = {2}".format(self.inputGate1Name,
                                                                                    self.inputGate2Name,
                                                                                    self.outputGateName)

    def hookup(self, gate_list):
        input_gate1_attach = filter(filter_for_output_gate(self.inputGate1Name), gate_list)
        self.inputGate1 = input_gate1_attach[0]

        input_gate2_attach = filter(filter_for_output_gate(self.inputGate2Name), gate_list)
        self.inputGate2 = input_gate2_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        value1 = self.inputGate1.calculate_gate()
        value2 = self.inputGate2.calculate_gate()
        self.outputGateValue = value1 | value2
        self.outputGateCalculated = True
        return self.outputGateValue


class LeftShift(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGate = 0
        self.outputGateValue = 0
        self.outputGateName = values[1].strip()
        second_pass = values[0].split('LSHIFT')
        self.inputGateName = second_pass[0].strip()
        self.inputGate = 0
        self.inputValue = int(second_pass[1].strip())
        self.outputGateCalculated = False

    def __str__(self):
        return "LeftShift inputGate = {0}, inputValue = {1}, outputGate = {2}".format(self.inputGateName,
                                                                                      self.inputValue,
                                                                                      self.outputGateName)

    def hookup(self, gate_list):
        input_gate_attach = filter(filter_for_output_gate(self.inputGateName), gate_list)
        self.inputGate = input_gate_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        value1 = self.inputGate.calculate_gate()
        left_shift_by = self.inputValue
        self.outputGateValue = value1 << left_shift_by
        self.outputGateCalculated = True
        return self.outputGateValue


class RightShift(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGate = 0
        self.outputGateValue = 0
        self.outputGateName = values[1].strip()
        second_pass = values[0].split('RSHIFT')
        self.inputGateName = second_pass[0].strip()
        self.inputGate = 0
        self.inputValue = int(second_pass[1].strip())
        self.outputGateCalculated = False

    def __str__(self):
        return "RightShift inputGate = {0}, inputValue = {1}, outputGate = {2}".format(self.inputGateName,
                                                                                       self.inputValue,
                                                                                       self.outputGateName)

    def hookup(self, gate_list):
        input_gate_attach = filter(filter_for_output_gate(self.inputGateName), gate_list)
        self.inputGate = input_gate_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        value1 = self.inputGate.calculate_gate()
        right_shift_by = self.inputValue
        self.outputGateValue = value1 >> right_shift_by
        self.outputGateCalculated = True
        return self.outputGateValue


class NotGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.outputGateName = values[1].strip()
        self.outputGate = 0
        self.outputGateValue = 0
        second_pass = values[0].split('NOT')
        self.inputGateName = second_pass[1].strip()
        self.inputGate = 0
        self.outputGateCalculated = False

    def __str__(self):
        return "NotGate inputGate = {0}, outputGate = {1}".format(self.inputGateName, self.outputGateName)

    def hookup(self, gate_list):
        input_gate_attach = filter(filter_for_output_gate(self.inputGateName), gate_list)
        self.inputGate = input_gate_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        value1 = self.inputGate.calculate_gate()
        self.outputGateValue = ~ value1
        self.outputGateCalculated = True
        return self.outputGateValue


class InputGate(Gate):
    def __init__(self, init_string):
        values = init_string.split('->')
        self.inputGate = 0
        self.inputGateName = values[0].strip()
        self.outputGate = 0
        self.outputGateName = values[1].strip()
        self.outputGateValue = 0
        self.outputGateCalculated = False

    def __str__(self):
        return "InputGate inputValue = {0}, outputGate = {1}".format(self.inputGateName, self.outputGateName)

    def hookup(self, gate_list):
        if not self.inputGateName.isdigit():
            input_gate_attach = filter(filter_for_output_gate(self.inputGateName), gate_list)
            self.inputGate = input_gate_attach[0]

    def calculate_gate(self):
        if self.outputGateCalculated:
            return self.outputGateValue

        if self.inputGateName.isdigit():
            self.outputGateValue = int(self.inputGateName)
        else:
            self.outputGateValue = self.inputGate.calculate_gate()
        self.outputGateCalculated = True
        return self.outputGateValue


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


def filter_for_output_gate(gate_name):
    def my_filter(x):
        return x.outputGateName == gate_name

    return my_filter
