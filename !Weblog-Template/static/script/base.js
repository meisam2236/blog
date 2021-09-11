// Tooltip
$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });
});
// Tooltip

// Menu 
const   drowpMenu = document.querySelector('.main-header__menu li:nth-child(2)'),
        mainBaner = document.querySelector('.main-page-con'),
        backdiv = document.querySelector('.menu-back'),
        drowpMenuBox = document.querySelector('.main-header__menu li:nth-child(2) div');
drowpMenu.addEventListener('mouseover', ()=> {
    drowpMenuBox.setAttribute('active','');
})

backdiv.addEventListener('mouseleave', ()=> {
    drowpMenuBox.removeAttribute('active');
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
