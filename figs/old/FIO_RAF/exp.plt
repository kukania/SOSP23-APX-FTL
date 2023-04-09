set terminal postscript color dashed eps size 5.2,1.0 enhanced font 'Helvetica,17' linewidth 1
set output 'exp.eps'

set style data histograms
set style histogram cluster gap 2
set style fill solid border -1
#set ylabel "RAF" offset 1.8,0 font "Helvetica, 20"
set yrange [0:2.5]
set xtics nomirror offset .45,.15
set ytics offset .5
set ytics 1
set grid y
#set key left Left reverse samplen 1 maxrows 6
#set key right
set key font "Helvetica,18"
set key out
#set key height 1
set key maxrow 1
#set key width -1
set key at 3,3.1
set key samplen 4
set ytics font "Helvetica,18"

set multiplot layout 1,2\
			margins 0.1,0.98,0.1,0.98 \
              spacing 0.08,0.08
set datafile separator ","

#set size 0.7,1
plot "./data/fio_seq" u ($2):xtic(1) ti "DFTL" lc rgb "#90EE90" ,\
	"" u ($3) ti "SFTL" lc rgb "#D2B48C",\
	"" u ($4) ti "" lc rgb "#D2691E",\
	"" u ($6) ti "" lc rgb "#8B0000",\

unset ylabel
set key at 2.5,3.1
plot "./data/fio_rand" u ($2):xtic(1) ti "" lc rgb "#90EE90" ,\
	"" u ($3) ti "" lc rgb "#D2B48C",\
	"" u ($4) ti "TPFTL" lc rgb "#D2691E",\
	"" u ($6) ti "ProbFTL" lc rgb "#8B0000",\

#set lmargin at screen 0.75
#plot "./data/workloade.csv" u 2:xtic(1) notitle lc rgb "#FAFAD2" ,\
#	"" u 3 notitle lc rgb "#90EE90" ,\
#	"" u 4 notitle lc rgb "#228B22" ,\
#	"" u 5 notitle lc rgb "black" ,\
#	"" u 6 notitle lc rgb "#D2691E" ,\
#	"" u 7 notitle lc rgb "#8B0000" ,\

