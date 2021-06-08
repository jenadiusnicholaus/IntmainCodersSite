//  Referece
// https://javascript.info/async-await

 class Thenable {
  constructor(num) {
    this.num = num;
  }
  then(resolve, reject) {
    setTimeout(() => resolve(this.num * 2), 1000); // (*)
  }
}

async function bookForClass(courseid){

    // Open request to get menuitem
    const request = new XMLHttpRequest();
    request.open('POST', '/bookforclass/');

    // Include csrf token in header so Django will accept the request
    const header =  "X-CSRFToken";
    const token = Cookies.get('csrftoken'); //Using the js-cookies library
    request.setRequestHeader(header, token);

    // Formdata object to structure data as if submitted from a form
    const data = new FormData();
    data.append('id', courseid);

    // Send request
    request.send(data);

    //Once request is received parse it and insert result in DOM
    request.onload = async () => {

        const loader = document.getElementById("spinner"+courseid)
        loader.style.display = 'inherit'

        let result = await new Thenable(1);
        // alert(result);
        const received = await request.responseText;
        console.log("Data as received:  " + received);

        // Remove [] from response text
        removedfirst = received.substring(1);
        removedlast = removedfirst.substring(0, removedfirst.length-1);
        console.log("Data with [] removed: " + removedlast);

        // Parse to JS object
        const parsed = JSON.parse(received);
        console.log("Output of JSON.parse:");
        console.log(parsed);

        // Insert value into DOM

        document.getElementById('message').innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert">
                                                              <strong>Holy guacamole!</strong> ${parsed['messages']}.
                                                              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>` ;
        loader.style.display = 'none'

    };
}




