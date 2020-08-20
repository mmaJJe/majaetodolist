const toggleBtn = document.querySelector(".toggleBtn")
const todoInputBox = document.querySelector(".todoInputBox")
const todoInput = document.querySelector(".todoInput")

toggleBtn.addEventListener("click", function(){
        toggleBtn.classList.toggle("close")
        todoInputBox.classList.toggle("close")
        todoInput.classList.toggle("close")
})

const slider = document.querySelector(".slider")
const toggleToDark = document.querySelector(".toggleToDark")
const ds = document.querySelectorAll(".d")

function found() {
    let localDark = localStorage.getItem("DARK")
    console.log(localDark)
    if (localDark==="true"){
        console.log("turn Dark")
        Dark = localDark
        onOff()
        localStorage.setItem("DARK", "true")
    } else{
        let Dark = false
        localStorage.setItem("DARK", Dark)
        console.log("turn birght")
    }
}

function onOff(){
    let Dark = localStorage.getItem("DARK")
    console.log(Dark)
    console.log("onof")

    slider.classList.toggle("on")
    toggleToDark.classList.toggle("on")
    if (Dark === "false"){
        Dark = true
    } else {
        Dark = false
    }
    ds.forEach(d=>d.classList.toggle("on"))
    localStorage.setItem("DARK", Dark)
}



slider.addEventListener("click", onOff )

found()