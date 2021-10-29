function loadJs(id, url = null, inlineScript = null, callback){
    let e = document.createElement('script');
    if (url)
        e.src = url;
    if (inlineScript)
        e.appendChild(document.createTextNode(inlineScript));
    e.type = 'text/javascript';
    e.id = id;
    e.defer = true;
    e.addEventListener('load', callback);
    document.getElementsByTagName('head')[0].appendChild(e);
}
loadJs("cookies-api","https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.2.1/js.cookie.min.js", null, function(){
    if (Cookies.get('name')) {
        var name = Cookies.get('name');
    }
})