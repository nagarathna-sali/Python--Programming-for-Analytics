### Problem 1 - Solution
empName=input("Employee Name: ") 
empNumber=input("Employee Number: ") 
weekEnding=str(input("Week ending: ")) #input for week ending in date format
noOfHoursWorked=float(input("Number of hours worked: ")) 
hourlyRate=float(input("Hourly Rate: ")) #hourly rate for standard working hours
overtimeRate=float(input("Overtime Rate: ")) # rate for overtime hours
stdTaxRate=float(input("Standard Tax Rate: ")) #tax rate for standard hours
overtimeTaxRate=float(input("Overtime Tax Rate: ")) #tax rate for overtime hours
##variable for total standard Hours
tot=hourlyRate*37.50 
###variable Overtime Hours is Number of hours worked minus standard working week hours 37.5
overTimeHrs=noOfHoursWorked-37.50 
#####variable for overtime pay is Hourly Rate multiplied by overtime rate for example 1.5
overTimePay=hourlyRate*overtimeRate 
### variable for total overtime is Total amount to be paid for overtime is over time hours * Overtime pay
totOvertime=overTimeHrs*overTimePay 
stdTaxCalc=stdTaxRate/100 ###standard Tax calculation percentage
overTimetaxcalc=overtimeTaxRate/100###Overtime Tax calculations percentage
dedStdTime=round((tot*stdTaxCalc),2) ### Tax deduction for standard/normal hours
dedOvrTime=round((totOvertime*overTimetaxcalc),2)  ### Tax deduction for Overtime hours
####Total Pay =total pay for standard hours +total pay for Overtime hours
totalPay=round((tot+totOvertime),2) 
#### variable for total deduction deduction for normal hours + deduction for Overtime Hours
toDeductions=round((dedStdTime+dedOvrTime),2) 
##Printing payslip
print("\t\t\t\t"," ".join("PAYSLIP"),"\t\t\t")#join function will add space between letters
print("WEEK ENDING ",weekEnding)
print("Employee: ",empName.title()) #title function capitalizes each word 
print("Employee Number: ",empNumber)
print("\t\t\t Earnings\t\t Deductions")
print("\t\t\t Hours\t","Rate\t","Total")
print("Hours (normal)\t\t","37.50\t",hourlyRate,"\t",tot," Tax @",stdTaxRate,"%",dedStdTime)
print("Hours (overtime)\t",overTimeHrs,"\t",overTimePay,"\t",totOvertime,"\t","Tax @",overtimeTaxRate,"%",dedOvrTime)
print()
print("\t\t\t Total pay:\t\t\t    ",tot+totOvertime)
print("\t\t\t Total Deductions:\t\t    ",dedStdTime+dedOvrTime)
print("\t\t\t Net Pay:\t\t\t    ",totalPay-toDeductions)