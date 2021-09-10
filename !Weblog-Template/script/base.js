const   drowpMenu = document.querySelector('.main-header__menu li:nth-child(2)'),
        mainBaner = document.querySelector('.main-page-con'),
        drowpMenuBox = document.querySelector('.main-header__menu li:nth-child(2) div');


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
