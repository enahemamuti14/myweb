//toggle 
const navbarNav = document.querySelector('.navbar-nav');

//buat si sidebarnya ada pas di klik
document.querySelector('#menu').onclick = () => {
    navbarNav.classList.toggle('active');
};

// // buat si sidebarnya ilang dari halaman nav ini gatau errornya kenapa
// const menuu = document.querySelector('#menu');

// document.addEventListener('click', function (e) {
//     if (!menuu.contains(e.target) && !navbarNav.contains(e.target)) {
//         navbarNav.classList.List.remove('active');
//     }
// });