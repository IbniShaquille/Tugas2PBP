# Todolist Django PBP

Link aplikasi heroku(https://bynpbp.herokuapp.com/todolist/html/)

## fungsi csrf_token

csrf_token adalah sebuah fungsi yang digunakan untuk mengamankan sebuah form agar tidak bisa diakses oleh orang lain. csrf_token akan menghasilkan sebuah token yang akan dijadikan sebuah hidden input pada form. Token tersebut akan di cek oleh django apakah token tersebut sesuai dengan token yang ada pada session. Jika token tersebut tidak sesuai maka akan muncul error 403.

## dapatkah membuat form menggunakan <form> tanpa generator form?

Dapat, dengan cara membuat form secara manual. dengan cara membuat form secara manual kita harus membuat input untuk setiap field yang ada pada model. Jika kita menggunakan generator form maka kita hanya perlu membuat form dengan memanggil fungsi form.

## proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1. Pengguna mengisi form pada halaman
2. Pengguna menekan tombol submit
3. Data yang diinputkan akan dikirimkan ke server
4. Server akan memproses data yang dikirimkan
5. Data yang sudah diproses akan disimpan pada database
6. Data yang sudah disimpan pada database akan ditampilkan pada halaman

## bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat model
2. Membuat view
3. Membuat template
4. Membuat url
5. Membuat form
6. menyambungkan semua bagian

# CSS Todolist Django PBP

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS adalah style yang diletakkan pada tag html. Internal CSS adalah style yang diletakkan pada tag head. External CSS adalah style yang diletakkan pada file css yang berbeda dengan file html. Kelebihan dari inline css adalah kita bisa membuat style yang hanya berlaku pada satu tag html. Kelebihan dari internal css adalah kita bisa membuat style yang berlaku pada semua tag html. Kelebihan dari external css adalah kita bisa membuat style yang berlaku pada semua tag html dan kita bisa mengubah style yang sudah dibuat tanpa harus mengubah file html. Kekurangan dari inline css adalah kita tidak bisa membuat style yang berlaku pada semua tag html. Kekurangan dari internal css adalah kita tidak bisa membuat style yang berlaku pada semua tag html dan kita tidak bisa mengubah style yang sudah dibuat tanpa harus mengubah file html. Kekurangan dari external css adalah kita tidak bisa membuat style yang berlaku pada satu tag html.

## Jelaskan tag HTML5 yang kamu ketahui

Tag HTML5 yang saya ketahui adalah tag header, footer, form, table, dan lain sebagainya.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

CSS selector yang saya ketahui adalah id selector, class selector, element selector, dan universal selector.

## jelaskan bagaimana cara kamu mengimplementasikan Checklist di atas

1. mengubah class table menjadi card
2. mengubah menjadi div saja tidak menggunakan table
3. menggunakan bootstrap untuk membuat card
4. karena ada yang masih kurang baik, saya mengubah di base.html agar dapat membuat style yang lebih luas

