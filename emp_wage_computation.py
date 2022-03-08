"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 17:34:00
    @Title : Employee Wage Computation
    """
import random as rd

WAGE_PER_HR = 20
FULL_DAY_HRS = 8
PART_TIME_HRS = 4
WORKING_DAYS = 20
WORKING_HRS = 100


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
    Calculates Monthly Wage and Total Working Hours for Employee working full day,
    part-time or absent using daily wage function and iterating it to working days constant.
    Return:
        Monthly Wage and Total Working Hours calculated by daily wage function
        and iterating it to working days constant.
    """
    total_wage = 0
    day_count = 0
    while WAGE_PER_HR > day_count:
        total_wage += calc_daily_wage()
        if total_wage // 20 > 100:
            return 2000, 100
        day_count += 1
    working_hrs = (total_wage // 20)
    return total_wage, working_hrs


def main():
    print("Welcome to Employee Wage Computation Program")
    total_wage, working_hrs = calc_monthly_wage()
    print("Monthly Wage and Total Working Hours for Employee are {} and {} ."
          .format(calc_monthly_wage()[0], calc_monthly_wage()[1]))


if __name__ == "__main__":
    main()
