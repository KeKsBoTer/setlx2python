$files = get-childitem $args[0] | where {$_.extension -eq ".stlx"}
foreach($f in $files){ 
    echo $f.Name
    $target = echo ((($f.FullName).split('\.')[0..6] -Join "\")+".py")
    $gen = setlx2python "$($f.FullName)" 
    if($?){
        $gen| out-file -encoding utf8 "$target"
    }else{
        echo $gen
    }
    echo " "
}