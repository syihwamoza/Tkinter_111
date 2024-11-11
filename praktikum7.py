import tkinter as tk  # Mengimpor modul tkinter untuk membuat aplikasi GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan kotak pesan error

def hasil_prediksi():  # Fungsi untuk menangani prediksi ketika tombol diklik
    try:
        for entry in entries:  # Iterasi melalui setiap entry (kolom input)
            nilai = int(entry.get())  # Mengambil nilai input dan mengonversinya menjadi integer
            print(f"Nilai yang dimasukkan: {nilai}")  # Debug: Menampilkan nilai input ke konsol
            if not (0 <= nilai <= 100):  # Mengecek apakah nilai di luar rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Memunculkan error jika nilai tidak valid

        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  # Menampilkan hasil prediksi
        print("Prediksi berhasil ditampilkan.")  # Debug: Menampilkan pesan jika prediksi berhasil

    except ValueError as ve:  # Menangani error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")  # Menampilkan kotak pesan error
        print("Error: Input tidak valid.")  # Debug: Menampilkan pesan error ke konsol

# Inisialisasi Tkinter root (jendela utama aplikasi)
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menentukan judul aplikasi
root.geometry("500x600")  # Menentukan ukuran jendela aplikasi
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang jendela utama

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#ff4d4d")  # Membuat label dengan font dan warna latar belakang
judul_label.pack(pady=20)  # Menampilkan label dengan jarak atas dan bawah

# Frame untuk input nilai
frame_input = tk.Frame(root, bg="#ff4d4d")  # Membuat frame untuk menampung input nilai dengan warna latar belakang merah
frame_input.pack(pady=10)  # Menampilkan frame dengan jarak atas dan bawah

# Membuat entry untuk input nilai (loop 10 kali untuk 10 mata pelajaran)
entries = []  # Daftar untuk menyimpan objek entry
for i in range(10):  # Perulangan untuk membuat 10 input field
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="#ff4d4d")  # Membuat label untuk setiap input
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di grid
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Membuat entry untuk input nilai
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry di grid
    entries.append(entry)  # Menambahkan entry ke daftar entries
    print(f"Entry {i+1} dibuat.")  # Debug: Menampilkan informasi bahwa entry dibuat

# Tombol prediksi untuk memanggil fungsi hasil_prediksi saat diklik
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"))  # Membuat tombol dengan teks dan pengaturan font
prediksi_button.pack(pady=30)  # Menampilkan tombol dengan jarak atas dan bawah

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="blue", bg="#ff4d4d")  # Membuat label untuk hasil prediksi
hasil_label.pack(pady=20)  # Menampilkan label dengan jarak atas dan bawah

# Memulai loop utama Tkinter untuk menampilkan jendela aplikasi
print("Aplikasi berjalan...")  # Debug: Menampilkan pesan bahwa aplikasi sedang berjalan
root.mainloop()  # Menjalankan loop utama aplikasi Tkinter
