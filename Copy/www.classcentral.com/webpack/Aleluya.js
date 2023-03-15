
console.log("Aleulya")
const button = document.querySelector('.hidden weight-semi large-up-block text-1 color-charcoal padding-right-small')
let html = document.querySelector('html')
let nav = document.querySelector('nav')
let div = document.querySelector('width-100 height-100 fixed top left animate-fade-hidden')

button.addEventListener("click", reveal)

function reveal(params) {
    html.classList.toggle('nav-open')
    nav.classList.toggle('is-open')
    div.classList.toggle("animate-fade-hidden")
}