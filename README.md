# Tugas 2 Pemrograman-Jaringan
|  Nama 	|   NRP	|
|---	|---	|
|  Davin Fisabilillah Reynard Putra 	|   5025221137	|

**Pemrograman Jaringan - C**

# Multithreaded Time Server (Python)
Proyek ini adalah implementasi sebuah server waktu sederhana menggunakan Python. Server ini mampu menangani beberapa koneksi klien secara bersamaan (concurrent) berkat penggunaan multithreading dan merespons dengan waktu saat ini sesuai permintaan.

---

# Deskripsi Soal
Tujuan dari program ini adalah untuk membangun sebuah time server dengan ketentuan sebagai berikut:

- Transport: Membuka port 45000 dengan protokol TCP.
- Konkurensi: Server harus dapat melayani beberapa permintaan klien secara bersamaan dengan menggunakan multithreading.
- Protokol Request:
  - Permintaan waktu diawali dengan string TIME dan diakhiri dengan karakter 13 (\r) dan 10 (\n).
  - Sesi dapat diakhiri dengan mengirimkan string QUIT yang juga diakhiri dengan \r\n.
- Protokol Response:
  - Respon dikirim dalam bentuk string UTF-8.
  - Format respon adalah JAM <jam>\r\n, di mana <jam> adalah waktu dalam format hh:mm:ss.

--- 
# Cara Menjalankan
Untuk menjalankan dan menguji server, ikuti langkah-langkah berikut:

1. Jalankan Server
Simpan kode di bawah sebagai time_server.py dan jalankan melalui terminal:

```
python3 server_time.py
```
Server akan menampilkan log bahwa ia telah berjalan di port 45000.

2. Uji dengan Klien (Telnet)
Buka jendela terminal baru dan gunakan telnet atau netcat untuk terhubung ke server.

```
telnet <IP_SERVER> 45000
```
Setelah terhubung, Anda dapat mulai mengirimkan perintah:

- Ketik TIME dan tekan Enter untuk meminta waktu.
- Ketik QUIT dan tekan Enter untuk memutuskan koneksi.

---

# Contoh Output 

## Output Sisi Server
![image](https://github.com/user-attachments/assets/e9df3920-10d3-408e-9e5b-5569cea02548)

## Output Sisi Client
![image](https://github.com/user-attachments/assets/591f4be4-045c-452f-899f-86b3a31660a2)
![image](https://github.com/user-attachments/assets/318c7f39-b561-45e3-8697-c58b846351f5)

---

# Penjelasan Kode Program

Kode mengimplementasikan sebuah time server multithreaded yang melayani beberapa client secara bersamaan. Program ini mempunyai dua kelas utama: Server dan ProcessTheClient. Kelas Server memiliki tugas utama untuk menginisialisasi soket jaringan, mengikatnya ke port 45000, dan mendengarkan koneksi TCP yang masuk. Ketika sebuah koneksi baru dari client diterima, kelas Server akan membuat sebuah objek baru dari kelas ProcessTheClient dan menjalankannya dalam sebuah thread terpisah. Cara ini memastikan bahwa server utama tetap dapat menerima koneksi baru tanpa harus menunggu selesainya permintaan dari client sebelumnya. Kelas ProcessTheClient kemudian mengambil alih komunikasi dengan client tersebut. Di dalamnya, sebuah loop berjalan untuk menerima perintah. Jika client mengirim perintah "TIME", kelas ini akan mengambil waktu saat ini menggunakan , memformatnya menjadi "hh:mm:ss", dan mengirimkannya kembali dalam format "JAM hh:mm:ss\r\n". Jika client mengirim "QUIT", loop akan berhenti dan koneksi untuk client tersebut akan ditutup.
