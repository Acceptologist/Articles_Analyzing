/*
    - info :
        javascript page     =>  CheckNumberOrNot.js
        init name           =>  CheckNumberOrNotScript

    -The Scripts it Depends On (init Name) :
        JQueryScript
*/

function isNumber(id){
	if ( isNaN( $(id).val() ) == false )
		return true;
	$(id).css('border-color', 'red');
	return false;
}