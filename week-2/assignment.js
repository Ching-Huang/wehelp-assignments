/*-----------------------JavaScript-----------------------*/
// 規則:
// 運用任何你學過的 JavaScript 程式語言基本知識，不依賴任何第三方的模組或套件
// 的情況下，完成以下程式要求。

/*要求一：函式與流程控制*/
// 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
// 提醒：請勿更動題目中任何已經寫好的程式。

function calculate(min, max){
   let sum = 0;
   for(let i = min; i <= max; i++){
      sum += i;
   }
   console.log(sum);
} 
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

/*要求二：JavaScript 物件與陣列*/
// 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
// 提醒：請勿更動題目中任何已經寫好的程式。
// --->事先拆解: data = {count,employees[{name,salary},{name,salary},{name,salary}]}<---

function avg(data){
   let employeesArray = data["employees"];
   let employeesCount = data["count"];
   employeesCount = employeesArray.length;
   
   let salarySum = 0;
   for(let i = 0; i < employeesArray.length ; i++){
      let employeesSalary = employeesArray[i].salary;
      salarySum += employeesSalary;
   }
   
   let averageSalary = salarySum / employeesCount;
   console.log(averageSalary);   
} 
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
}); // 呼叫 avg 函式

/*要求三：演算法*/
// 找出至少包含兩筆整數的陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

function maxProduct(nums){
   let multipleMax = -Infinity;
   for(let i = 0; i < nums.length; i++){
      for(let j = i+1; j < nums.length; j++){
         if(nums[i]*nums[j] > multipleMax){
            multipleMax = nums[i]*nums[j];
         }
      }
   }
   if(multipleMax === -0){
      multipleMax = 0;
   }
   console.log(multipleMax);
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2

/*要求四 ( 請閱讀英文 )：演算法*/
// Given an array of integers, show indices of the two numbers such that they add up to a
// specific target. You can assume that each input would have exactly one solution, and you
// can not use the same element twice.

function twoSum(nums, target){
   for(let i = 0; i < nums.length; i++){
      for(let j = i+1; j < nums.length; j++){
         if(nums[i] + nums[j] === target){
            return [i, j];
         }
      }
   }  
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

