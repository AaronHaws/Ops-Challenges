$directory = "dir1", "dir2", "dir3", "dir4"

foreach ($directory in $directories){
>> mkdir $directory
>> echo hello > "$directory/hello.txt"
>> }
