const img = document.querySelector('#product-image')


const colors = document.querySelectorAll('.color')
const green = document.getElementById('green').childNodes[1],
silver = document.getElementById('silver').childNodes[1],
golden = document.getElementById('golden').childNodes[1],
grafite = document.getElementById('grafite').childNodes[1],
blue = document.getElementById('blue').childNodes[1]

green.addEventListener('click', () => {
    colors.forEach(a => {
        if(a.classList.contains('selected')){
            a.classList.remove('selected')
        }
    })

    green.classList.add('selected')
    img.src = './assets/img/iphone_green.jpg'
})

silver.addEventListener('click', () => {
    colors.forEach(a => {
        if(a.classList.contains('selected')){
            a.classList.remove('selected')
        }
    })
    
    silver.classList.add('selected')
    img.src = './assets/img/iphone_silver.jpg'
})

golden.addEventListener('click', () => {
    colors.forEach(a => {
        if(a.classList.contains('selected')){
            a.classList.remove('selected')
        }
    })
    
    golden.classList.add('selected')
    img.src = './assets/img/iphone_golden.jpg'
})

grafite.addEventListener('click', () => {
    colors.forEach(a => {
        if(a.classList.contains('selected')){
            a.classList.remove('selected')
        }
    })
    
    grafite.classList.add('selected')
    img.src = './assets/img/iphone_grafite.jpg'
})

blue.addEventListener('click', () => {
    colors.forEach(a => {
        if(a.classList.contains('selected')){
            a.classList.remove('selected')
        }
    })
    
    blue.classList.add('selected')
    img.src = './assets/img/iphone_blue.jpg'
})


