// Bug - script:50 - Cannot read properties of null (reading 'isSameNode')
// Bug - script:88 - Cannot read properties of null (reading 'classList')

const inputElement = document.querySelector('.new-task-input')
const addTaskButton = document.querySelector('.new-task-btn')
const tasksContainer = document.querySelector('.tasks-container')


// Validar se está vazio
const validateInput = () => inputElement.value.trim().length > 0

const handleAddTask = () => {
    const inputIsValid = validateInput()

    console.log(inputIsValid)

    if (!inputIsValid){
        return inputElement.classList.add('error')
    }

    // Criar elementos no html
    const taskItemContainer = document.createElement('div')
    taskItemContainer.classList.add('task-item')

    const taskContent = document.createElement('p')
    taskContent.innerText = inputElement.value

    taskContent.addEventListener('click', () =>  handleClick(taskContent))

    // Colocar o icone do Font Awesome
    const deleteItem = document.createElement('i')
    deleteItem.classList.add('fa-regular')
    deleteItem.classList.add('fa-trash-can')

    deleteItem.addEventListener('click', () => handleDeleteClick(taskItemContainer, taskContent))

    // Colocar a div
    tasksContainer.appendChild(taskItemContainer)
    
    taskItemContainer.appendChild(taskContent)
    taskItemContainer.appendChild(deleteItem)

    inputElement.value = ''

    updateLocalStorage()
}

const handleClick = taskContent => {
    const tasks = tasksContainer.childNodes

    for (const task of tasks) {
        const currentTaskIsBeingClicked = task.firstChild.isSameNode(taskContent)
        
        if (currentTaskIsBeingClicked){
            task.firstChild.classList.toggle('completed')
        }
    }

    updateLocalStorage()
}

const handleDeleteClick = (taskItemContainer, taskContent) => {
    const tasks = tasksContainer.childNodes

    for (const task of tasks) {
        const currtentTaskIsBeingClicked = task.firstChild.isSameNode(taskContent)
        
        if (currtentTaskIsBeingClicked){
            taskItemContainer.remove()
        }
    }

    updateLocalStorage()
}

const handleInputChange = () => {
    const inputIsValid = validateInput()

    if (inputIsValid){
        return inputElement.classList.remove('error')
    }
}

const updateLocalStorage = () => {
    const tasks = tasksContainer.childNodes

    const localStorageTasks = [...tasks].map(task => {
        const content = task.firstChild
        const isCompleted = content.classList.contains('completed')

        return { description: content.innerText, isCompleted }
    })


    localStorage.setItem('tasks', JSON.stringify(localStorageTasks))
}

const refreshTasksUsingLocalStorage = () => {
    const tasksFromLocalStorage = JSON.parse(localStorage.getItem('tasks'))

    if(!tasksFromLocalStorage) return

    for(const task of tasksFromLocalStorage) {
        // Criar elementos no html
        const taskItemContainer = document.createElement('div')
        taskItemContainer.classList.add('task-item')

        const taskContent = document.createElement('p')
        taskContent.innerText = task.description

        if(task.isCompleted) {
            taskContent.classList.add('completed')
        }

        taskContent.addEventListener('click', () =>  handleClick(taskContent))

        // Colocar o icone do Font Awesome
        const deleteItem = document.createElement('i')
        deleteItem.classList.add('fa-regular')
        deleteItem.classList.add('fa-trash-can')

        deleteItem.addEventListener('click', () => handleDeleteClick(taskItemContainer, taskContent))

        // Colocar a div
        tasksContainer.appendChild(taskItemContainer)
        
        taskItemContainer.appendChild(taskContent)
        taskItemContainer.appendChild(deleteItem)
    }
}

refreshTasksUsingLocalStorage()

addTaskButton.addEventListener('click', () =>  handleAddTask())

inputElement.addEventListener('change', () => handleInputChange())