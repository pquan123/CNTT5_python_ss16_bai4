from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def find_patient_index(records, patient_id):
    for index, patient in enumerate(records):
        if patient.startswith(patient_id + "-"):
            return index
    return -1


def display_records(records):
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for index, patient in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = patient.split("-")

        print(
            f"{index}. [{patient_id}] "
            f"{name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.replace("-", " ").title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if (
            not birth_year.isdigit()
            or int(birth_year) < 1900
            or int(birth_year) > current_year
        ):
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        break

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ").capitalize()

    new_patient = "-".join(
        [patient_id, name, birth_year, diagnosis]
    )

    records.append(new_patient)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(new_patient)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    patient_info = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {patient_info[1]}")
    print(f"Chẩn đoán hiện tại: {patient_info[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    )

    new_diagnosis = (
        new_diagnosis.replace("-", " ").capitalize()
    )

    patient_info[3] = new_diagnosis

    records[index] = "-".join(patient_info)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    child = 0
    adult = 0
    elderly = 0

    for patient in records:
        birth_year = int(patient.split("-")[2])

        age = current_year - birth_year

        if age < 16:
            child += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")


def main():
    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        ).strip()

        if choice == "1":
            display_records(patient_records)

        elif choice == "2":
            add_patient(patient_records)

        elif choice == "3":
            update_diagnosis(patient_records)

        elif choice == "4":
            generate_age_report(patient_records)

        elif choice == "5":
            print(
                "\nCảm ơn bác sĩ đã sử dụng hệ thống!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")

main()