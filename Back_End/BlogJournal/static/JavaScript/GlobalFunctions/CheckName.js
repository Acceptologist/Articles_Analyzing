/*
    - info :
        javascript page     =>  CheckName.js
        init name           =>  CheckNameScript

    -The Scripts it Depends On (init Name) :
        JQueryScript
        SetMessageBoxScript

    - Data Needed :
        id  => #Name
        var => Name_Len
        var => CheckPage
*/

function CheckName(){

    if ( $('#Name').val().length == 0 || $('#Name').val().length > Name_Len )
        return ;

    $.ajax({
        type : "POST",
        url : CheckPage,
        data : 'N='+$('#Name').val(),
        error: function (jqXHR, exception) {
            console.log(jqXHR);
            return false;
        },
        
        success : function(Data){
            try{
                Data = JSON.parse(Data);
                if ( Data['Result'] == 0 ){
                    
                    if ( Data['Object'] == 'Empty' || Data['Object'] == 'Too Long' )
                        $('#Name').css('border-color','red');
                    
                    else if ( Data['Object'] == 'Found In Users' 
                        || Data['Object'] == 'Found In Waiting_Users')
                        $('#Name').css('border-color','red');
                    else{
                        $('#Name').css('border-color','green');
                        return true;
                    }
                }
                else{
                    SetMessage(5000, '#E30300',
                        '<p>Error Meaasege Code : '+Data['Object']['Error Code']+
                        '</p><p>Something Goes Wrong</p>');
                    
                    console.log(
                        'Error info :'+'\n'+
                        'Proccess : in Searching For Name'+'\n\n'+
                        'Error Location = '+Data['Object']['Error Location']+'\n'+
                        'Error Code = '+Data['Object']['Error Code']+'\n'+
                        'Error Message = '+Data['Object']['Error Message']+'\n'
                        );
                }
            }
            catch(e){
                console.log(
                    'Error info :'+'\n'+
                    'Proccess : in Searching For Name'+'\n\n'+
                    'Error Location = in CheckScript.js \n'+
                    'Error API Code = 11\n'+
                    'Error Message = Failed To Covert JSON \n'
                    );
            }    
        }
    });
    return false;
}