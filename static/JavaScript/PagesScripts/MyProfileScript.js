function MakeSlide(id){
    $("#DropDownBox"+id).toggle("slide");
}

function Edit(id){
    location.href = EditPostPage+id;
}

function Delete(id){
    if ( confirm('Do You Sure Want To Delete This Post') == true )
        DeletePost(id);

}

function DeletePost(id, Post_Number){
	
	$.ajax({
        type : "POST",
        url : DeletePostPage,
        data : 'Number=' + id + '&csrfmiddlewaretoken=' + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
            TriggerMessage(3500, 'red', '<p>Error Occurred</p>');
        },
        
        success : function(Data){
            console.log(Data);
            try{
                if ( Data['Result'] == 0 )
                    TriggerMessage(3500, '#E30300', '<p>Post Not Found</p>');

         		else if ( Data['Result'] == 1 ){
         			TriggerMessage(4000, '#53A01A','<p>Deleted</p>');
         			$('#Post' + id).remove();
         			Posts = parseInt($('#Posts_Number').text());
         			$('#Posts_Number').text( Posts -1 );
         			$('.Number').text(Posts - 1);
         		}

                else
                    SetError_Function('in Deleting User Post',
                        'in MyProfileScript.js', 'in DeletePost Function',
                        Data['Error']['Error Type'], Data['Error']['Error Code'],
                        Data['Error']['Error Message'], true);
            }
            catch(e){
                SetError_Function('in Deleting User Post',
                    'in MyProfileScript.js', 'in DeletePost Function', 'JSON Error',
                    '1', 'Failed To Covert JSON', true);
            }
        }
    });
}