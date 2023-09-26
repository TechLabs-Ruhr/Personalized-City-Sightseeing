const radioText = document.querySelector('#radioText');
const radioVideo = document.querySelector('#radioVideo');

const duration = document.querySelector('#duration');

radioText.addEventListener('change', e => {
    console.log('radioText');
    let element = document.createElement('input');
    element.type = 'url';
    element.name = 'content';
    element.required = true;
    element.placeholder = 'URL';
    document.querySelector('#content').replaceWith(element);
    element.id = 'content';

    duration.required = false;
});

radioVideo.addEventListener('change', e => {
    console.log('radioVideo');
    let element = document.createElement('textarea');
    element.name = 'content';
    element.required = true;
    element.placeholder = 'YouTube-Embed-Code';
    document.querySelector('#content').replaceWith(element);
    element.id = 'content';

    duration.required = true;
});