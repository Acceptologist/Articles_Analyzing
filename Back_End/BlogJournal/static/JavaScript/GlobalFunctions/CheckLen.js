/*
	- info :
		javascript page    	=>  CheckLength.js
        init name   		=>  CheckLengthScript

	-The Scripts it Depends On (init Name) :
		JQueryScript
*/

function CheckLength(id, len){
    if ( $(id).val().length <= len && $(id).val().length != 0 )        
        return true;
    $(id).css('border-color','red');
    return false;
}

function CheckStringLength(string, Len){
	if ( string.length > Len || string.length == 0)
		return false;
	return true;
}