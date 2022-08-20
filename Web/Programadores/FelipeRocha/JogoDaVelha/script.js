// Selecionar todas celulas
const cellElements = document.querySelectorAll('[data-cell]'),
board = document.querySelector("[data-board]"),
winningMessage = document.getElementById('winning-p'),
winningModal = document.querySelector("[data-winning-message]"),
restartButton = document.getElementById('restart-btn')

let isCircleTurn

const winnigCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

const startGame = () => {
    isCircleTurn = false
    
    for(const cell of cellElements){
        cell.classList.remove('circle')
        cell.classList.remove('x')
        cell.removeEventListener('click', handleClick)
        cell.addEventListener('click', handleClick, { once: true })
    }


    setBoardHoverClass()
    winningModal.classList.remove('show-winning-message')
}

const endGame = (isDraw) => {
    isDraw ? winningMessage.innerHTML = 'Empate!' : winningMessage.innerHTML = isCircleTurn ? 'O Venceu' : 'X Venceu'

    winningModal.classList.add('show-winning-message')
}

const checkForWin = (currentPlayer) => {
    return winnigCombinations.some( combination => {
        return combination.every( index => {
            return cellElements[index].classList.contains(currentPlayer)
        })
    })
}

const checkForDraw = () => {
    return [...cellElements].every( cell => {
        return cell.classList.contains('x') || cell.classList.contains('circle')
    })
}

const placeMark = (cell, classToAdd) => {
    cell.classList.add(classToAdd)
}

const setBoardHoverClass = () => {
    board.classList.remove('circle')
    board.classList.remove('x')

    isCircleTurn ? board.classList.add('circle') : board.classList.add('x') 
}

const swapTurns = () => {
    isCircleTurn = !isCircleTurn

    setBoardHoverClass()
}

const handleClick = (e) => {
    // Colocar a marca X ou Circulo
    const cell = e.target
    const classToAdd = isCircleTurn ? 'circle' : 'x'

    placeMark(cell, classToAdd)
    // Verificar Vitoria e Empate
    const isWin = checkForWin(classToAdd)
    
    const isDraw = checkForDraw()
    
    if (isWin) {
        endGame(false)
    }else if (isDraw) {
        endGame(true)
    }else {
        // Mudar Símbolo

        swapTurns()
    }
}

startGame()

restartButton.addEventListener('click', startGame)