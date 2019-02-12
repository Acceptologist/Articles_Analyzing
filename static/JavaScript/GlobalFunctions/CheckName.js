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

    if ( $('#Name').val().length == 0 ){
        $('#Name').css('border-color', '#FFF');
        return ;
    }
    else if ( $('#Name').val().length > Name_Len ){
        $('#Name').css('border-color', 'red');
        return ;
    }

    $.ajax({
        type : "POST",
        url : CheckNamePage,
        data : 'Name=' + $('#Name').val() + '&csrfmiddlewaretoken=' + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
        },
        
        success : function(Data){
            try{
                if ( Data['Result'] == 0 )
                    $('#Name').css('border-color','green');
                else if ( Data['Result'] == 1 )
                    $('#Name').css('border-color','red');
            }
            catch(e){
                SetError_Function('in Searching For Name Reservied Or Not',
                    'in CheckNameScript.js', 'in CheckName Function', 'JSON Error',
                    '1', 'Failed To Covert JSON', false);
            }    
        }
    });
}