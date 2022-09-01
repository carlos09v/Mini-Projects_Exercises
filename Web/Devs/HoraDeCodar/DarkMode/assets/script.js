const changeThemeBtn = document.querySelector('#change-theme')

// Toggle dark mode
const toggleDarkMode = () => {
    document.body.classList.toggle('dark')
}

// Load light or dark mode
const loadTheme = () => {
    const darkMode = localStorage.getItem('dark')

    if(darkMode){
        toggleDarkMode()
    }
}

loadTheme()

changeThemeBtn.addEventListener('change', () => {
    toggleDarkMode()

    // Save or remove dark mode
    localStorage.removeItem('dark')

    if(document.body.classList.contains('dark')){
       localStorage.setItem('dark', 1) 
    }
})