<?php
$cont = 0;
$num = [];
while($cont < 50){
    if($cont <=1){
        echo($cont);
        array_push($num,$cont);
    }else{
        $suma = $num[cont-1] + $num[cont-2];
        array_push($num,$suma);
        echo($suma);
    }
    $cont+=1;
    echo(" - ");
}
?>