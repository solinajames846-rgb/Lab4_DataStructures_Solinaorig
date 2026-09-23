LAST_NAME = "Solina"
STUDENT_ID = "TUPM-26-2302"
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")

base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]
print(f"Initial Sequence: {number_sequence}")
number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
print(f"After Extend: {number_sequence}")
base_count = number_sequence.count(base_val)
print(f"Occurrences of {base_val}: {base_count}")
number_sequence.sort()
print(f"Sorted Sequence: {number_sequence}")



