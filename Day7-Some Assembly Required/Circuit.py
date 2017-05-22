import Gates
import struct


class Circuit(object):
    gates = []

    def __str__(self):
        return_value = ""
        for gate in self.gates:
            '''return_value += "[{0}] = {1}\n".format(gate.outputGateName,
                                                   struct.unpack('H', struct.pack('h', gate.outputGateValue)))'''
            return_value += "[{0}] = {1}\n".format(gate.outputGateName,
                                                    gate.outputGateValue)
        return return_value

    def add_gate(self, new_gate):
        print("adding gate {0}".format(str(new_gate)))
        self.gates.append(new_gate)

    def hookup_gates(self):
        for gate in self.gates:
            print("hookup gate {0}".format(str(gate)))
            gate.hookup(self.gates)

    def calculate_gates(self):
        for gate in self.gates:
            print("calculate gate {0}".format(str(gate)))
            gate.calculate_gate()

    def clear_gates(self):
        for gate in self.gates:
            gate.clear_gate()