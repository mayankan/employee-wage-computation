"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 15:00:00
    @Title : Employee Wage Computation
    """
import random as rd


def get_attendance():
    return True if rd.randint(0, 1) == 1 else False


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Employee is present.") if get_attendance() else print("Employee is absent.")


if __name__ == "__main__":
    main()
