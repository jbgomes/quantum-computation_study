from qiskit import QuantumCircuit

qc = QuantumCircuit(2) # parâmetro 2 é a quantidade de qubits ou registradores quânticos disponíveis
qc.x(1) # gate quântico x está indo no qubit 1 (segundo qubit)
qc.h(0)

qc.draw() # mostra a aparência do circuito quântico