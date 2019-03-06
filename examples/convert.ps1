$files = get-childitem -recurse  $args[0] | where {$_.extension -eq ".stlx"}
foreach($f in $files){ 
    echo $f.Name
    $path = ($f.FullName).split('\.')
    $target = echo (($path[0..($path.Count-2)] -Join "\")+".py")
    $gen = setlx2python "$($f.FullName)" 
    if($?){
        $gen| out-file -encoding utf8 "$target"
    }else{
        echo $gen
    }
    echo " "
}