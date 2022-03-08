"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 16:49:00
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8
PART_TIME_HRS = 4


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


def main():
    print("Welcome to Employee Wage Computation Program")
    print("Daily wage for Employee is {}.".format(calc_daily_wage()))


if __name__ == "__main__":
    main()
