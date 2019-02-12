$(document).ready(function(){

    $("#LogForm").submit(function(event){
        Result = CheckLength('#Email', Email_Len);
        Result = CheckLength('#Password', Password_Len, Result);
        if ( CheckEmailPattern(Result) == false )
            event.preventDefault();
    });
})