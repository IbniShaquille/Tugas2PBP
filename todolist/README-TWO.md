# Javascript dan AJAX

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming adalah proses yang berjalan secara berurutan. Asynchronous programming adalah proses yang berjalan secara bersamaan. Synchronous programming akan menunggu proses sebelumnya selesai baru akan menjalankan proses selanjutnya. Asynchronous programming tidak akan menunggu proses sebelumnya selesai baru akan menjalankan proses selanjutnya. Synchronous programming akan membutuhkan waktu yang lebih lama untuk menyelesaikan suatu proses. Asynchronous programming akan membutuhkan waktu yang lebih singkat untuk menyelesaikan suatu proses.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programming adalah paradigma yang mengacu pada suatu proses yang berjalan secara berurutan. Contoh penerapannya pada tugas ini adalah ketika kita menekan tombol "Add" maka akan muncul sebuah form untuk menambahkan data. Ketika kita menekan tombol "Close" maka form tersebut akan hilang. Ketika kita menekan tombol "Submit" maka data yang kita masukkan akan ditambahkan ke dalam tabel. 

## Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX adalah ketika kita mendapatkan sebuah data dengan GET tanpa harus merefresh halaman. Ketika kita mengirim sebuah data dengan POST tanpa harus merefresh halaman. dengan demikian, kita dapat mengirimkan data tanpa harus merefresh halaman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. membuat sebuah json untuk memberikan data berupa json dengan key n value.
2. membuat path /todolist/json
3. lalu mendapatkan data dengan GET dari jQuery library
4. membuat sebuah /todolist/json/add untuk menambah data
5. membuat modal agar bisa menambahkan data
6. menghubungkan modal tersebut dengan tombol /todolist/json/add
7. membuat POST method untuk menambahkan data dengan jQuery library