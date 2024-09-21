from zipfile import ZipFile

FILE_NAME = r"data\\Rotfuss_Hronika-ubiycy-korolya_1_Imya-vetra_RuLit_Me_789125.epub"
extract_dir = "data\\extract"

with ZipFile(FILE_NAME, "r") as zip_ref:
    zip_ref.extractall(extract_dir)