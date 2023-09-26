var unfolded = false;

document.getElementById('burgermenu').addEventListener('click', e => {
    if(unfolded) {
        document.querySelector('nav').style.display = 'none';
    } else {
        document.querySelector('nav').style.display = 'flex';
    }
    unfolded = !unfolded;
})