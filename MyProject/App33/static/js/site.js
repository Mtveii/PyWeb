class Base64 {
    static #textEncoder = new TextEncoder();
    static #textDecoder = new TextDecoder();

    static encode = (str) => btoa(String.fromCharCode(...Base64.#textEncoder.encode(str)));
    static decode = (str) => Base64.#textDecoder.decode(Uint8Array.from(atob(str), c => c.charCodeAt(0)));
    
    static encodeUrl = (str) => this.encode(str).replace(/\+/g, '-').replace(/\//g, '_'); //.replace(/=+$/, '');
    static decodeUrl = (str) => this.decode(str.replace(/\-/g, '+').replace(/\_/g, '/'));

    static jwtEncodeBody = (header, payload) => this.encodeUrl(JSON.stringify(header)) + '.' + this.encodeUrl(JSON.stringify(payload));
    static jwtDecodePayload = (jwt) => JSON.parse(this.decodeUrl(jwt.split('.')[1]));
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Script works");
    let btn = document.getElementById("btn-seed");
    if(btn) { btn.addEventListener('click', btnSeedClick); }
    
    btn = document.getElementById("auth-modal-btn");
    if(btn) { btn.addEventListener('click', btnAuthModalClick); }
});

function btnAuthModalClick() {
    const loginInput = document.getElementById("auth-modal-login");
    if(!loginInput) throw "auth-modal-login input not found";
    const passwordInput = document.getElementById("auth-modal-password");
    if(!passwordInput) throw "auth-modal-password input not found";
    let isOk = true;
    const login = loginInput.value;
    if(!login || login.includes(':')) {
        loginInput.classList.add("is-invalid");
        isOk = false;
    }
    else {
        loginInput.classList.remove("is-invalid");
    }
    const password = passwordInput.value;
    if(!password || password.length < 3) {
        passwordInput.classList.add("is-invalid");
        isOk = false;
    }
    else {
        passwordInput.classList.remove("is-invalid");
    }
    if(isOk) {
        let userPass = login + ':' + password;
        let credentials = Base64.encode(userPass);
        fetch("/auth/", {
            headers: {
                "Authorization": "Basic " + credentials
            }
        }).then(
            //=============================HW==================================
            response => {
            const errorContainer = document.getElementById("auth-modal-error-container");
            errorContainer.innerHTML = ""; 
            
            if(response.ok) {
                response.text().then(accessId => {
                    console.log("Access ID:", accessId);
                    
                });
            } else {
                response.text().then(errorMessage => {
                    const alertDiv = document.createElement("div");
                    alertDiv.className = "alert alert-danger alert-dismissible fade show";
                    alertDiv.setAttribute("role", "alert");
                    alertDiv.innerHTML = `
                        <strong>Помилка автентифікації!</strong> ${errorMessage}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    `;
                    errorContainer.appendChild(alertDiv);
                });
            }
        }).catch(error => {
            const errorContainer = document.getElementById("auth-modal-error-container");
            const alertDiv = document.createElement("div");
            alertDiv.className = "alert alert-danger alert-dismissible fade show";
            alertDiv.setAttribute("role", "alert");
            alertDiv.innerHTML = `
                <strong>Помилка мережі!</strong> ${error}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            `;
            errorContainer.appendChild(alertDiv);
        });
        //=============================HW==================================
    }
}

function btnSeedClick() {
    if(confirm("Це вельми небезпечна дія. Підтверджуєте?")) {
        fetch("/seed/", {
            method: "PATCH"
        }).then(r => r.json())
        .then(j => {
            console.log(j);
        });
    }
}