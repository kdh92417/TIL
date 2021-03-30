class Project:
    def __init__(self, _employee):
        self._employee = _employee
        self.project_list = []

    def new_project(self):

        print('새로운 프로젝트를 생성합니다.')
        print('프로젝트 이름 : ', end='')
        project_name = input()

        print('기간 : ', end='')
        project_duration = input()

        print('어떤 사람을 포함시킬 건가요?')
        # 선택 가능한 직원 목록 출력
        print(self._employee.get_employee_list())
        project_members = input()

        project_template = {
            'name' : project_name,
            'duration' : project_duration,
            'members' : project_members
        }

        self.project_list.append(project_template)

    def show_current_project(self):
        if self.project_list:
            print("[ 프로젝트 목록 ]")
            for pj in self.project_list:
                print(f"- 프로젝트명 : {pj['name']}\t| 기간 : {pj['duration']}\t| 구성원 : {pj['members']}")
        else:
            print('[x] 등록된 프로젝트가 없습니다.')
        print('\n')

    def print_instruction(self):
        print('-------------------------------------')
        print('[ 프로젝트 관리 기능  ]\n')
        print('-------------------------------------')
        print('1 - 새로운 프로젝트 생성')
        print('2 - 프로젝트 조회')
        print('3 - 돌아가기')
        print('-------------------------------------')

    def execute_job(self):
        while True:

            self.print_instruction()
            print('[프로젝트] 메뉴를 선택하세요 : ', end='')
            selected = input()

            if int(selected) == 1:
                self.new_project()
            elif int(selected) == 2:
                self.show_current_project()
            elif int(selected) == 3:
                break
