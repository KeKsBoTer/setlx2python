$files = get-childitem -recurse  $args[0] | where {$_.extension -eq ".stlx"}
foreach($f in $files){ 
    echo "$($f.FullName)" 
    $basename = $f.Basename -replace "-","_"
    $target = $f.DirectoryName +"\"+ $basename + ".py"
    $gen = setlx2python "$($f.FullName)" 
    if($?){
        $gen | out-file -encoding utf8 "$target"
    }else{
        echo $gen
    }
    echo " "
}