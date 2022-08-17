<?php
function anagrama($a,$b){
    $cont = 0;
    $igual = 0;
    if(strlen($a)==strlen($b) and $a != $b){
        $lstA = sort(str_split($a));
        $lstB = sort(str_split($b));
        foreach($lstA as $i){
            if($i == $lstB[$cont]){
                $igual +=1;
            }
            $cont +=1;
        }
    }
    return (strlen($a) == $igual and strlen($b)== $igual);
};
echo (anagrama("alan","lana"));
?>