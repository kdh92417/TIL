# 시리얼 번호 생성 함수
def create_serial():
    # 시리얼 넘버를 위한 딕트 생성
    serial_dict = {}

    # 상품명을 입력받아 시리얼넘버를 생성하는 루프
    while True:
        product_name = input("시리얼 생성을 위한 상품명을 입력해주세요 : ")

        # 'q'를 입력받으면 루프 종료
        if product_name == 'q':
            break

        # 시리얼 앞 두자리 대문자로 생성
        serial_text = product_name[:2].upper()

        # 시리얼 딕트안에 해당 상품이 있다면 넘버를 +1 해주고 시리얼 넘버 생성
        if product_name in serial_dict:
            serial_dict[product_name][0] += 1
            serial = str(serial_dict[product_name][0]).zfill(4)
            serial_dict[product_name][1].append(serial_text + serial)

        # 딕트안에 상품이 없다면 1번 시리얼넘버 생성
        else:
            serial_dict[product_name] = [1, [serial_text + str(1).zfill(4)]]

        print(f"시리얼 넘버 : {serial_dict[product_name][1][-1]}")

    return serial_dict


# Test
print(create_serial())