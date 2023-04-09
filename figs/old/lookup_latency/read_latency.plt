set terminal eps color dashed size 5.3,1.6 enhanced font 'Helvetica,16' linewidth 1
set output 'read_latency.eps'

set style data histograms
set style histogram cluster gap 1
set style fill solid border -1
set ylabel "Latency ({/Symbol m}s)" font ',14' offset 2,0
set yrange [0:110]
set xtics font ",14"
set xtics font ",17"
set ytics font ",14" offset 0.5,0
set ytics 20
set grid y
set xtics scale 0
unset key

set datafile separator ","

plot	"./data/read_latency.csv"	u 2:xtic(1)	lc rgb "#8B0000" ,\
	""  using 0:($2+7.8):(sprintf("%g",$2)) with labels notitle font ",14"
