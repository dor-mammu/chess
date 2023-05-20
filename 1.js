var userId = 1; // 전역변수 => 어떠한 코드블럭에서 얘를 바꿈 => 진짜로 통쨰로 바뀜
let id = 2; // 지역변수
const idid = 3; // 상수

var userName = 'Chess';

var user = {id: 1, name: 'Chess'}; // 딕셔너리 = object 객체

var users = [
    {id:1, name:'Chess'},
    {id:2, name:'.com'}
]; // 배열

for (let i = 0; i < users.length; i++) {
    console.log(users[i].name)
}

console.log(0 == "0") // value
console.log(0 === "0") // 자료형 + 값

if (true) {
    console.log("")
}

else if (true) {

}

else {}

// 삼항 조건 "?"
var a = 1;

var result = a == 2 ? 2 : 3// 앞에 조건, 뒤에 결과
console.log(result)

// and: && or:|| not: !==
var a = 1;
switch (a) {
    case 1:
    case 3:
        break // and
    case 2:
        break
} // 간단하게 나타내는게 더 보기 편할때 => switch case