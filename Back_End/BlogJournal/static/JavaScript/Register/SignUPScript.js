$(document).ready(function(){

    $("#SignForm").submit(function(event){
        if ( CheckData() == false )
            event.preventDefault();
    });
})

function CheckData(){
    Result = true;

    if ( CheckLength('#Name', Name_Len ) == false )
        Result = false;
    if ( CheckLength('#Email', Email_Len ) == false )
        Result = false;
    if ( CheckLength('#Password', Password_Len ) == false )
        Result = false;

    if ( CheckEmailPattern() == false )
        Result = false;
    if ( CheckPassword() == false )
    	Result = false;

    return Result;
}

function CheckEmail(){

    if ( CheckLength('#Email', Email_Len ) == false )
        return ;
    if ( CheckEmailPattern() == false )
        return ;
    isEmailFound();
}

function isEmailFound(){

    $.ajax({
        type : "POST",
        url : CheckPage,
        dataType : 'json',
        data : {
            E: $('#Email').val(),
            csrfmiddlewaretoken: Token
            },
        error: function (jqXHR, exception) {
            ErrorFunction('in Making Ajax Call',
                           'in CheckScript.js',
                           Ajax_Error, false)
        },
        success : function(Data){
            try{
                //Data = JSON.parse(Data);
                if ( Data['Result'] == 0 )
                    $('#Email').css('border-color','green');
                else
                    $('#Email').css('border-color','red');
            }
            catch(e){
                ErrorFunction('in Searching For Email',
                              'in CheckScript.js',
                              JSON_Error, false)
            }
        }
    });
}