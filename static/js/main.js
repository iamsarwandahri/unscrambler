$(document).ready(function(){

$('#submitBtn').on('click', function (){
    input = $('#scrambledWordInput').val()

    $.ajax({
        type: "POST",
        url: "/search/",
        data: JSON.stringify({'input': input}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
        success: function (data) {

            // $('.container2').show()
            $('.container2').remove('')

            if(Array.isArray(data['list'])){
                for(l of data['list']){
                    if(l.length>0){
                        len = l[0].length
    
                    $('body').append(`<div id="container`+len+`" class="container2" style="display: block;">
                    <strong>`+len+` Letter words</strong>
                    <p id="item1">`+l.join(', ')+`</p></div>`);
                    }
                }
            }

            else{
                $('body').append(`<div id="container1" class="container2" style="display: block;">
                    <strong>`+data['list']+`</strong></div>`);

            }

        }
    });
})

})
