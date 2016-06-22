import Circuit
import Gates

f = open("testInput.txt")
circuit = Circuit.Circuit()
for line in f:
    gate = Gates.create_gate(line)
    circuit.add_gate(gate)

circuit.hookup_gates()
