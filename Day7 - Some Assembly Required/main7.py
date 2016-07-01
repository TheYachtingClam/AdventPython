import Circuit
import Gates

f = open("realInput.txt")
circuit = Circuit.Circuit()
for line in f:
    gate = Gates.create_gate(line)
    circuit.add_gate(gate)

circuit.hookup_gates()
circuit.calculate_gates()
print(str(circuit))
