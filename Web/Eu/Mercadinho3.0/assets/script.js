const res = document.querySelector('.res')
const form = document.querySelector('#cadastro')
const btnCalc = document.querySelector('#btn-calc')
const btnEnviar = document.querySelector('[submit]')
const prodSpan = document.querySelector('#prod')
const data = document.querySelector('.data')
let tot = 0
let prod = 1
let lista = []

const resetLabel = () => {
    form[0].value = ''
    form[1].value = ''
}

const showData = document.querySelector('.btnShow')
showData.onclick = () => {
    // `ñ consegui fazer com ternário
    // Toggle display
    if(res.style.display == 'none') {
        res.style.display = 'block'
    }else {
        res.style.display = 'none'
    }
}

btnEnviar.onclick = e => {
    e.preventDefault()
    prodSpan.parentNode.style.display = 'block'
    const label = document.createElement('p')

    prodSpan.innerText = ++prod

    let nome = form[0].value
    let valor = form[1].value
    tot += valor
    label.innerText = `${nome} ${valor}`

    lista.push(nome)
    data.appendChild(label)
    resetLabel()
    showData.style.display = 'block'
}

const calc = () => {
    res.innerHTML = ''
    form.style.display = 'none'
    prodSpan.parentNode.style.display = 'none'

    const resul = document.createElement('div')
    resul.classList.add('resul')

    const btnBuy = document.createElement('button')
    btnBuy.innerText = 'Opções de Compra:'
    btnBuy.classList.add('btnShow')
    
    resul.innerHTML = `<h2>O resultado total dos seus produtos foi <span>R$ ${Number(tot).toFixed(2)}</span> !</h2>`
    resul.appendChild(btnBuy)
    res.appendChild(resul)

    btnBuy.onclick = e => {

    }
}