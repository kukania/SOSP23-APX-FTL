!!! posix memory ASYNC: 1!!!

 |---------- algorithm_log : Demand FTL
 | Total Blocks(Segments): 8192
 |  -Translation Blocks:   8 (+1 reserved)
 |  -Data Blocks:          8182 (+1 reserved)
 | Total Pages:            4194304
 |  -Translation Pages:    4096
 |  -Data Pages            4189184
 |  -Page per Block:       512
 | Total Logical Pages:    16777216
 | Total cache entries:    4096
 |  -Mixed Cache entries:  1085
 |  -Cache Percentage:     26.489%
 | Write buffer size:      512
 |
 | ! Assume no Shadow buffer
 | ! PPAs are prefetched on write flush stage
 |---------- algorithm_log END

BM_Init() End!
_nos:8192
bench:524288
range : 15679641
bench range:0 ~ 15679641
bench range:0 ~ 15679641
15313 X 1024 = 15680512, answer=15679640
making seq Set bench!



30625 X 1024 = 31360000, answer=31359282
making rand Set and Get bench!
last set:1023


req_cnt_test:cnt -> 47038922:0 fuck
bench finish
bench free


a_type	l_type	max	min	avg	cnt	percentage
--------------------------------------------
|            bench type:                   |
--------------------------------------------
----algorithm----
[0~100(usec)]: 0
[100~200(usec)]: 0
[200~300(usec)]: 0
[300~400(usec)]: 0
[400~500(usec)]: 0
[500~600(usec)]: 0
[600~700(usec)]: 0
[700~800(usec)]: 0
[800~900(usec)]: 0
[900~1000(usec)]: 0
[over_ms]: 0
[over__s]: 0
----lower----
[0~100(usec)]: 0
[100~200(usec)]: 0
[200~300(usec)]: 0
[300~400(usec)]: 0
[400~500(usec)]: 0
[500~600(usec)]: 0
[600~700(usec)]: 0
[700~800(usec)]: 0
[800~900(usec)]: 0
[900~1000(usec)]: 0
[over_ms]: 0
[over__s]: 0
----average----
[avg_algo]: 0.0
[avg_low]: 0.0
-----lower_info----
[write_op]: 0
[read_op]: 0
[trim_op]:0
[WAF, RAF]: 0.000000, 0.000000
[if rw test]: 0.000000(WAF), 0.000000(RAF)
[all write Time]:0.0
[all read Time]:0.0

----summary----
[all_time]: 74.156551
[size]: 244994.375000(mb)
[FAIL NUM] 0
[SUCCESS RATIO] 1.000000
[throughput] 3383035.438096(kb/s)
             3303.745545(mb/s)
[READ WRITE CNT] 0 15679640
error cnt:0



