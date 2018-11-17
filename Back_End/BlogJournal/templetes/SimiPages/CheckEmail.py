from Python import init
"""
if ( $_SERVER["REQUEST_METHOD"] == "POST" && isset($_SERVER["HTTP_REFERER"]) 
	&& ( isset($_POST['N']) || isset($_POST['E']) ) ){
	
	include_once URL;
    if ( $URL_REFERER->GetURLPath() == -1 ){
        include_once ErrorPage;
        exit();
    }
    
    if ( $URL_REFERER->URLResult != SignUP && $URL_REFERER->URLResult != Sittings ){
        include_once UnAuthurithedUser;
        exit();
    }
}
else{
	include_once UnAuthurithedUser;
	exit();
}

include_once FILTERS;
include_once CheckUser;
include_once JSON;
// if Name is Set
if ( isset($_POST['N']) ){

	// Filter Name
	if ( ( $Result = $FILTER->FilterName($_POST['N']) )[1] != 'OK' ){// Function in FILTER.php
		
		if ( $JSON->MakeJsonCheck( $Result ) == -1 ){
			echo json_encode( $JSON->Error );
			exit();
		}
		echo $JSON->JSONResult;
		exit();
	}
	
	$GLOBALS['N'] = $FILTER->FILTER_Result;
	// Search For Name
	if ( $JSON->MakeJsonCheck( CheckUserName($GLOBALS['N']) ) == -1 ){
		echo json_encode( array('Result' => -1, 'Object' => $JSON->Error ) );
		exit();
	}

	echo $JSON->JSONResult; // CheckUserName Function in CheckUser.php
}
// if Email is Set
else{
	
	// Filter Email
	if ( ( $Result = $FILTER->FilterEmail($_POST['E']) )[1] != 'OK' ){
		
		if ( $JSON->MakeJsonCheck( $Result ) == -1 ){
			echo json_encode( array('Result' => -1, 'Object' => $JSON->Error ) );
			exit();
		}
		echo $JSON->JSONResult;
		exit();
	}

	$GLOBALS['E'] = $FILTER->FILTER_Result;
	// Search For Email
	if ( $JSON->MakeJsonCheck( CheckUserEmail($GLOBALS['E']) ) == -1 ){
		echo json_encode( $JSON->Error );
		exit();
	}
	echo $JSON->JSONResult; // CheckUserEmail Function in CheckUser.php
}
exit();
?>
"""