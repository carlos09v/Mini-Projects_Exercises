const slider = document.querySelector('#slider')
const button = document.querySelector('#button')

const sizePassword = document.querySelector('#valor')
const passw = document.querySelector("#password")

const containerPassword = document.querySelector('#container-password')

let charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@"
let novaSenha = ''

sizePassword.innerHTML = slider.value

slider.oninput = function() {
    sizePassword.innerHTML = this.value
}

function generatePassword() {
    let pass = ''
    for(let i = 0, n = charset.length; i < slider.value; ++i){
        pass += charset.charAt(Math.floor(Math.random() * n))
    }

    containerPassword.classList.remove("hide")
    passw.innerHTML = pass
    novaSenha = pass
}

function copyPassword() {
    // Copiar senha
    navigator.clipboard.writeText(novaSenha)
}
