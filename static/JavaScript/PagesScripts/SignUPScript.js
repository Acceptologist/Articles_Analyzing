$(document).ready(function(){
    $("#SignForm").submit(function(event){
        if ( CheckData() == false )
            event.preventDefault();
    });
})

function CheckData(){
    Result = CheckLength('#Name', Name_Len);
    Result = CheckLength('#Email', Email_Len, Result);
    Result = CheckLength('#Password', Password_Len, Result);
    Result = CheckEmailPattern(Result);
    return CheckPassword(Result);
}

function CheckEmail(){
    
    if ( $('#Email').val().length == 0 ){
        $('#Email').css('border-color', '#FFF');
        return ;
    }
    else if ( $('#Email').val().length > Email_Len ){
        $('#Email').css('border-color', 'red');
        return ;
    }

    $.ajax({
        type : "POST",
        url : CheckEmailPage,
        data : 'Email=' + $('#Email').val() + '&csrfmiddlewaretoken=' + Token,
        error: function (jqXHR, exception) {
            console.log(jqXHR);
        },
        
        success : function(Data){
            try{
                if ( Data['Result'] == 0 )
                    $('#Email').css('border-color','green');
                else if ( Data['Result'] == 1 )
                    $('#Email').css('border-color','red');
            }
            catch(e){
                SetError_Function('in Searching For Email Reservied Or Not',
                    'in SignUPScript.js', 'in CheckEmail Function', 'JSON Error',
                    '1', 'Failed To Covert JSON', false);
            }    
        }
    });
}