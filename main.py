meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("Kata yang anda ketik adalah:", word)
    print("Arti dari kata yang anda tuliskan adalah:", meme_dict.get(word))
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Maaf, kata", word, "tidak ada dalam kamus ini")
