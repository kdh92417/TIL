from department import Department
from project    import Project
from employee   import Employee

def print_menu():
    print("-----------------------------------")
    print("---------    Adam ERP    --------")
    print("-----------------------------------")
    print('[ 사용자 메뉴 ]\n')
    print('1 - 인사 관리')
    print('2 - 프로젝트 관리')
    print('3 - 부서 관리')
    print('4 - 프로그램 종료')
    print("-----------------------------------")

if __name__ == '__main__':
    # Project -----> Employee
    em = Employee()
    pj = Project(em)

    # Employee --> Department
    dp = Department()
    while True:
        print_menu()
        print("메뉴를 선택하세요 : ", end='')
        selected = input()

        if int(selected) == 1:
            em.executeJob(dp)
        elif int(selected) == 2:
            pj.execute_job()
        elif int(selected) == 3:
            dp.execute_job()
        elif int(selected) == 4:
            break