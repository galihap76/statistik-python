import numpy as np

def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = np.argmax(np.bincount(data))

    return mean, median, mode


num_patients = int(input("Masukkan jumlah pasien: "))
patient_data = []

for i in range(num_patients):
    age = int(input(f"Masukkan usia pasien ke-{i+1}: "))
    patient_data.append(age)

mean, median, mode = calculate_statistics(patient_data)

print("Hasil Statistik Usia Pasien:")
print(f"Rata-rata (Mean) usia: {mean}")
print(f"Median usia: {median}")
print(f"Modus usia: {mode}")
