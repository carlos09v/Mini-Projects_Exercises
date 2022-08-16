let count = 1

setInterval(function() {
    document.getElementById('slide' + count).checked = true
    count++

    if(count > 5){
        count = 1
    }

}, 4000)