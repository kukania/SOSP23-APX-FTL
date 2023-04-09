set terminal eps color dashed size 4.7,1.8 enhanced font 'Helvetica,14' linewidth 1
set output 'throughput_2x.eps'

set style data histograms
set style histogram cluster gap 1
set style fill solid border -1
set ylabel "WAF" font ',14' offset 2,0
set yrange [0:15]
set xtics font ",14"
set ytics 2
#set xtics font ",15" offset -0.3,.2 rotate by -30
set ytics font ",14" offset 0.5,0
set grid y
set key
set key out
set key maxrow 1
set key  at 5,17.5

set multiplot layout 1,2

#set datafile separator ","

plot	"./merge/res_2x"	u 2:xtic(1)	lc rgb "#8B0000" ti "DFTL" ,\
		"./merge/res_2x"	u 4:xtic(1) lc rgb "#666666" ti "BloomFTL"

set style data histograms
set style histogram cluster gap 1
set style fill solid border -1
set yrange [0:2]
set ytics 0.5
unset key
set ylabel "RAF" font ',14' offset 2,0
plot	"./merge/res_2x"	u 3:xtic(1)	lc rgb "#8B0000" ti "DFTL" ,\
		"./merge/res_2x"	u 5:xtic(1) lc rgb "#666666" ti "BloomFTL"
