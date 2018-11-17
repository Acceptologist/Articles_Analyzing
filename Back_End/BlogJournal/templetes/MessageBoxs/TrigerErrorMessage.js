SetMessage(5000, '#E30300' , 
    "<p>Error Meaasege Code : <?php echo $Result[1]['Error Code'];?>"
    +"</p><p>Something Goes Wrong</p>'");

console.log("<?php"+
    "echo 'Proccess : '.$Result[2].'\n';"+
    "echo 'Error Location info :in '.$Result[3].'\n';"+
    "echo 'Error Location = '.$Result[1]['Error Location'].'\n';"+
    "echo 'Error Code = '.$Result[1]['Error Code'].'\n';"+
    "echo 'Error Message = '.$Result[1]['Error Message'].'\n';"+
    "?>");