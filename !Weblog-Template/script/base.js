const   drowpMenu = document.querySelector('.main-header__menu li:nth-child(2)'),
        drowpMenuBox = document.querySelector('.main-header__menu li:nth-child(2) div');


drowpMenu.addEventListener('click', ()=> {
    if(drowpMenuBox.hasAttribute('active')) {
        drowpMenuBox.removeAttribute('active')
    }else
    drowpMenuBox.setAttribute('active','')
})
