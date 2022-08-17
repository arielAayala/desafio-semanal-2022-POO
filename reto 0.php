<?php
$num = 1;
while($num <=100 ){
    if($num % 3== 0 and $num % 5==0){
        echo("fizzbuzz ");
    }elseif($num % 3==0){
        echo("fizz");
    }elseif($num % 5==0){
        echo("buzz");
    }else{
        echo($num);
    }
    echo(" - ");
    $num +=1;
}?>