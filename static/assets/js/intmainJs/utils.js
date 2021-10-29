function CSRF_token_header(){
    const header =  "X-CSRFToken";
    return header;
}

function CSRF_token(){
    const token = Cookies.get('csrftoken');; //Using the js-cookies library
    return token;
}

