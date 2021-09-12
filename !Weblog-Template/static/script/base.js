// Tooltip
$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });
});
// Tooltip

// Menu list
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

// Menu respo

const menuBox = document.querySelector('.main-header__menu ul');
const colexit = document.querySelector('.collpase-menu i');
const backBlack = document.querySelector('.blackBack');

colexit.addEventListener('click', ()=> {

  if(colexit.classList.contains('fa-bars')) {
    colexit.classList = 'fas fa-times';
    menuBox.style.right = 0;
    backBlack.style.display = 'block';
    console.log(backBlack)
  }else {
    colexit.classList = 'fas fa-bars';
    menuBox.style.right = '-180px';
    backBlack.style.display = 'none';
    drowpMenuBox.removeAttribute('active');
  }
})

backBlack.addEventListener('click', () => {
  colexit.classList = 'fas fa-bars';
  menuBox.style.right = '-180px';
  backBlack.style.display = 'none';
  drowpMenuBox.removeAttribute('active');
})

