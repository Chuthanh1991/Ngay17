
class Testcauhoi :
	def __init__(self, danhsach_C):
		self.socau_hoi =0
		self.danhsach_cauhoi = danhsach_C
		self.diem = 0


	def Sitt_has_cauhoi(self) :
		return self.socau_hoi < len(self.danhsach_cauhoi)




	def Cauhoi_tieptheo(self):
		cauhoi_hientai = self.danhsach_cauhoi[self.socau_hoi]
		self.socau_hoi += 1
		nguoidung_traloi = input(f"Câu hỏi {self.socau_hoi}: {cauhoi_hientai.text} (True/False): ")
		self.kiemtra_cautraloi(nguoidung_traloi, cauhoi_hientai.dapan)

	def kiemtra_cautraloi(self, nguoidung_traloi, cauhoi_hientai) :
		if nguoidung_traloi.lower() == cauhoi_hientai.lower():
			self.diem += 1
			print("Bạn trả lời đúng!")
		else:
			print("Bạn trả lời sai!")
		print(f"Câu trả lời đúng là: {cauhoi_hientai}")
		print(f"Điểm hiện tại của bạn là: {self.diem}/{self.socau_hoi}")
		print("\n")

