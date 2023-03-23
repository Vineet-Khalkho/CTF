from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from Crypto.Util.number import long_to_bytes, bytes_to_long


file = open(r"quantum_artifact.qasm").read()
qtc = QuantumCircuit.from_qasm_str(file)
qtc.measure_all()

stabilizer_simulator = AerSimulator(method='stabilizer')

tc = transpile(qtc, stabilizer_simulator)

stabilizer_result = stabilizer_simulator.run(tc, shots=1).result()

res = stabilizer_result.get_counts()
flag = list(res.keys())[0]
flag = flag.replace(" ", "")
flag = int(flag, 2)
flag = long_to_bytes(flag)
print(flag)
