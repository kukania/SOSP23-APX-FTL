set terminal postscript color dashed eps size 5.2,1.0 enhanced font 'Helvetica,17' linewidth 1
set output 'exp.eps'

set style data histograms
set style histogram cluster gap 2
set style fill solid border -1
#set ylabel "WAF" offset 1.8,0 font "Helvetica, 20"
set yrange [0:3.5]
set xtics nomirror offset .45,.15
set ytics offset .5
set ytics 1
set grid y
#set key left Left reverse samplen 1 maxrows 6
#set key right
set key font "Helvetica,22"
set key out
set key height 1
set key maxrow 1
set key at 8,4.6
#set key samplen 1
unset key
set ytics font "Helvetica,20"

set multiplot layout 1,2\
			margins 0.1,0.98,0.1,0.98 \
              spacing 0.08,0.08
set datafile separator ","

#set size 0.7,1

#set object 1 rect from 1.25,1.23 to 1.418,3.1 fc "#d60000" front
#set label 1 "Reblooming\n Overhead" at 1.6,2.6 font "Helvetica,14" front
#set arrow 1 from 1.6,2.3 to 1.418, 2.5
plot "./data/fio_seq" u ($2):xtic(1) ti "DFTL" lc rgb "#90EE90" ,\
	"" u ($3) ti "SFTL" lc rgb "#D2B48C",\
	"" u ($4) ti "TPFTL" lc rgb "#D2691E",\
	"" u ($6) ti "BloomFTL" lc rgb "#8B0000",\

unset object 1

unset ylabel
unset key
#unset label 1
#unset arrow 1
#set object 2 rect from 0.25,1.11 to 0.418, 2.59 fc "#d60000" front
#set object 3 rect from 1.25,1.18 to 1.418, 3.13 fc "#d60000" front
#set object 4 rect from 2.25,1.1 to 2.418, 2.49 fc "#d60000" front
plot "./data/fio_rand" u ($2):xtic(1) ti "DFTL" lc rgb "#90EE90" ,\
	"" u ($3) ti "SFTL" lc rgb "#D2B48C",\
	"" u ($4) ti "TPFTL" lc rgb "#D2691E",\
	"" u ($6) ti "BloomFTL" lc rgb "#8B0000",\
