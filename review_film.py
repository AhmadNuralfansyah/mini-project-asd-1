class ReviewFilm:
    def __init__(self, judul, genre, tahun, rating, komentar):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating
        self.komentar = komentar

    def __str__(self):
        return f"===Review Film:==\n\
Judul: {self.judul}\n\
Genre: {self.genre}\n\
Tahun: {self.tahun}\n\
Rating: {self.rating}\n\
Komentar: {self.komentar}"

class DatabaseReview:
    def __init__(self):
        self.reviews = []

    def tambah_review(self, review):
        self.reviews.append(review)

    def tampilkan_semua_review(self):
        if not self.reviews:
            print("Belum ada review film.")
        else:
            for review in self.reviews:
                print(review)
                

    def cari_review_by_judul(self, judul):
        for review in self.reviews:
            if review.judul.lower() == judul.lower():
                return review
        return None

    def update_review(self, judul, review_baru):
        review = self.cari_review_by_judul(judul)
        if review:
            review.rating = review_baru.rating
            review.komentar = review_baru.komentar
            print(f"Review film '{judul}' berhasil diperbarui.")
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    def hapus_review(self, judul):
        review = self.cari_review_by_judul(judul)
        if review:
            self.reviews.remove(review)
            print(f"Review film '{judul}' berhasil dihapus.")
        else:
            print(f"Review film '{judul}' tidak ditemukan.")



database_review = DatabaseReview()

while True:
    print("\n")
    print("==Menu Review Film==")
    print("1. Tambah Review")
    print("2. Tampilkan Semua Review")
    print("3. Cari Review")
    print("4. Update Review")
    print("5. Hapus Review")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        judul = input("Masukkan judul film: ")
        genre = input("Masukkan genre film: ")
        tahun = int(input("Masukkan tahun film: "))
        rating = int(input("Masukkan rating film (1-10): "))
        komentar = input("Masukkan komentar film: ")

        review_baru = ReviewFilm(judul, genre, tahun, rating, komentar)
        database_review.tambah_review(review_baru)

    elif pilihan == 2:
        database_review.tampilkan_semua_review()

    elif pilihan == 3:
        judul = input("Masukkan judul film yang ingin dicari: ")
        review = database_review.cari_review_by_judul(judul)

        if review:
            print(f"Review film '{judul}' ditemukan:")
            print(review)
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    elif pilihan == 4:
        judul = input("Masukkan judul film yang ingin diupdate: ")
        review = database_review.cari_review_by_judul(judul)

        if review:
            rating_baru = int(input("Masukkan rating baru (1-10): "))
            komentar_baru = input("Masukkan komentar baru: ")

            review_baru = ReviewFilm(judul, review.genre, review.tahun, rating_baru, komentar_baru)
            database_review.update_review(judul, review_baru)
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    elif pilihan == 5:
        judul = input("Masukkan judul film yang ingin dihapus: ")
        database_review.hapus_review(judul)

    elif pilihan == 0:
        break

    else:
        print("invalid.")
