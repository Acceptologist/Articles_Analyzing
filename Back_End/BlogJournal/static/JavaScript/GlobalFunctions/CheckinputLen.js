/*
	- info :
		javascript page    	=>  CheckinputLen.js
        init name   		=>  CheckinputLenScript

	-The Scripts it Depends On (init Name) :
		JQueryScript
		CheckLenScript
*/

// Functions For input 
function CheckinputLen(The_Object, Len){
    if ( $('#'+The_Object.id).val().length == 0 )
        $('#'+The_Object.id).css('border-color', '#666866');
    else if ( CheckLength('#'+The_Object.id, Len) == true )
        $('#'+The_Object.id).css('border-color', '#645A60');
}