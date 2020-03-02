
"""
计算从1970年到2050年之间所有的闰年
"""


leap_year = [year for year in range(1970, 2051) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]
print(leap_year)
