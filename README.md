# Tugas 2 Pemrograman-Jaringan
|  Nama 	|   NRP	|
|---	|---	|
|  Davin Fisabilillah Reynard Putra 	|   5025221137	|

**Pemrograman Jaringan - C**

## Penjelasan Kode Program

Kode mengimplementasikan sebuah time server multithreaded yang melayani beberapa client secara bersamaan. Program ini mempunyai dua kelas utama: Server dan ProcessTheClient. Kelas Server memiliki tugas utama untuk menginisialisasi soket jaringan, mengikatnya ke port 45000, dan mendengarkan koneksi TCP yang masuk. Ketika sebuah koneksi baru dari client diterima, kelas Server akan membuat sebuah objek baru dari kelas ProcessTheClient dan menjalankannya dalam sebuah thread terpisah. Cara ini memastikan bahwa server utama tetap dapat menerima koneksi baru tanpa harus menunggu selesainya permintaan dari client sebelumnya. Kelas ProcessTheClient kemudian mengambil alih komunikasi dengan client tersebut. Di dalamnya, sebuah loop berjalan untuk menerima perintah. Jika client mengirim perintah "TIME", kelas ini akan mengambil waktu saat ini menggunakan , memformatnya menjadi "hh:mm:ss", dan mengirimkannya kembali dalam format "JAM hh:mm:ss\r\n". Jika client mengirim "QUIT", loop akan berhenti dan koneksi untuk client tersebut akan ditutup.
