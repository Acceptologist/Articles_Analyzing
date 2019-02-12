$(document).ready(function(){

	$('#Like').click(function(){
        SendAjax('Like', MakeLike_DisLikePage, 'ID=' + Post_id + '&Type=0', 1,
            'MakeLike');
	})

	$('#DisLike').click(function(){
        SendAjax('DisLike', MakeLike_DisLikePage, 'ID=' + Post_id + '&Type=1', 2,
            'MakeDisLike');
	})

	$('#SendComment').click(function(){
        if ( CheckLength('#Comment', Comment_Len) )
            SendAjax('Comment', MakeCommentPage,
                'ID=' + Post_id + '&Comment=' + $('#Comment').val(), 3,
                'MakeComment');
	})
})

function SendAjax(NotUserText, Page, Data, Type, ErrorFunction){
    if ( !isUser ){
        TriggerMessage(3500, 'red', '<p>Must Log in To '+NotUserText+'</p>');
        return ;
    }

    $.ajax({
        type : "POST",
        url : Page,
        data : Data + '&csrfmiddlewaretoken=' + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
            TriggerMessage(3500, 'red', '<p>Error Occurred</p>');
        },
        
        success : function(Data){
            console.log(Data);
            try{
                if ( Data['Result'] == 0 )
                    TriggerMessage(3500, 'red', '<p>' +Data['Data']+ '</p>');

                else if ( Data['Result'] == 1 ){
                    
                    if ( Type == 1 ){
                        TriggerMessage(3500, 'green', '<p>Liked</p>');
                        $('#Likes').text( parseInt($('#Likes').text()) + 1 );
                    }
                    else if ( Type == 2 ){
                        TriggerMessage(3500, 'green', '<p>DisLiked</p>');
                        $('#DisLikes').text( parseInt($('#DisLikes').text()) + 1 );
                    }
                    else{
                        date = new Date();
                        The_Comment_Date = date.getDate() + '/' + date.getMonth() 
                            + '/' + date.getFullYear() + '   ' + date.getHours() 
                            + ':' + date.getMinutes() + ':' + date.getSeconds();
                        TriggerMessage(3500, 'green', '<p>Commented</p>');
                        $( Data['Data'] ).appendTo('.Comments_Div');
                        $('#Comment').val('');
                        $('#Comments').text( parseInt($('#Comments').text()) + 1 );
                    }
                }

                else
                    SetError_Function('in Making '+NotUserText,
                        'in PostScript.js', 'in '+ErrorFunction+' Function',
                        Data['Error']['Error Type'], Data['Error']['Error Code'],
                        Data['Error']['Error Message'], true);
            }
            catch(e){
                SetError_Function('in Making '+NotUserText,
                    'in PostScript.js', 'in '+ErrorFunction+' Function',
                    'JSON Error', '1', 'Failed To Covert JSON', true);
            }
        }
    });
}