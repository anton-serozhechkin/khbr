let videoArray = document.querySelectorAll("iframe");
let followButton = document.querySelectorAll('.index-follow-button');

if (screen.width <= 375) {
    for (let i = 0; i < videoArray.length; i++) {
       videoArray[i].width = '100%';
    }
}
if (screen.width <= 414) {
    for (let i = 0; i < videoArray.length; i++) {
       videoArray[i].width = '100%';
    }
}
if (screen.width <= 768) {
    for (let i = 0; i < videoArray.length; i++) {
       videoArray[i].width = '100%';
    }
}
