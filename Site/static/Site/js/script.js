function scrollToBottom() {
    var commentsContainer = document.querySelector('.comments-container');
    commentsContainer.scrollTop = commentsContainer.scrollHeight;
}

window.onload = scrollToBottom;
document.getElementById('commentForm').addEventListener('submit', function () {
    scrollToBottom();
});

