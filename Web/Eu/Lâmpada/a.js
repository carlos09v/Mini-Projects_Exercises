let lamp = document.getElementById('foto1')
const res = document.getElementById('res')
lamp.addEventListener('mouseenter', acender)
lamp.addEventListener('mouseout', apagar)
function acender(){
    lamp.setAttribute('src','lampada-on.jpg')
    res.innerHTML = 'Acendeu !'
}
function apagar(){
    lamp.setAttribute('src','lampada.jpg')
    res.innerHTML = 'Apagou !'
}