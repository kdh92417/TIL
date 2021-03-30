
class Department:
    def __init__(self):
        self.department_list = []

    def new_department(self):
        print("새로운 부서를 등록합니다.")
        print("부서명을 입력하세요 : ", end='')
        dept_name = input()
        self.department_list.append({
            'name' : dept_name,
            'members' : 0
        })

    def show_department(self):
        if self.department_list:
            print("[ 부서 목록 ]")
            for dp in self.department_list:
                print(f"- 부서명 : {dp['name']}\t| 구성원 : {dp['members']}" )
        else:
            print("[x] 등록된 부서가 존재하지 않습니다.")
        print('\n')

    def add_member_to_dept(self, dept_name):
        for idx, dp in enumerate(self.department_list):
            if dp['name'] == dept_name:
                dp['members'] += 1

    def print_instruction(self):
        print("---------------------------------------")
        print("[ 부서 관리 기능 ]\n")
        print("---------------------------------------")
        print("1 - 새로운 부서 생성")
        print("2 - 부서 현황 조회")
        print("3 - 돌아가기")
        print("---------------------------------------")

    def execute_job(self):
        while True:
            self.print_instruction()
            print("[부서] 메뉴를 선택하세요 : ", end='')
            selected = input()

            if int(selected) == 1:
                self.new_department()
            elif int(selected) == 2:
                self.show_department()
            elif int(selected) == 3:
                break