[cdf]read---
0	165	0.000011
10	2167	0.000149
20	5138	0.000476
30	6377	0.000883
40	5543	0.001237
50	4128	0.001500
60	3253	0.001707
70	2501	0.001867
80	2021	0.001996
90	1518	0.002093
100	1252	0.002172
110	1049	0.002239
120	913	0.002298
130	834	0.002351
140	836	0.002404
150	825	0.002457
160	765	0.002505
170	727	0.002552
180	705	0.002597
190	638	0.002637
200	566	0.002674
210	617	0.002713
220	536	0.002747
230	576	0.002784
240	560	0.002820
250	577	0.002856
260	615	0.002896
270	582	0.002933
280	607	0.002971
290	642	0.003012
300	591	0.003050
310	610	0.003089
320	729	0.003135
330	738	0.003183
340	1098	0.003253
350	2727	0.003426
360	7372	0.003897
370	18817	0.005097
380	40154	0.007658
390	75104	0.012448
400	122714	0.020274
410	178931	0.031686
420	239876	0.046984
430	297098	0.065932
440	344326	0.087892
450	373400	0.111707
460	386888	0.136381
470	376948	0.160422
480	354270	0.183016
490	315515	0.203139
500	271694	0.220466
510	224460	0.234782
520	179421	0.246225
530	137921	0.255021
540	102557	0.261562
550	73423	0.266244
560	51127	0.269505
570	35294	0.271756
580	24194	0.273299
590	17330	0.274404
600	12376	0.275194
610	9518	0.275801
620	7526	0.276281
630	6625	0.276703
640	6017	0.277087
650	5633	0.277446
660	5325	0.277786
670	5347	0.278127
680	5033	0.278448
690	5239	0.278782
700	5306	0.279120
710	5316	0.279459
720	5543	0.279813
730	5602	0.280170
740	5885	0.280545
750	6359	0.280951
760	7896	0.281455
770	10324	0.282113
780	14333	0.283027
790	20952	0.284363
800	31856	0.286395
810	49028	0.289522
820	73338	0.294199
830	107762	0.301072
840	157786	0.311135
850	220328	0.325187
860	295049	0.344004
870	380247	0.368255
880	477174	0.398688
890	574434	0.435324
900	664719	0.477717
910	741929	0.525035
920	796611	0.575841
930	831187	0.628851
940	833971	0.682039
950	810431	0.733726
960	757009	0.782006
970	683221	0.825580
980	597647	0.863696
990	503319	0.895796
1000	409149	0.921890
1010	322599	0.942465
1020	246540	0.958188
1030	185660	0.970029
1040	134912	0.978633
1050	96020	0.984757
1060	66538	0.989001
1070	46366	0.991958
1080	30674	0.993914
1090	20902	0.995247
1100	14647	0.996181
1110	10404	0.996845
1120	8042	0.997358
1130	6522	0.997774
1140	5195	0.998105
1150	4249	0.998376
1160	3275	0.998585
1170	2764	0.998761
1180	2265	0.998906
1190	1680	0.999013
1200	1423	0.999104
1210	1202	0.999180
1220	1019	0.999245
1230	815	0.999297
1240	649	0.999339
1250	622	0.999378
1260	528	0.999412
1270	474	0.999442
1280	457	0.999471
1290	497	0.999503
1300	438	0.999531
1310	397	0.999556
1320	333	0.999578
1330	279	0.999595
1340	275	0.999613
1350	307	0.999633
1360	287	0.999651
1370	262	0.999668
1380	189	0.999680
1390	180	0.999691
1400	205	0.999704
1410	181	0.999716
1420	185	0.999727
1430	160	0.999738
1440	187	0.999750
1450	149	0.999759
1460	177	0.999770
1470	160	0.999781
1480	171	0.999792
1490	129	0.999800
1500	109	0.999807
1510	80	0.999812
1520	91	0.999818
1530	76	0.999822
1540	72	0.999827
1550	67	0.999831
1560	103	0.999838
1570	116	0.999845
1580	118	0.999853
1590	115	0.999860
1600	66	0.999864
1610	56	0.999868
1620	37	0.999870
1630	44	0.999873
1640	42	0.999876
1650	42	0.999878
1660	34	0.999881
1670	39	0.999883
1680	29	0.999885
1690	15	0.999886
1700	14	0.999887
1710	13	0.999888
1720	14	0.999889
1730	7	0.999889
1740	8	0.999889
1750	8	0.999890
1760	1	0.999890
1770	1	0.999890
1790	3	0.999890
1800	3	0.999891
1810	1	0.999891
1820	5	0.999891
1830	15	0.999892
1840	17	0.999893
1850	13	0.999894
1860	8	0.999894
1870	5	0.999895
1880	5	0.999895
1890	3	0.999895
1900	3	0.999895
1910	3	0.999895
1920	5	0.999896
1930	5	0.999896
1940	6	0.999896
1950	11	0.999897
1960	11	0.999898
1970	4	0.999898
1980	1	0.999898
1990	5	0.999899
2000	12	0.999899
2010	17	0.999900
2020	9	0.999901
2030	8	0.999901
2040	2	0.999902
2200	2	0.999902
2210	1	0.999902
2220	1	0.999902
2230	1	0.999902
2240	1	0.999902
2250	5	0.999902
2260	2	0.999902
2270	3	0.999903
2280	11	0.999903
2310	2	0.999903
2370	3	0.999904
2380	3	0.999904
2390	2	0.999904
2410	1	0.999904
2430	2	0.999904
2460	2	0.999904
2470	1	0.999904
2480	1	0.999904
2490	2	0.999905
2500	1	0.999905
2510	6	0.999905
2520	2	0.999905
2530	5	0.999905
2540	2	0.999906
2550	1	0.999906
2570	3	0.999906
2580	1	0.999906
2590	4	0.999906
2600	1	0.999906
2610	3	0.999906
2620	3	0.999907
2630	15	0.999907
2640	6	0.999908
2650	5	0.999908
2660	9	0.999909
2670	16	0.999910
2680	16	0.999911
2690	10	0.999911
2700	7	0.999912
2710	8	0.999912
2720	17	0.999914
2730	16	0.999915
2740	26	0.999916
2750	23	0.999918
2760	32	0.999920
2770	27	0.999921
2780	23	0.999923
2790	12	0.999924
2800	19	0.999925
2810	29	0.999927
2820	24	0.999928
2830	13	0.999929
2840	16	0.999930
2850	11	0.999931
2860	12	0.999932
2870	9	0.999932
2880	14	0.999933
2890	12	0.999934
2900	6	0.999934
2910	12	0.999935
2920	14	0.999936
2930	13	0.999937
2940	15	0.999938
2950	14	0.999939
2960	19	0.999940
2970	14	0.999941
2980	9	0.999941
2990	7	0.999942
3000	15	0.999943
3010	16	0.999944
3020	3	0.999944
3030	3	0.999944
3040	5	0.999944
3050	5	0.999945
3060	3	0.999945
3070	1	0.999945
3080	6	0.999945
3090	4	0.999946
3100	3	0.999946
3110	3	0.999946
3120	8	0.999946
3130	1	0.999946
3140	5	0.999947
3150	12	0.999948
3160	6	0.999948
3170	3	0.999948
3180	8	0.999949
3190	7	0.999949
3200	9	0.999950
3210	9	0.999950
3220	15	0.999951
3230	23	0.999953
3240	10	0.999953
3250	10	0.999954
3260	12	0.999955
3270	17	0.999956
3280	16	0.999957
3290	5	0.999957
3300	3	0.999957
3310	12	0.999958
3320	14	0.999959
3330	18	0.999960
3340	11	0.999961
3350	10	0.999961
3360	10	0.999962
3370	15	0.999963
3380	9	0.999964
3390	8	0.999964
3400	5	0.999964
3410	7	0.999965
3420	2	0.999965
3430	3	0.999965
3440	2	0.999965
3450	2	0.999965
3460	5	0.999966
3470	6	0.999966
3480	2	0.999966
3490	2	0.999966
3500	3	0.999967
3510	1	0.999967
3520	1	0.999967
3530	4	0.999967
3540	5	0.999967
3550	2	0.999967
3560	7	0.999968
3570	3	0.999968
3580	6	0.999968
3590	3	0.999969
3610	2	0.999969
3620	4	0.999969
3630	2	0.999969
3640	4	0.999969
3660	2	0.999970
3670	3	0.999970
3680	2	0.999970
3690	4	0.999970
3700	3	0.999970
3710	4	0.999971
3720	4	0.999971
3730	11	0.999972
3740	12	0.999972
3750	6	0.999973
3760	2	0.999973
3780	3	0.999973
3790	5	0.999973
3800	4	0.999974
3810	7	0.999974
3820	13	0.999975
3830	5	0.999975
3840	4	0.999975
3850	5	0.999976
3860	9	0.999976
3870	2	0.999976
3880	4	0.999977
3890	4	0.999977
3900	7	0.999977
3910	7	0.999978
3920	16	0.999979
3930	7	0.999979
3940	9	0.999980
3950	10	0.999981
3960	9	0.999981
3970	11	0.999982
3980	6	0.999982
3990	5	0.999983
4000	3	0.999983
4020	2	0.999983
4040	1	0.999983
4050	1	0.999983
4060	1	0.999983
4070	3	0.999983
4080	1	0.999983
4090	3	0.999983
4100	4	0.999984
4110	2	0.999984
4130	1	0.999984
4160	3	0.999984
4190	3	0.999984
4200	5	0.999985
4210	1	0.999985
4220	2	0.999985
4230	1	0.999985
4240	1	0.999985
4250	1	0.999985
4260	2	0.999985
4290	1	0.999985
4310	4	0.999985
4320	4	0.999986
4330	4	0.999986
4340	4	0.999986
4350	3	0.999986
4360	1	0.999986
4370	4	0.999987
4380	2	0.999987
4390	5	0.999987
4400	10	0.999988
4410	3	0.999988
4420	5	0.999988
4430	7	0.999989
4440	2	0.999989
4460	1	0.999989
4470	1	0.999989
4480	1	0.999989
4490	1	0.999989
4500	3	0.999989
4510	2	0.999989
4520	3	0.999990
4530	1	0.999990
4540	2	0.999990
4550	2	0.999990
4560	1	0.999990
4570	2	0.999990
4580	2	0.999990
4590	5	0.999991
4600	3	0.999991
4610	2	0.999991
4620	1	0.999991
4630	2	0.999991
4640	2	0.999991
4650	8	0.999992
4660	1	0.999992
5050	1	0.999992
5080	1	0.999992
5090	1	0.999992
5100	1	0.999992
5110	3	0.999992
5140	1	0.999992
5150	3	0.999993
5170	1	0.999993
5180	2	0.999993
5230	1	0.999993
5240	2	0.999993
5250	2	0.999993
5380	1	0.999993
5450	1	0.999993
5460	3	0.999993
5470	2	0.999994
5480	3	0.999994
5490	1	0.999994
5510	3	0.999994
5520	5	0.999994
5530	1	0.999994
5540	2	0.999994
5550	1	0.999995
5560	3	0.999995
5570	1	0.999995
5580	1	0.999995
5590	1	0.999995
5600	2	0.999995
5610	3	0.999995
5620	7	0.999996
5630	5	0.999996
5640	2	0.999996
5650	2	0.999996
5660	2	0.999996
5670	5	0.999997
5680	6	0.999997
5690	4	0.999997
5700	3	0.999997
5710	2	0.999998
5750	1	0.999998
5770	1	0.999998
5780	2	0.999998
5790	1	0.999998
5800	4	0.999998
5810	6	0.999999
5820	3	0.999999
5830	3	0.999999
5840	1	0.999999
5850	1	0.999999
5860	3	0.999999
5870	1	0.999999
5880	2	0.999999
5900	5	1.000000
5910	3	1.000000
a_type	l_type	max	min	avg	cnt	percentage
0	0	16	3	7.897	29	0.00018%
1	0	5252	1	462.592	4442317	28.33175%
3	0	5904	9	931.249	11236206	71.66112%
4	0	4601	42	1816.062	1085	0.00692%
6	0	4062	3182	3594.750	4	0.00003%
--------------------------------------------
|            bench type:                   |
--------------------------------------------
----algorithm----
[0~100(usec)]: 15679641
[100~200(usec)]: 0
[200~300(usec)]: 0
[300~400(usec)]: 0
[400~500(usec)]: 0
[500~600(usec)]: 0
[600~700(usec)]: 0
[700~800(usec)]: 0
[800~900(usec)]: 0
[900~1000(usec)]: 0
[over_ms]: 0
[over__s]: 0
----lower----
[0~100(usec)]: 0
[100~200(usec)]: 0
[200~300(usec)]: 0
[300~400(usec)]: 0
[400~500(usec)]: 0
[500~600(usec)]: 0
[600~700(usec)]: 0
[700~800(usec)]: 0
[800~900(usec)]: 0
[900~1000(usec)]: 0
[over_ms]: 0
[over__s]: 0
----average----
[avg_algo]: 0.0
[avg_low]: 0.0
-----lower_info----
[write_op]: 0
[read_op]: 0
[trim_op]:79236
[WAF, RAF]: 0.000000, 0.000000
[if rw test]: 0.000000(WAF), 0.000000(RAF)
[all write Time]:0.0
[all read Time]:0.0

