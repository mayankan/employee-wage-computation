"""
    @Author: Mayank Anand
    @Date: 2022-03-08 15:00:00
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-08 17:57:00
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
        Monthly Wage and Daily Wage dictionary calculated by daily wage function
        and iterating it to working days constant.
    """
    day_count = 0
    daily_wage = {}
    while WAGE_PER_HR > day_count:
        daily_wage[day_count] = calc_daily_wage()
        if sum(daily_wage.values()) // 20 > 100:
            return 2000, daily_wage
        day_count += 1
    total_wage = sum(daily_wage.values())
    return total_wage, daily_wage


def main():
    print("Welcome to Employee Wage Computation Program")
    total_wage, daily_wage = calc_monthly_wage()
    working_hrs = (total_wage // 20)
    print("Monthly Wage and Total Working Hours for Employee are {} and {} ."
          .format(total_wage, working_hrs))
    print("Daily Wage for Employee is: ")
    for day, wage in daily_wage.items():
        print(day+1, " - ", wage)


if __name__ == "__main__":
    main()
