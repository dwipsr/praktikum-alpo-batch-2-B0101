import time

# Catat waktu mulai
waktu_mulai = time.perf_counter()

# Contoh: Proses perulangan hingga 10 juta kali
total = 0

# --- KODE YANG INGIN DIUKUR ---
for i in range(10_000_000):
    total += i
    # print(i)

# Catat waktu selesai
waktu_selesai = time.perf_counter()

# Hitung selisih waktu
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"Hasil perhitungan: {total}")
print(f"Lama waktu eksekusi: {lama_eksekusi:.6f} detik")