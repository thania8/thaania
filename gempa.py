class Gempa:
    # konstruktor inisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):

        # atribut
        self.lokasi = lokasi
        self.skala = skala

    # method menentukan dampak skala gempa
    def dampak(self):

    # statement / logika
        if self.skala < 2:
            print('dampak gempa tidak berasa')
        elif self.skala >=2 and self.skala <=4:
            print('dampak gempa bangunan retak-retak')
        elif self.skala > 4 and self.skala <=6:
            print('dampak gempa berdampak bangunan roboh')
        elif self.skala > 6:
            print('dampak gempa berpotensi tsunami')

        # menampilkan lokasi dan skala gempa
        print(f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')