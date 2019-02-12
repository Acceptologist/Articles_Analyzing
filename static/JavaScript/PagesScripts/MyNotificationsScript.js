function GetMoreNotifications(){
	
	$.ajax({
        type : "POST",
        url : GetNotificationsPage,
        data : 'Number=' + Notifications_Number + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
            TriggerMessage(3500, 'red', '<p>Error Occurred</p>');
        },
        
        success : function(Data){
        	console.log(Data);
            try{
                if ( Data['Result'] == 0 )
                	$('.Show_More_Div').fadeOut(500);
                
                else if ( Data['Result'] == 1 ){
                	Count = 0;
                	for (i=1; i<=Data['Data']['Count']; i++, Count++){
                		$(Data['Data']['Notifications'][i])
                					.appendTo('.Notifications');
                		Notifications_Number++;
                	}
                	if ( Count != 7 )
                		$('.Show_More_Div').fadeOut(500);
                }
                
                else
                    TriggerMessage(3500, 'red', '<p>Error Occurred</p>');
            }
            catch(e){
                SetError_Function('in Searching For More Notifications',
                    'in ArticleScript.js', 'in GetMoreNotifications Function',
                    'JSON Error', '1', 'Failed To Covert JSON', false);
            }
        }
    })
}