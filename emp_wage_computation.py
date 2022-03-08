"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 15:00:00
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8


def get_attendance():
    """
    Gets Attendance whether employee is present or absent using random function.
    :return: True if employee is present else false.
    """
    return True if rd.randint(0, 1) == 1 else False


def calc_daily_wage():
    return WAGE_PER_HR * FULL_DAY_HRS if get_attendance() else 0


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Daily wage for Employee is {}.".format(calc_daily_wage()))


if __name__ == "__main__":
    main()
