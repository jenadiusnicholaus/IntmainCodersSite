
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


 class Thenable {
  constructor(num) {
    this.num = num;
  }
  then(resolve, reject) {
    setTimeout(() => resolve(this.num * 2), 1000); // (*)
  }
}


async function bookForClass(courseid,) {
//     preventDefault();
    let url =  "make_booking/";
    const request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.setRequestHeader( CSRF_token_header(),CSRF_token());
    const data = new FormData();
    data.append('id', courseid);

    // Send request
    request.send(data);
    request.onload = async () => {
        let loader = document.getElementById('spinner')
        loader.style.display = 'inherit'
        let result = await new Thenable(1);
        const received = await request.responseText;
        removedFirst = received.substring(1);
        removedLast = removedFirst.substring(0, removedFirst.length-1);

        // Parse to JS object
        const parsed = JSON.parse(received);
        console.log("Output of JSON.parse:");
        console.log(parsed);

        // Insert value into DOM

        document.getElementById('message').innerHTML = `
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
          <strong>Holy guacamole!</strong> ${parsed['messages']}.
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
       </div>` ;
        loader.style.display = 'none'

    };
}

// function getDayClasses(dayId) {
//     fetch('dayclasslist/').then(
//         function(response) {
//             if (response.status == 200) {
//               console.log(response)
//             }
//         }).catch(function(err) {
//         console.log('Fetch Error', err);
//     });
// }

function getDayClasses(dayId,)
{

        let _url =  "dayclasslist/";

        const request = new XMLHttpRequest();
        request.open('POST', _url,true);
        request.setRequestHeader( CSRF_token_header(),CSRF_token());
        // request.setRequestHeader("Content-type", "application/json");
        const data = new FormData();
        data.append('id', dayId);

      request.send(data);
  request.onload = async () =>
  {
    const loader = document.getElementById('listspinner')
    loader.style.display = 'inherit'
    let result = await new Thenable(1);
    const received = request.responseText;
    // console.log(received);
    // removedFirst = received.substring(1);
    // removedLast = removedFirst.substring(0, removedFirst.length-1);
    //
    const parsedJson = JSON.parse(received);
    // console.log(parsedJson)
    console.log(parsedJson)

    parsedJson.forEach((data) =>
    {
      console.log(data.scheduling_time)
    })

    let elementItemSet = document.querySelector('.schedule-listing');
    elementItemSet.innerHTML = '';
    let newList = '';

    for (let i = 0; i <= parsedJson.length; i++)
    {
      let classList = parsedJson[i]
      if (classList != undefined)
      {
        let scheduling_time = classList.scheduling_time
        let courseDesc = classList.course.desc;
        let coursetitle = classList.course.title
        let course_instructor = classList.course_instructor.name
        let imageurl = classList.course_instructor.profile
        newList += `<div class="schedule-item" style="background-size: cover;">
           <div class="sc-time" style="background-size: cover;">${scheduling_time}</div>
              <div class="sc-pic" style="background-size: cover;">
                <img  src="http://animal.discovery.com/mammals/cheetah/pictures/cheetah-picture.jpg" class="img-circle" alt="">
              </div>
              <div class="sc-name" style="background-size: cover;">
              <h4>${course_instructor}</h4>
              <span>Founder &amp; CEO</span>
              <button style="color: white" onclick="bookForClass(${classList.class_id})" class="btn btn-outline-primary">
              <span id="spinner" style="display: none; color: white" class="spinner-border spinner-border-sm"></span>
              <b>Book now</b>
              </button>
              </div>
              <div class="sc-info" style="background-size: cover;">
              <h3>${coursetitle}</h3>
              <p>${courseDesc}</p>
            </div>
              <div class="clearfix" style="background-size: cover;"></div>
        </div>` ;
      }


    }
    elementItemSet.innerHTML += newList;
  }
}







