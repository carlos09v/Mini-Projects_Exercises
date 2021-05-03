function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var Fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if(Fano.value.length == 0 || Number(Fano.value) > ano){
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(Fano.value)
        var gênero =  ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        if(fsex[0].checked){
            gênero = 'Homem'
            if(idade >= 0 && idade <= 12){
                // Criança
                img.setAttribute('src','crianca_homem.png')
            }else if(idade < 21){
                // Jovem
                img.setAttribute('src','jovem_homem.png')
            }else if(idade < 60){
                // Adulto
                img.setAttribute('src','adulto.png')
            }else{
                // Idoso
                img.setAttribute('src','idoso_homem.png')
            }
        }else if(fsex[1].checked){
            gênero = 'Mulher'
            if(idade >= 0 && idade <= 12){
                // Criança
                img.setAttribute('src','crianca_mulher.png')
            }else if(idade < 21){
                // Jovem
                img.setAttribute('src','jovem_mulher.png')
            }else if(idade < 60){
                // Adulto
                img.setAttribute('src','adulta.png')
            }else{
                // Idoso
                img.setAttribute('src','idoso_mulher.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
    }
}