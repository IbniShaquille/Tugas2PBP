# Template Proyek Django PBP

Link aplikasi heroku(https://bynpbp.herokuapp.com/mywatchlist/html/)
![HTML](https://github.com/IbniShaquille/tugas2PBP/blob/main/assets/HTML.jpg)
![JSON](https://github.com/IbniShaquille/tugas2PBP/blob/main/assets/JSON.jpg)
![XML](https://github.com/IbniShaquille/tugas2PBP/blob/main/assets/XML.jpg)

## JSON vs XML vs HTML

JSON atau JavaScript object notation adalah format yang digunakan untuk menyimpan atau mentransfer data. JSON merupakan turunan javascript. JSON lebih mudah dipahami dan dibaca karena struktur bentuknya yang berupa key and value.
XML atau Extensible Markup Language merupakan bahasa markah yang dibuat untuk menyimpan dan mentransfer data. XML lebih kompleks dibandingkan JSON karena XML memiliki struktur yang lebih kompleks. XML memiliki tag-tag yang berbeda-beda sehingga lebih kompleks dibandingkan JSON.
HTML atau Hypertext Markup Language merupakan bahasa markah yang digunakan untuk membuat halaman web. HTML memiliki struktur yang lebih sederhana dibandingkan JSON dan XML. HTML memiliki tag-tag yang berbeda-beda sehingga lebih kompleks dibandingkan JSON dan XML. selain itu, HTML merupakan bahasa markah yang digunakan untuk membuat halaman web. 

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

kita memerlukan data delivery dalam mengimplementasi sebuah platform karena dalam sebuah platform kita memerlukan dan mengirimkan data. oleh karena itu data delivery sangat diperlukan dalam pembentukan sebuah platform. selain itu, dengan data delivery dapat membuat sebuah platform kita lebih dinamis karena tidak perlu membuat sebuah platform lagi ketika ingin mengubah data.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

untuk membuat app mywatchlist, saya membuat mywatchlist seperti membuat katalog kemarin. lalu, menambahkan path juga seperti tugas kemarin. lalu, model yang diperlukan saya masukkan ke views.py dan disesuaikan dengan atribut-atribut yang diminta. lalu untuk menambahkan 10 data, saya menggunakan data-data film yang ada. untuk implementasi HTML, XML, dan JSON dengan mengimport HttpResponse dan Serializer dan mereturn disesuaikan data deliver yang diminta. untuk membuat routing, menggunakan urls.py untuk membuka dan menampilkan data yang diminta dan menyesuaikan dengan urls yang kita minta. deployment dilakukan dengan hanya push ke github dan mengaktifkan heroku. postman hanya memasukan 3 urls localdata yang ada dan send request ke postman. 