$files = get-childitem -recurse  $args[0] | where {$_.extension -eq ".stlx"}
foreach($f in $files){ 
    echo "$($f.FullName)" 
    $target = $f.DirectoryName +"\"+ $f.Basename + ".py"
    $gen = setlx2python "$($f.FullName)" 
    if($?){
        $gen | out-file -encoding utf8 "$target"
    }else{
        echo $gen
    }
    echo " "
}