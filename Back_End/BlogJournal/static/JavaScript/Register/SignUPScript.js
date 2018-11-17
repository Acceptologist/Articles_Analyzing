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
    if ( $('#Email').val().length==0 || $('#Email').val().length>Email_Len )
        return ;
    //isEmailFound();
}

function isEmailFound(){

    $.ajax({
        type : "POST",
        url : CheckPage,
        data : 'E='+$('#Email').val(),
        error: function (jqXHR, exception) {
            console.log(jqXHR);
            return false;
        },

        success : function(Data){
            try{
                Data = JSON.parse(Data);
                if ( Data['Result'] == 0 ){

                    if ( Data['Object'] == 'Empty' || Data['Object'] == 'Too Long' )
                        $('#Email').css('border-color','red');

                    else if ( Data['Object'] == 'Found In Users'
                        || Data['Object'] == 'Found In Waiting_Users')
                        $('#Email').css('border-color','red');
                    else{
                        $('#Email').css('border-color','green');
                        return true;
                    }
                }
                else{
                    SetMessage(5000, '#E30300', MyPage ,
                        '<p>Error Meaasege Code : '+Data['Object']['Error Code']+
                        '</p><p>Something Goes Wrong</p>');

                    console.log(
                        'Error info :'+'\n'+
                        'Proccess : in Searching For Email'+'\n\n'+
                        'Error Location = '+Data['Object']['Error Location']+'\n'+
                        'Error Code = '+Data['Object']['Error Code']+'\n'+
                        'Error Message = '+Data['Object']['Error Message']+'\n'
                        );
                }
            }
            catch(e){
                console.log(
                    'Error info :'+'\n'+
                    'Proccess : in Searching For Email'+'\n\n'+
                    'Error Location = in CheckScript.js \n'+
                    'Error API Code = 10\n'+
                    'Error Message = Failed To Convert Data \n'
                    );
            }
        }
    });
    return false;
}