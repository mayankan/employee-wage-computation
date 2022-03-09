"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 16:40:00
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8
PART_TIME_HRS = 4


def get_attendance():
    """
    Gets Attendance whether employee is present or absent using random function.
    :return: True if employee is present else false.
    """
    return True if rd.randint(0, 1) == 1 else False


def get_work_hrs():
    """
    Gets Working Hours whether employee is working Full Time or Part Time.
    Return:
        True if employee is working Full Day else False.
    """
    return True if rd.randint(0, 1) == 1 else False


def calc_daily_wage(work_hrs):
    """
    Calculates Daily Wage for Employee working full day or part-time.
    Parameter:
        Boolean value having True if employee is working Full Day else Part Time.
    Return:
        Wage per hour multiplied to Full Day Working Hours or Part Time Working Hours
     if employee is present else 0.
    """
    if get_attendance():
        wage = WAGE_PER_HR * FULL_DAY_HRS if work_hrs else WAGE_PER_HR * PART_TIME_HRS
        return wage
    else:
        return 0


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Daily wage for Employee is {}.".format(calc_daily_wage(get_work_hrs())))


if __name__ == "__main__":
    main()
