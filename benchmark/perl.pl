$count=10000;
$z=0;

# 10000
# start time 1515130547
# end time 1515130568
# 100000000
# cost: 21

$start = time();
printf("start time %d\n", $start);

for ($x=0;$x < $count; $x=$x +1) {
    for ($y=0;$y < $count; $y = $y +1) {
        $z = $z + 1;
    }
}
$end = time();
printf("end time %d\n", $end);

print "$z\n";
$cost = $end - $start;
print "cost: $cost s\n";
