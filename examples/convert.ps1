$files = get-childitem -recurse  $args[0] | where {$_.extension -eq ".stlx"}
foreach($f in $files){ 
    echo "$($f.FullName)" 
    $basename = $f.Basename -replace "-","_"
    $target = $f.DirectoryName +"\"+ $basename + ".py"
    setlx2python "$($f.FullName)" -o "$target"
    echo " "
}