$(document).ready(function(){

$('#submitBtn').on('click', function (){
    input = $('#scrambledWordInput').val()
    console.log('Input', input)

    $.ajax({
        type: "POST",
        url: "/search/",
        data: JSON.stringify({'input': input}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
        success: function (data) {
            console.log('Data', data)

            $('.container2').show()

            $('#item1').html('')
            $('.container2').remove('')


            for(l of data['list']){
                console.log(l)
                if(l.length>0){
                    len = l[0].length

                $('body').append(`<div id="container`+len+`" class="container2" style="display: block;">
                <strong>`+len+` Letter words</strong>
                <p id="item1">`+l.join(', ')+`</p></div>`);
                }
            }

            words = data['list']

            var words = 
            $('#item1').html(words)

        }
    });
})

})
