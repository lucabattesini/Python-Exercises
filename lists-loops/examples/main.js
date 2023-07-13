//      0   1    2   3  4
list = [7, 22, 32, 14, 9, 4];
len = list.length;

// console.log(list[0]);
// console.log(list[2]);
// console.log(list[4]);

// console.log(".....");

for (let i = 0; i < len; i++) {
    console.log("início --------");
    console.log("index: ", i);
    console.log("valor: ", list[i]);
    console.log("valor do próximo: ", list[i+1]);
    console.log("valor do anterior: ", list[i-1]);
    console.log("fim ----------");
}


