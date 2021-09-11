// Tooltip
$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });
});
// Tooltip

// Menu 
const   drowpMenu = document.querySelector('.main-header__menu li:nth-child(2)'),
        mainBaner = document.querySelector('.main-page-con'),
        drowpMenuBox = document.querySelector('.main-header__menu li:nth-child(2) div');
drowpMenu.addEventListener('mouseover', ()=> {
    drowpMenuBox.setAttribute('active','')
})

drowpMenu.addEventListener('click', ()=> {
    if(drowpMenuBox.hasAttribute('active')) {
        drowpMenuBox.removeAttribute('active')
    }else
    drowpMenuBox.setAttribute('active','')
})

mainBaner.addEventListener('click', ()=> {
    if(drowpMenuBox.hasAttribute('active')) {
        drowpMenuBox.removeAttribute('active')
    }
})
