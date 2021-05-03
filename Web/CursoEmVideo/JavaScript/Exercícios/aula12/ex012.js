var agora = new Date()
var atual = agora.getHours()
var hora = 9
console.log(`Agora são exatamente ${atual} horas.`)
if(atual<5){
    console.log('Boa Madrugada!')
}else if(atual<12){
    console.log('Bom Dia')
}else if(atual<18){
    console.log('Boa Tarde!')
}else{
    console.log('Boa Noite!')
}