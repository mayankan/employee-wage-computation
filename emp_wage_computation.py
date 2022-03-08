"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 17:02:00
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8
PART_TIME_HRS = 4
WORKING_DAYS = 20


def get_attendance():
    """
    Gets Attendance whether employee is present, working part-time or absent using random function.
    Return:
        2 if employee is working full day, 1 if part-time and 0 if absent.
    """
    return rd.randint(0, 2)


def calc_daily_wage():
    """
    Calculates Daily Wage for Employee working full day or part-time using case statement.
    Return:
        Wage per hour multiplied to Full Day Working Hours or Part Time Working Hours
     if employee is present else 0.
    """
    wage_calc = {
        2: WAGE_PER_HR * FULL_DAY_HRS,
        1: WAGE_PER_HR * PART_TIME_HRS,
        0: 0
    }
    return wage_calc.get(get_attendance())


def calc_monthly_wage():
    """
    Calculates Monthly Wage for Employee working full day, part-time or absent using daily wage function
     and iterating it to working days constant.
    Return:
        Monthly Wage calculated by daily wage function and iterating it to working days constant.
    """
    total_wage = 0
    day_count = 0
    while WAGE_PER_HR > day_count:
        total_wage += calc_daily_wage()
        day_count += 1
    return total_wage


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Monthly wage for Employee is {}.".format(calc_monthly_wage()))


if __name__ == "__main__":
    main()
