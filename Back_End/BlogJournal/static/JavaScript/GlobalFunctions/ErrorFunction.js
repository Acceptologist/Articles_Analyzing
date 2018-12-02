/*
    - info :
        javascript page     =>  ErrorFunction.js
        init name           =>  ErrorFunctionScript

    -The Scripts it Depends On (init Name) :
        JQueryScript
        SetMessage
*/
function ErrorFunction(Process, Location, Error, CanShowMessage){
    console.log(
        'Error info :\n\n'+
        'Process : ' + Process + '\n'+
        'Error Location = ' + Location + '\n'+
        'Error Type = ' + Error['Type'] + '\n'+
        'Error API Code = ' + Error['API'] + '\n'+
        'Error Message = ' + Error['Message'] + '\n'
    );
    if ( CanShowMessage == true )
        TrigerMessage(5000, '#E30300',
            '<p>Error Message Code : ' + Error['API'] +
            '</p><p>Something Goes Wrong</p>');
}
