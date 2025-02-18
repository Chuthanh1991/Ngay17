'''
class NguoiDung:
	def __init__(self, nguoidung_id, nguoidung_ten) :
		self.id = nguoidung_id
		self.ten = nguoidung_ten
		self.luot_theo_doi = 0
		self.dang_theo_doi = 0
	def theo_doi(self, nguoidung):
		nguoidung.luot_theo_doi += 1
		self.dang_theo_doi += 1

nguoidung_1 = NguoiDung("001", "Chu kim Thành")
nguoidung_2 = NguoiDung("002", "Nguyen van A")

nguoidung_1.theo_doi(nguoidung_2)
print(nguoidung_1.luot_theo_doi)
print(nguoidung_1.dang_theo_doi)
print(nguoidung_2.luot_theo_doi)
print(nguoidung_2.dang_theo_doi)
'''

from question_model import Cauhoi
from data import question_data
from quiz_brain import Testcauhoi

# Khởi tạo biến danh sách
nganhang_cauhoi  = []
for cauhoi in question_data:
	cauhoi_text = cauhoi["text"]
	dapan_text = cauhoi["answer"]
	cauhoi_moi = Cauhoi(cauhoi_text, dapan_text)
	nganhang_cauhoi.append(cauhoi_moi)
#print(nganhang_cauhoi[0].dapan)


# Khởi tạo đối tượng quản lý bài kiểm tra
quan_ly_bai_kiemtra = Testcauhoi(nganhang_cauhoi)
 #Bài kiểm tra còn câu hỏi nào không
while quan_ly_bai_kiemtra.Sitt_has_cauhoi():
	quan_ly_bai_kiemtra.Cauhoi_tieptheo()
print("Bạn đã hoàn thành bài kiểm tra")
print("Điểm của bạn là:", quan_ly_bai_kiemtra.diem)





#TODO 1: đặt câu hỏi



#TODO 2: kiểm tra xem câu trả lời có đúng không



#TODO 3: kiểm tra xem chúng ta đã kết thúc bài kiểm tra chưa


