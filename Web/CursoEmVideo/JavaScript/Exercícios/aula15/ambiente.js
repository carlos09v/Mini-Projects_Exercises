let num = [5,8,3,9,5]
num.push(2) // Append
num.sort() // Ordenar
console.log(`Nosso vetor é o ${num}.`)
console.log(`O vetor tem ${num.length} elementos.`) // Len
console.log(`O primeiro valor do vetor é o ${num[0]}.`)

let pos = num.indexOf(8)
if(pos == -1){
    console.log('O valor não foi encontrado!')
}else{
    console.log(`O valor 8 está na posição ${pos}`)
}
