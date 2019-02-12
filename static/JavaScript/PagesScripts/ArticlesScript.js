function GetMorePosts(){
    $.ajax({
        type : "POST",
        url : GetPostsPage,
        data : 'Number=' + Posts_Number + '&csrfmiddlewaretoken=' + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
        },
        
        success : function(Data){
        	console.log(Data);
            try{
                if ( Data['Result'] == 0 )
                	$('.Show_More_Div').fadeOut(500);
                else if ( Data['Result'] == 1 ){
                	Count = 0;
                	for (i=1; i<=Data['Data']['Count']; i++, Count++){
                		$(Data['Data']['Posts'][i]).insertBefore('.Show_More_Div');
                		Posts_Number++;
                	}
                	if ( Count != 5 )
                		$('.Show_More_Div').fadeOut(500);
                }
                else
                    TriggerMessage(3500, 'red', '<p>Error Occurred</p>');
            }
            catch(e){
                SetError_Function('in Searching For More Posts',
                    'in ArticleScript.js', 'in GetMorePosts Function', 'JSON Error',
                    '1', 'Failed To Covert JSON', false);
            }
        }
    });
}