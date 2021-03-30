
class Employee:

    def __init__(self):
        self.employ_list = []
        print("parent init")

    def get_employee_list(self):
        name_list = []
        for idx, em in enumerate(self.employ_list):
            name_list.append(em['user_name'])
        return name_list

    def newEmployee(self, _department):

        user_template = {}

        print("> 등록할 직원의 정보를 입력해 주세요.")
        print("이름 : ", end='')
        user_name = input()
        _department.show_department()
        print("부서 : ", end='')
        department = input()
        print("직무 : ", end='')
        position = input()

        user_template = {
            'user_name': user_name,
            'department': department,
            'position': position
        }

        self.employ_list.append(user_template)
        _department.add_member_to_dept(department)
        print('[*] 새로운 직원이 추가 되었습니다 - ', user_template['user_name'])

    def deleteEmployee(self):
        print("삭제할 직원의 이름을 입력하세요 : ", end='')
        user_name = input()

        for idx, em in enumerate(self.employ_list):
            if em['user_name'] == user_name:
                del self.employ_list[idx]
                print('[*] 정상적으로 삭제 되었습니다. - ', user_name)
                return

        print('[x] 사용자를 찾을 수 없습니다. ')

    def show_employee_list(self):
        if self.employ_list:
            print("[직원 목록]")
            for em in self.employ_list:
                print(f"- 이름 : {em['user_name']}\t| 부서 : {em['department']}\t| 직무 : {em['position']}")
        else:
            print("[x] 등록된 직원이 존재하지 않습니다.")
        print('\n')

    def printInstruction(self):
        print("-----------------------------------")
        print("---------    인사관리 기능     --------")
        print("-----------------------------------")
        print('[ 인사 관리 메뉴 ]\n')
        print('1 - 새로운 직원 추가')
        print('2 - 기존 직원 삭제')
        print('3 - 직원 목록 조회')
        print('4 - 돌아 가기')
        print("-----------------------------------")

    def executeJob(self, _department):

        while True:
            self.printInstruction()
            print("[인사] 메뉴를 선택하세요 : ", end='')
            selected = input()

            if int(selected) == 1:
                self.newEmployee(_department)
            elif int(selected) == 2:
                self.deleteEmployee()
            elif int(selected) == 3:
                self.show_employee_list()

            elif int(selected) == 4:
                print("프로그램을 종료합니다. ")
                break

class RegularEmployee(Employee):
    def __init__(self):
        print("child init")

    def newEmployee(self, _department):
        print("new in regular")
        super().newEmployee(_department)


class PartTimeEmployee(Employee):
    def newEmployee(self, _department):
        print("new in parttime")




if __name__ == '__main__':
    re = RegularEmployee()
    pt = PartTimeEmployee()

    test = 0
    re.executeJob(test)