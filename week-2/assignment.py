# <-----------------------Python----------------------->
# 規則:
# 運用任何你學過的 Python 程式語言基本知識，不依賴任何第三方的模組或套件
# 的情況下，完成以下程式要求。
# 注意：請使用 Python 3 以上的版本進行開發。

# /*要求一：函式與流程控制*/
# // 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
# // 提醒：請勿更動題目中任何已經寫好的程式。

def calculate(min, max):
    sum = 0
    for a in range(min, max+1):
        sum += a
    else:
        print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# /*要求二：Python 字典與列表*/
# 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
# 提醒：請勿更動題目中任何已經寫好的程式。

def avg(data):
    employeesArray = data["employees"]
    employeesCount = data["count"]
    employeesCount = len(employeesArray)
    
    salarySum = 0
    for i in range(len(employeesArray)):
        employeesSalary = employeesArray[i]["salary"]
        salarySum += employeesSalary
    averageSalary = salarySum / employeesCount
    print(averageSalary)
    
avg({
    "count":3,
    "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
    ]
}) # 呼叫 avg 函式


# 要求三：演算法
# 找出至少包含兩筆整數的列表 (Python) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
    import math
    multipleMax = -math.inf
    for i in range(0, (len(nums)-1)+1):
        for j in range(i+1, (len(nums)-1)+1):
            if nums[i]*nums[j] > multipleMax:
                multipleMax = nums[i]*nums[j]
    print(multipleMax)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

# 要求四 ( 請閱讀英文 )：演算法
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums, target):
    for i in range(0, (len(nums)-1)+1):
        for j in range(i+1, (len(nums)-1)+1):
            if nums[i] + nums[j] == target:
                return [i,j]

result = twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
