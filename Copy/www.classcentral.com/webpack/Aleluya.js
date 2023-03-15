console.log("Aleluya DEEp")

const otra = document.querySelector('#page-home > div.contain-page > header > div.relative.bg-white.cc-header.border-bottom.border-gray-light > nav > div.margin-right-small.large-up-margin-right-medium > button.hidden.weight-semi.large-up-block.text-1.color-charcoal.padding-right-small')

let html = document.querySelector('html')

let nav = document.querySelector('#page-home > div.contain-page > header > div.relative.bg-white.cc-header.border-bottom.border-gray-light > nav > div.margin-right-small.large-up-margin-right-medium > nav')
let div = document.querySelector('#page-home > div.contain-page > header > div.width-100.height-100.fixed.top.left')
let appear=document.querySelector('#page-home > div.contain-page > header > div.relative.bg-white.cc-header.border-bottom.border-gray-light > nav > div.margin-right-small.large-up-margin-right-medium > nav > div.main-nav-dropdown__index > section:nth-child(2)')
otra.addEventListener("click", reveal)

function reveal() {
    html.classList.toggle('nav-open')
    nav.classList.toggle('is-open')
    div.classList.toggle("animate-fade-hidden")
}
