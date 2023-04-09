set terminal postscript color eps dashed enhanced font 'Helvetica,20' linewidth 1
set output 'motivation_latency_trend.eps'
set size 4.0, 5.0

#set title "Samsung KV-SSD Sync Read Latency Trend"
set xlabel 'Time (microsecond)'
set ylabel 'CDF' offset 1
set xrange [100:10000]
#set yrange [0.85:0.9999]
set yrange [0.5:1.0]
set xtics 10
set zeroaxis
set grid
set key font ',25'
set key outside
set key samplen 1 maxcols 1
set key at 9000,0.6 
#set size 0.45,0.55
set logscale x 10

set style line 1 lc rgb "red" lw 5
set style line 2 lc rgb "dark-magenta" lw 5
set style line 3 lc rgb "dark-red" lw 5
set style line 6 lc rgb "violet" lw 5
set style line 5 lc rgb "plum" lw 5
set style line 4 lc rgb "dark-violet" lw 5
set style line 7 lc rgb "green" lw 5
set style line 8 lc rgb "seagreen" lw 5
set style line 9 lc rgb "dark-green" lw 5
set style line 10 lc rgb "blue" lw 5
set style line 11 lc rgb "navy" lw 5
set style line 12 lc rgb "royalblue" lw 5

set label "Hit" at 130,1.04
set arrow from 100,1.02 to 210,1.02 lw 4 heads
set arrow from 210,0.5 to 210,1.055 nohead dt 2 lw 4

set label "Clean Eviction" at 250,1.04
set arrow from 210,1.02 to 800,1.02 lw 4 heads
set arrow from 800,0.5 to 800,1.055 nohead dt 2 lw 4

set label "Dirty Eviction" at 840,1.04
set arrow from 800,1.02 to 2200,1.02 lw 4 heads
set arrow from 2200,0.5 to 2200,1.055 nohead dt 2 lw 4


set label "GC" at 4100,1.04
set arrow from 2200,1.02 to 10000,1.02 lw 4 heads


set datafile separator ","

#set title "YCSB-A (50:50), Default (zipfian)"
#set origin 0.0,5.0
set size 1.0,1.0
plot	"./data/mixed.dat" u 1:3 ti "RM-R" with l ls 1, \
	"./data/seqread.dat" u 1:3 ti "SR" with l ls 4, \
	"./data/page-seqread.dat" u 1:3 ti "PAGE" with l ls 10, \

#	"./data/page-mixed.dat" u 1:3 ti "PAGE-RM-R" with l ls 7, \
