set terminal eps color dashed size 7.0,2.7 enhanced font 'Helvetica'
set output 'superblock_gc.eps'
set margin 9,4.25,4,1
set xlabel 'Over-provisioning Ratio' font "Helvetica,22" offset 0,-0.5
set ylabel 'WAF' font "Helvetica,22" offset -0.0,0
set xrange [0:0.25]
set yrange [0:25]
set xtics 0.05
set ytics 5
set tics font "Helvetica,25"
set zeroaxis
set grid
set key right top samplen 8 spacing 0.65 font ",23"
set size 1,1

plot "./data/input.data" u 1:7 t "Page-level FTL  " smooth csplines lw 6,\
	"./data/input.data" u 1:2 t "# of blocks per SB = 1  " smooth csplines lw 6, \
	"./data/input.data" u 1:3 t " = 2  " smooth csplines lw 6, \
	"./data/input.data" u 1:4 t " = 4  " smooth csplines lw 6, \
	"./data/input.data" u 1:5 t " = 8  " smooth csplines lw 6, \
	"./data/input.data" u 1:6 t " = 16" smooth csplines lw 6
