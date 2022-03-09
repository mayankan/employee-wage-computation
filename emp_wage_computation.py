"""
    @Author: Mayank Anand
    @Date: 2022-03-08
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8
PART_TIME_HRS = 4
WORKING_DAYS = 20


def get_attendance():
    """
    Gets Attendance whether employee is present or absent using random function.
    Return:
        True if employee is present else false.
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
    Calculates Daily Wage for Employee working full day or part-time using case statement.
    Return:
        Wage per hour multiplied to Full Day Working Hours or Part Time Working Hours
     if employee is present else 0.
    """
    wage_calc = {
        True: FULL_DAY_HRS * WAGE_PER_HR,
        False: PART_TIME_HRS * WAGE_PER_HR
    }
    attendance = {
        True: wage_calc.get(work_hrs),
        False: 0
    }
    return attendance.get(get_attendance())


def calc_monthly_wage():
    """
    Calculates Monthly Wage for Employee working full day, part-time or absent using daily wage function
     and iterating it to working days constant.
    Return:
        Monthly Wage calculated by daily wage function and iterating it to working days constant.
    """
    total_wage = 0
    day_count = 0
    while WORKING_DAYS > day_count:
        total_wage += calc_daily_wage()
        day_count += 1
    return total_wage


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Monthly wage for Employee is {}.".format(calc_monthly_wage()))


if __name__ == "__main__":
    main()
