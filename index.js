/*// let diceRoll;
// while (diceRoll !== 6) {
//   diceRoll = Math.floor(Math.random() * 6) + 1;
//   console.log(`Rolled a ${diceRoll}`);
// }
// Output: Rolled a 4, Rolled a 2, Rolled a 6 (when 6 is rolled)
// let secondsLeft = 10;
// while (secondsLeft >= 0) {
//   console.log(`Countdown: ${secondsLeft}`);
//   secondsLeft--;
// }
// Output: Countdown: 10, Countdown: 9, ..., Countdown: 0*/
// let age;
// while (isNaN(age) || age < 18) {
//   age = prompt("Please enter your age:");
// }
// console.log(`You are ${age} years old.`);


// let num = 7;
// let guess;
// while(guess != num){
//   let guess = prompt("Guess the correct number");
// }
// console.log("congratulations");

// const secretNumber = 7;
// let guess;

// while (guess !== secretNumber) {
//   guess = prompt("Guess a number between 1 and 10:");
// }

// console.log("You guessed it!");



// let a = 0;
// let sum = 0;
// while (a<101) {
//   if(a % 2 == 0){
//     sum +=a;
//   }
//   a++
    
// }
// console.log(sum)

// console.log("To printing the even numbers");
// let num = 0;
// while(num<20){
//   if(num % 2 == 0){
//     console.log(num)
//     num++;
//   }
//   num++;
//   // console.log(num);
// }



// function sum(a,b) {
//   console.log("Sum of 2 & 4 is " + sum(2,4) + "enough");
//   return a+b;
// }
// sum(2,4);
// console.log("The result of 2 & 4 are by addition is",result)


// function myfunction() {
//   let carname = "BMW";
//   console.log("My new car is " +carname);
// }
// myfunction();
// // console.log(myfunction(carname));



// function sayhello(name){
//   return "welcome " +name+ " !";
// }
// var greet=sayhello("Sanket");
// console.log(greet);
// var greet1=sayhello("Rama")
// console.log(greet1)


// #function of addition --------->
// function sum(a,b) {
//   return a+b
  
// }
// result = sum(446,44)
// console.log(result)

// # constant of function-------->
// const func1 =(s) =>{
//   console.log(s)
// }
// func1(34)

// <!-- business well_name generator ----------->
// let rand = Math.random();
// console.log(rand);
// let first,second,third;
// if(rand < 0.33){
//   first =" amazing";
// }
// else if(0.33<rand && rand<0.66){
//   first="crazy";
// }
// else{
// first="great";
// }

// let rand1 =Math.random()
// if(rand1 < 0.33){
//   second =" cafe";
// }
// else if(0.33<rand1 && rand1<0.66){
//   second="cloths";
// }
// else{
//   second="network";
// }

// let rand3 = Math.random()
// if(rand3 < 0.33){
//   third = "hub";
// }
// else if(0.33<rand3 && rand3<0.66){
//   third="center";
// }
// else{
//   third="zone";
// }
// console.log(`${first} ${second} ${third}`);


// OTP GENERATOR--------------------------------------------------------------->
// function generateOTP(limit) {
//     let digits = '0123456789';
//     let otp =' ';
//     for(let i=0;i<limit;i++){
//         otp=otp+ digits[Math.floor(Math.random()*10)]
//     } 
//     return otp;
//     // console.log(otp)
// }
// console.log(`Hey your OTP is${generateOTP(6)}`)
// // console.log("your otp is "+generateOTP(6))
// console.log("Don't Share your OTP.")


// for(let i=0;i<10;i++){
//     console.log(i)
// }



//ARRAYS---------------------------------------------------------------------->
// const cars = ["Bmw","Mercedes Benz","Rolls Royce"]
// let car = cars.toString()
// console.log(cars)
// console.log(car)
// console.log(cars[2])
// let carrr = cars.length
// let carr = cars.push("Volks wagen 215")
// console.log(carrr)
// console.log(carr)
// // let pop = cars.pop()
// // console.log(pop)
// console.log(cars)



// const fruits = ["Orange","Grapes","Grapes","Water mellon"]
// const cars = ["BMW","Rolls Royce"]
// console.log("Before inserting fruits list are :- " +fruits)
// let fruits1 = fruits.push("Mango","Custerd apple");
// console.log("After inserting some fruits :-" +fruits)
// // let pop = fruits.pop()
// // console.log(pop)
// console.log(fruits)
// let concat = fruits.concat(cars)
// console.log(concat)

// let name = "Sanket";
// let firstLetter = name[name.length-6];
// console.log(firstLetter)

// function myfunction(name,age,college,adress) {
//     fullname = "";
//     fullname += `My name is ${name} and my age ${age} my college is ${college}`
//     return fullname;
    
// }
// console.log(myfunction("sanket",21,"DR Smce"))

// // let decide = Math.random()
// console.log(decide)
// console.log("Lets make debut with computer ")
// if (decide<0.5) {
//     console.log("probability of your '")
    
