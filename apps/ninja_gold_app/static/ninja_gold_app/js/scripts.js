//This forces our textarea window to the bottom to show player updates as they happen.
function forceTextToBottom(){
    var textarea = document.getElementById('text_output');
    textarea.scrollTop = textarea.scrollHeight;
}