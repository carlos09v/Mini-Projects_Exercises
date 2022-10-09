const level = document.getElementById('level'),
visor = document.getElementById('visor'),
frutatxt = document.getElementById('frutatxt'),
img = document.getElementById('fruit1'),
btn = document.getElementsByClassName('btn')


let count = 0
let countlv = 1


img.addEventListener('click', e => {
  count++

  frutatxt.innerHTML = 'Continue Clicando ! 😀'
  visor.textContent = count

  if (count >= 25) {
    countlv + 1
    level.innerText = countlv
    level.style.color = 'green'
  }
  
  if (count >= 50) {
    countlv + 1
    level.innerText = countlv
    level.style.color = 'blue'
  }
  
  if (count >= 75) {
    countlv + 1
    level.innerText = countlv
    level.style.color = 'red'
    frutatxt.innerHTML = "FINAL BOSS !!"
  }
  
  if (count == 100) {
    countlv + 1
    level.style.color = 'purple'
    frutatxt.innerHTML = " 🎆 CONGRATULATIONS ! 🎆"
  }else if (count > 100) {
    reset()
  }
})



function reset() {
  count = 0
  visor.textContent = count
  frutatxt.innerHTML = '⬇️ Clique na Banana ⬇️'
}