// }
// else{
//     console.log("No your '")
// }





// function arithmatic(a,b){
//     console.log(a+b)
//     console.log(a-b)
//     console.log(a*b)
//     console.log(a/b)

// }
// let cars = ["car1","car2"]
// let carr = cars.push(["car3","car44","car4"])
// // let carrr = cars.pop()
// console.log(cars)

// arithmatic(4,2)


// function arrpass(arr,item) {
//     arr.push(item)
//     return item;   
// }
// let typearr = [1,2,3,4,5]
// // console.log(arrpass(typearr,6))
// console.log(typearr)

// function comparision(num){
//     if(num === 12){
//         return "it is true"
//     }
//     return "it is not true"
// }
// console.log(comparision("j"))


// function factorial(n){
//     let fact=1;
//     for(let i=1;i<=n;i++){
//         fact*=i
//     }
//     return fact;
// }
// console.log(factorial(5))


// let filmKGF = {
//     "hero":"yash",
//     "director":"prashant",
//     "budget":"100 crore",
//     "collection":"1250 crore"

// }
// filmKGF['production'] = "Hombale films"
// let herofilmKGF = filmKGF.hero;
// console.log(filmKGF)


// function random(max,min){
//     return Math.floor(Math.random()*(max-min+1))+min;
// }
// let randomrange=random(1,100)
// console.log(randomrange)


// function evall(a,b){
//      return eval(a*b)
// }
// console.log(evall(2,4))


// let num = 5;
// //           5        7      7      9
// console.log(num++ + ++num + num++ + ++num + ++num)

// let random = Math.floor(Math.random()*10)
// console.log(random)


// let object = {
//         stdName : "Sanket",
//         usn : "1CC21CS052",
//         pass : true,
//         sem : [1,2,3,4,5]
// }
// console.log(object.pass)

// let person = {
//     Myname : "Sanket",
//     age : 20,
//     country : "India"
// }
// function personobj(){
//     let details = `${person.Myname} is ${person.age} years old and lives in ${person.country}`
//     console.log(details)
// }
// personobj()


// less than 6 years old -> free
// 6 to 17 years old     -> child discount
// 18 to 26 years old    -> student discount
// 27 to 66 years old    -> full price
// over 66 years old     -> senior citizen discount

// let age = 67; 
// if (age <= 6) {
//     console.log("free")
// }
// else if (age >= 6 && age <=17){
//     console.log("child discount")
// }
// else if( age >= 18 && age <= 26 ){
//     console.log("Student discount")
// }
// else if( age >= 27 && age <= 66 ){
//     console.log("Full price")
// }
// else if( age >= 67 && age <= 120){
//     console.log("Senior citizen discount")
// }
// else{
//     console.log("Age is not possible")
// }


// let country = ["India","USA","UAE","UK","USSR"]
// // for ( let i = 0;i<=country.length;i++){
    
//     // }
//     for (let index = 0; index < country.length; index++) {
//         const element = country[index];
        
//         console.log(element)
//     }

// let largeCountries = ["Tuvalu","India","USA","Indonesia","Monaco"]
// largeCountries.shift()
// largeCountries.pop(3)
// largeCountries.push("China")
// largeCountries.unshift("Russia")

// console.log(largeCountries)


// let date = 12
// let day = "friday"
// if(date == 13 && day == "friday"){
//     console.log("😂")
// }
// else{
//     console.log("😒")
// }


// let hands = ["🐉", "🐥", "🐊","💩", "🦍", "🐢", "🐩", "🦭",
//  "🦀", "🐝", "🤖", "🐘", "🐸", "🕷","🐆", "🦕", "🦁"]
// function random(){
//      let get = Math.floor(Math.random() * hands.length)
//     return hands[get]
// }
// console.log(`${random()} vs ${random()}`)

// addEventListener("click", function(){

// }


// let arr = ["com","in","org"]
// let listEl = document.getElementById("list-el")

// for (let i=0;i<arr.length;i++){
//     listEl.innerHTML += "<li>" + arr[i] +"</li>"
// }


// function factorial(num){
//     let fac = 1;
//     for(let i=1;i<=num;i++){
//         fac*=i
//     }
//     // console.log(fac)
//     return fac
// }
// console.log(factorial(5))


// for (let i = 1;i<18;i+=2){
//     console.log(i)

// }
// function factorial(num){
//     let fac=1
//     for (var i =1;i<=num;i++){
//      fac*=i
//     //  console.log(i)
//     console.log(`${i}=${fac}`)
//     }
//     return fac
//     }


// // let result =   factorial(1000)
// // // console.log(result)

// arrow function 
// let add = (a,b)=>a*b;

// console.log(add(3,2))


let points = [1,22,45,67,89,34,245,91]
console.log(points[2])
console.log(points.sort(function(a,b){return a-b}))
let math= Math.random()
console.log(math)
console.log(Math.round(math*10))