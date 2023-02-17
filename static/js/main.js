// delete alerts
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
    alertClose.addEventListener('click', () => alertWrapper.style.display = 'none')
}

// save search form param
let search_form = document.getElementById('search_form')
let page_links = document.getElementsByClassName('page-link')

if (search_form) {
    for(let i = 0; page_links.length > i; i++) {
        page_links[i].addEventListener('click', function (e) {
            e.preventDefault()

            let page = this.dataset.page

            search_form.innerHTML += `<input value=${page} name="page" hidden />`

            search_form.submit()
        })
    }
}

//Likes/Dislikes api
let token = localStorage.getItem('token')
let vote_btns = document.getElementsByClassName('vote--option')

if (vote_btns.length > 0) {
    for (let i = 0; vote_btns.length > i; i++) {
        vote_btns[i].addEventListener('click', (e) => {
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project

            fetch(`http://127.0.0.1:8000/api/pyqt-projects/${project}/vote/`, {
                method:'POST',
                headers: {
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`
                },
                body:JSON.stringify({'value': vote})

            })
        })
    }
}

// add auth token
let form = document.getElementById('login-form')

if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault()

        let form_data = {
            'username': form.username.value,
            'password': form.password.value
        }

        fetch('http://127.0.0.1:8000/api/users/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(form_data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.access) {
                    localStorage.setItem('token', data.access)
                    form.submit()
                }
            })
    })
}

// delete token
let logout_button = document.getElementById('logout-button')

if (logout_button) {
    logout_button.addEventListener('click',(e) => {
        localStorage.removeItem('token')
    })
}

// delete message confirm
function confirm_delete(confirm_msg) {
    return confirm(confirm_msg)
}


// background music for text quest
let backgroundMusic = document.getElementById("background-music");

let savedTime = localStorage.getItem("background-music");
if (savedTime) {
  backgroundMusic.currentTime = savedTime;
}

backgroundMusic.addEventListener("pause", function () {
  localStorage.setItem("background-music", backgroundMusic.currentTime);
});

backgroundMusic.addEventListener("ended", function () {
  localStorage.removeItem("background-music");
});

window.addEventListener("beforeunload", function () {
  localStorage.setItem("background-music", backgroundMusic.currentTime);
});