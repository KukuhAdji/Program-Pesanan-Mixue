class Node:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_menu(self, nama, harga):
        # Menambahkan menu ke keranjang
        if not self.head:
            self.head = Node(nama, harga)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(nama, harga)

    def tampilkan_pesanan(self):
        # Menampilkan pesanan yang sudah ditambahkan
        if not self.head:
            print("Keranjang kosong")
        else:
            current = self.head
            idx = 1
            while current:
                print(f"{idx}. {current.nama} {current.harga} rupiah")
                current = current.next
                idx += 1

    def hitung_total_harga(self):
        # Menghitung total harga pesanan
        total = 0
        current = self.head
        while current:
            total += current.harga
            current = current.next
        return total

menu_miexue = {
    "Miexue Ice Cream": 5000,
    "Boba Shake": 16000,
    "Mi Sundae": 14000,
    "Mi Ganas": 11000,
    "Creamy Mango Boba": 22000
}

keranjang = LinkedList()

while True:
    print("\nPilihan Menu:")
    print("1. Tambah pesanan ke keranjang")
    print("2. Tampilkan pesanan yang sudah ditambahkan")
    print("3. Bayar Pesanan")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        # Pilihan untuk menambah pesanan
        print(menu_miexue)
        pesanan = input("Masukkan pesanan (nama menu): ")
        if pesanan in menu_miexue:
            harga = menu_miexue[pesanan]
            keranjang.tambah_menu(pesanan, harga)
            print(f"{pesanan} sudah ditambahkan ke keranjang")
        else:
            print("Menu tidak tersedia")
    elif pilihan == "2":
        # Pilihan untuk menampilkan pesanan yang sudah ditambahkan
        print("Pesanan yang sudah ditambahkan:")
        keranjang.tampilkan_pesanan()
    elif pilihan == "3":
        # Pilihan untuk membayar pesanan
        total_harga = keranjang.hitung_total_harga()
        print(f"Total biaya yang harus dibayarkan adalah {total_harga} rupiah")
        uang_dibayar = int(input("jumlah uang yang anda bayarkan: "))
        bayar = uang_dibayar-total_harga
        if bayar == 0:
            print("Silahkan pesanannya, Terimakasih sudah membeli")
        else:
            print("Ini kembalian anda: ", bayar)
            print("Terimakasih sudah membeli")
        break
    elif pilihan == "4":
        # Pilihan untuk keluar dari program
        print("Terimakasih semoga hari mu menyenangkan dan sampai jumpa kembali")
        break
    else:
        print("Pilihan tidak valid")
