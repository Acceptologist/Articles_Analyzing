function CheckinputLenAndNumber(The_Object, Len){
    Result = CheckLength('#'+The_Object.id, Len);
    Result1 = isNumber('#'+The_Object.id);
    if ( Result == true && Result1 == true )
        $('#'+The_Object.id).css('border-color', '#645A60');
}