----summary----
[all_time1]: 100.670053
[all_time2]: 390.522947
[size]: 244994.390625(mb)
[FAIL NUM] 0
[SUCCESS RATIO] 1.000000
[throughput1] 642405.927557(kb/s)
             627.349539(mb/s)
[throughput2] 2492044.540793(kb/s)
             2433.637247(mb/s)
[cache hit cnt,ratio] 0, 0.000000
[READ WRITE CNT] 15679641 15679641
error cnt:0
result of ms:
---
bye bye!
# of gc: 79236
# of translation page gc: 60311
# of data page gc: 18925
# of translation page gc w/ data page gc: 20807
# of translation page gc w/ read op: 4
# of evict: 22477803
# of buf hit: 29
!!! print info !!!
BH: buffer hit, H: hit, R: read, MC: memcpy, CE: clean eviction, DE: dirty eviction, GC: garbage collection
a_type--->>> 0: BH, 1: H
2: R & MC, 3: R & CE & MC
4: R & DE & MC, 5: R & CE & GC & MC
6: R & DE & GC & MC
!!! print info !!!
Cache hit on read: 4442317
Cache miss on read: 11237295
Cache hit on write: 20117578
Cache miss on write: 11241593

Miss ratio: 71.68%
Miss ratio on read : 71.67%
Miss ratio on write: 71.70%

Clean hit on read: 4442092
Dirty hit on read: 225
Clean hit on write: 4
Dirty hit on write: 20117574

# Clean eviction: 11236206
# Dirty eviction: 11241597

Clean eviciton on read: 11236206
Dirty eviction on read: 1089
Clean eviction on write: 0
Dirty eviction on write: 11240508

Dirty eviction ratio: 50.01%
Dirty eviction ratio on read: 0.01%
Dirty eviction ratio on write: 100.00%

WAF: 1.72


num caching: 1085
num_flying: 0

TRIM	79236
TR	22525542
TW	11241597
TGCR	13797952
TGCW	19641722
DR	15679612
DW	7839744
DGCR	7878688
DGCW	6046030

Total Read Traffic : 59881794
Total Write Traffic: 44769093

Total WAF: 5.71

all read time:52.22
write_q_hit:110	read_q_hit:0	retry_hit:0
locality check:0.000000