const level = document.getElementById('level'),
visor = document.getElementById('visor'),
frutatxt = document.getElementById('frutatxt'),
img = document.getElementById('fruit1'),
btn = document.getElementsByClassName('btn'),
rebirth = document.querySelector('header h3'),
rebirValue = document.querySelector('#rebirth-value'),
body = document.querySelector('body')


let count = 0
let countlv = 1
let reb = 0


img.addEventListener('click', e => {
  count++

  frutatxt.innerHTML = 'Continue Clicando ! 😀'
  visor.textContent = count

  if (count == 25) {
    countlv += 1
    level.innerText = countlv
    level.style.color = 'green'
    img.setAttribute('src', './assets/pexels-cachoBanana1.jpg')
    img.parentNode.style.padding = '2px'
  }else if (count == 50) {
    countlv += 1
    level.innerText = countlv
    level.style.color = 'blue'
    img.setAttribute('src', './assets/pexels-cachoBanana2.jpg')
  }else if(count == 75) {
    countlv += 1
    level.innerText = countlv
    level.style.color = 'red'
    frutatxt.innerHTML = "FINAL BOSS !!"
    img.setAttribute('src', './assets/pexels-bananeira.jpg')
  }else if(count == 100) {
    countlv += 1
    level.innerText = countlv
    img.parentNode.style.display = 'none'
    level.style.color = 'purple'
    frutatxt.innerHTML = " 🎆 CONGRATULATIONS ! 🎆"
  
    const makeRebirth = document.createElement('p')
    makeRebirth.innerHTML = '⬇️ Faça o rebirth ⬇️'
    makeRebirth.style.textAlign = 'center'
    frutatxt.appendChild(makeRebirth)
  
    btn[0].style.display = 'none'
    btn[1].style.display = 'block'
  }
})

function rebir() {
  reb += 1
  rebirValue.innerText = reb
  rebirth.style.display = 'block'
  body.style.backgroundColor = 'blueviolet'
  img.parentNode.style.display = 'block'
  btn[0].style.display = 'block'
  btn[1].style.display = 'none'
  
  reset()
}

function reset() {
  countlv = 1
  count = 0
  
  level.innerText = countlv
  visor.innerText = count
  level.style.color = 'black'
  frutatxt.innerHTML = '⬇️ Clique na Banana ⬇️'
  img.parentNode.style.padding = '20px'
  img.setAttribute('src', './assets/banana.jpg')
}

function hack() {
  countlv = 4
  count = 99
  level.innerText = countlv
  level.style.color = 'red'
  visor.innerText = count

  img.parentNode.style.padding = '2px'
  img.setAttribute('src', './assets/pexels-bananeira.jpg')
}


