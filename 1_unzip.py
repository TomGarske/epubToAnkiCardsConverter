from zipfile import ZipFile

FILE_NAME = r"data\\Rotfuss_Hronika-ubiycy-korolya_1_Imya-vetra_RuLit_Me_789125.epub"
# FILE_NAME = r"data\\Rouling_Garri-Potter-perevod-ROSMEN-s-red-Shenina-_1_Garri-Potter-i-Filosofskiy-kamen_RuLit_Me_816475.epub"
extract_dir = "data\\extract"

with ZipFile(FILE_NAME, "r") as zip_ref:
    zip_ref.extractall(extract_dir)