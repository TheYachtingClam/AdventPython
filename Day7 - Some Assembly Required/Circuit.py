import Gates


class Circuit(object):
    gates = []

    def add_gate(self, new_gate):
        self.gates.append(new_gate)

    def hookup_gates(self):
        for gate in self.gates:
            gate.hookup(self.gates)
