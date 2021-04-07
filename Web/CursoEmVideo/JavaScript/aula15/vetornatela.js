let valores = [0,5,3,9,4,5]
// valores.sort()
/*
for(let pos = 0;pos < valores.length;pos++){
    console.log(`A posição ${pos+1} tem o valor ${valores[pos]}`)
}
*/
for(let pos in valores){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}

console.log(valores.indexOf(3))
console.log(valores.indexOf(15)) // -1 = Não encontrado
