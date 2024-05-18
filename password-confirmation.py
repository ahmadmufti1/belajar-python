import re
from stringcolor import*


username = str(input("Masukkan Nama Anda : "))

nomor_telepon = str(input("Masukkan No. Telp Anda : "))
while not re.search(r"[0-9]", nomor_telepon):
    print(cs("Nomor Telepon harus berupa angka","red").underline())
    nomor_telepon = str(input("Masukkan Nomor Telepon Anda :\n"))

email = str(input("Masukkan Email Anda : "))
while not re.search(r"[$#@!]", email):
    print(cs("Email harus menggunakan @gmail.com","red").underline())
    email = str(input("Masukkan Ulang Email Anda :\n"))

password = str(input("Masukkan Password Anda : "))
while not re.search(r"[A-Z a-z 0-9]{7,}", password):
    print("password anda harus")
    print(cs("Setidaknya Berjumlah 8 Huruf", "red"))
    print(cs("Menggunakan Huruf Kapital", "red"))
    print(cs("Menggunakan Huruf Kecil", "red"))
    print(cs("Menggunakan Angka", "red"))
    password = str(input("Masukkan Ulang Password Anda : \n"))

else:
    print(cs("Selamat Datang", "green"))
    print(cs(f"{username}", "blue"))


