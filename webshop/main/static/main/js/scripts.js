const sec1 = document.querySelector('.name-bio')
const header = document.querySelector('header')
const header2 = document.querySelector('#header2')



setTimeout(function bioname() {
    anime({
        targets: sec1,
        translateX: '20px',
        duration: 2000,
        opacity: 1,
    })
}, 1000);

setTimeout(function headerOpac() {
    anime({
        targets: [header, header2],
        opacity: 1,
        duration: 2000,
    })
}, 1000);

