/*
    - info :
        javascript page     =>  CheckPattern.js
        init name           =>  CheckPatternScript

    -The Scripts it Depends On (init Name) :
        JQueryScript

    - Data Needed :
        id  => #Email
*/

function CheckEmailPattern(){
    reg = /\S+@\S+\.\S+/;
    if ( reg.test( $('#Email').val() ) == true )
        return true;
    $('#Email').css('border-color','red');
    return false;
}