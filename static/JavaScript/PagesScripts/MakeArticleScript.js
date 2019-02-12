$(document).ready(function(){

	$("#ArticleForm").submit(function(event){
		Result = CheckLength('#Title', ArticleTitle_Len);
		Result = CheckLength('#Tags', ArticleTags_Len, Result, true);
		if ( CheckLength('#Article', Article_Len, Result) == false )
            event.preventDefault();
    });
})