salary_before_tax = float(input("录入税前工资："))
take_home_salary = salary_before_tax -(salary_before_tax*0.08+(salary_before_tax*0.02)+3+salary_before_tax*0.002+salary_before_tax*0.12)
print("税后工资为："+str(round(take_home_salary,2)))