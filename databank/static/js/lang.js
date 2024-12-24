
function main() {
    registerTextareaInputListener();
    registerKeysListener();    
}

function postMainComment(text_area) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            text_area.classList.remove('comment-animation');
            text_area.offsetWidth
            text_area.classList.add('comment-animation');
        }
    }
    xhr.send(new FormData(text_area.parentNode.parentNode));
};

function postIntableSelect(select) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            select.classList.remove('select-in-table-animation');
            select.offsetWidth
            select.classList.add('select-in-table-animation');
        }
    }
    xhr.send(new FormData(select.parentNode.parentNode));
};

function postAddComment(button) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let comment = document.createElement('div');
            comment.innerHTML = xhr.response;
            addTextareaInputListener(comment.lastChild);
            document.getElementById('all_comments').appendChild(comment);
            document.getElementById(comment.lastChild.id).focus();
        }
    }
    xhr.send(new FormData(button.parentNode.parentNode));
};

function postComment(current_comment) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    
    xhr.onload = function() {
        let comments = document.getElementById('all_comments')
        if (xhr.status === 200) {
            for (let comment of comments) {
                if (comment.name == current_comment.name && current_comment.value == "")
                    comments.removeChild(comment.parentNode);
                else if (comment.nodeName == "TEXTAREA" && comment.value == "")
                    comments.removeChild(comment.parentNode);
            }
            current_comment.classList.remove('comment-animation');
            current_comment.offsetWidth
            current_comment.classList.add('comment-animation');
        }
    }

    xhr.send(new FormData(current_comment.parentNode.parentNode));
}


function addTextareaInputListener(textarea){
    textarea.style.overflowY = "hidden";
    textarea.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = this.scrollHeight + "px";
        this.innerHTML = this.value;
    });
}

function registerTextareaInputListener() {
    document.querySelectorAll("textarea").forEach(function(textarea) {
        textarea.style.height = textarea.scrollHeight + "px";
        addTextareaInputListener(textarea);
    });
};

function registerKeysListener() {
    document.body.addEventListener('keydown', function(e) {
        console.log(e);
        if (e.key == "Escape") {
            e.target.blur();
        }
        else if (e.ctrlKey && e.key == "Enter") {
            e.target.blur();
            setTimeout(function() {document.getElementsByClassName('add-comment-button')[0].click();},100)
            // console.log(document.getElementsByClassName('add-comment-button')[0])
            
        }
      });
}