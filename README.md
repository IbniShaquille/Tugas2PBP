# Template Proyek Django PBP

Link aplikasi heroku(https://bynpbp.herokuapp.com/katalog/)
![Bagan](https://github.com/IbniShaquille/tugas2PBP/blob/main/assets/diagram.png)

## penjelasan bagan

Bagan di atas merupakan bagan yang dikhususkan untuk django karena django merupakan MTV. MTV atau Model Template View, yaitu:
1. Model berfungsi untuk melakukan interaksi (menulis/membaca)dengan database.
2. Template berfungsi untuk mengatur tampilan dalam bentuk HTML.
3. View memuat logika yang digunakan untuk mengolah data dari model kemudian dapat
dikirimkan ke dalam Template. Pada bagian terakhir, ada URLS yaitu alamat yang berfungsi untuk menerima permintaan HTTP yang dilanjutkan ke View dan nanti diteruskan HTTP response.

## mengapa menggunakan Virtual Environment dan apabila jika tidak pada django?

Menggunakana Virtual Environment Karena setiap project mempunya kebutuhan yang berbeda-beda sehingga dibutukan virtual environment agar setiap project memiliki environmentnya masing-masing. Selain itu, versi dari library tidak akan berubah meskipun kita update. Jika kita tidak menggunakannya, maka library yang kita gunakan akan berubah-ubah. Hal ini akan semakin terasa jika project dikerjakan oleh sebuah tim, maka versi library akan disesuaikan pada versi laptop masing-masing tim.

## Penjelasan implementasi poin 1 sampai 4

Untuk mengimplementasi poin 1-4, saya sudah pernah mengerjakan tutorial 1. Saya menggunakan referensi tutorial tersebut. Ketika membuat views dan meroutingnya saya mengambil objek objek yang ada pada catalogitems yang ada di models. Lalu, saat masuk ke template (HTML), saya memasukkan table yang ada dengan objek-objek yang ada di models. Jadi, saat saya mengirimkan URL yang saya punya, masuk ke views untuk diolah dan masuk ke models. Lalu, models mengambilkan data dari database yang nanti dikirim ke views untuk dimasukkan ke template yang telah dibuat sehingga tampil pada layar