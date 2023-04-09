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
 |  -Mixed Cache entries:  1024
 |  -Cache Percentage:     25.000%
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
bench range:0 ~ 15679641
15313 X 1024 = 15680512, answer=15679640
making seq Set bench!



45937 X 1024 = 47039488, answer=47038922
making rand Set bench!


30625 X 1024 = 31360000, answer=31359282
making rand Set and Get bench!
last set:1023


req_cnt_test:cnt -> 94077839:0 fuck
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
[all_time]: 75.577414
[size]: 244994.375000(mb)
[FAIL NUM] 0
[SUCCESS RATIO] 1.000000
[throughput] 3319434.030913(kb/s)
             3241.634796(mb/s)
[READ WRITE CNT] 0 15679640
error cnt:0



[cdf]read---
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
[trim_op]:237308
[WAF, RAF]: 0.000000, 0.000000
[if rw test]: 0.000000(WAF), 0.000000(RAF)
[all write Time]:0.0
[all read Time]:0.0

----summary----
[all_time]: 1078.618316
[size]: 734983.156250(mb)
[FAIL NUM] 0
[SUCCESS RATIO] 1.000000
[throughput] 697765.595889(kb/s)
             681.411715(mb/s)
[READ WRITE CNT] 0 47038922
error cnt:0



[cdf]read---
0	57	0.000004
10	646	0.000045
20	1406	0.000135
30	1691	0.000242
40	1583	0.000343
50	1259	0.000424
60	1282	0.000505
70	1033	0.000571
80	818	0.000623
90	719	0.000669
100	657	0.000711
110	631	0.000751
120	601	0.000790
130	550	0.000825
140	476	0.000855
150	420	0.000882
160	444	0.000910
170	365	0.000934
180	398	0.000959
190	386	0.000984
200	364	0.001007
210	379	0.001031
220	395	0.001056
230	420	0.001083
240	450	0.001112
250	437	0.001140
260	411	0.001166
270	464	0.001195
280	423	0.001222
290	425	0.001249
300	469	0.001279
310	469	0.001309
320	554	0.001345
330	568	0.001381
340	715	0.001426
350	1237	0.001505
360	3392	0.001722
370	9792	0.002346
380	25148	0.003950
390	53467	0.007360
400	96022	0.013484
410	150689	0.023094
420	212038	0.036618
430	268608	0.053749
440	314242	0.073790
450	349123	0.096056
460	364503	0.119303
470	360643	0.142304
480	340410	0.164014
490	307094	0.183599
500	265381	0.200525
510	221215	0.214633
520	177485	0.225952
530	137726	0.234736
540	103395	0.241330
550	75385	0.246138
560	53857	0.249573
570	38099	0.252003
580	26705	0.253706
590	18969	0.254916
600	13797	0.255796
610	10403	0.256459
620	8405	0.256995
630	7367	0.257465
640	6735	0.257895
650	6629	0.258318
660	6849	0.258754
670	7501	0.259233
680	7774	0.259729
690	8398	0.260264
700	8485	0.260805
710	8214	0.261329
720	8092	0.261845
730	7658	0.262334
740	7476	0.262810
750	7429	0.263284
760	8248	0.263810
770	9659	0.264426
780	12285	0.265210
790	17410	0.266320
800	25563	0.267950
810	37859	0.270365
820	57310	0.274020
830	84139	0.279386
840	123758	0.287279
850	177662	0.298610
860	247231	0.314377
870	329796	0.335411
880	424936	0.362512
890	526211	0.396072
900	628172	0.436135
910	719879	0.482047
920	793563	0.532658
930	842433	0.586386
940	859448	0.641199
950	845603	0.695129
960	804275	0.746423
970	740891	0.793675
980	656910	0.835570
990	560151	0.871295
1000	462945	0.900820
1010	371280	0.924499
1020	289299	0.942950
1030	220600	0.957019
1040	162547	0.967386
1050	117593	0.974886
1060	83603	0.980218
1070	57699	0.983898
1080	39801	0.986436
1090	27572	0.988194
1100	19555	0.989442
1110	13897	0.990328
1120	10390	0.990990
1130	7906	0.991495
1140	5928	0.991873
1150	4722	0.992174
1160	3967	0.992427
1170	3377	0.992642
1180	2974	0.992832
1190	2591	0.992997
1200	2318	0.993145
1210	2085	0.993278
1220	1901	0.993399
1230	1841	0.993517
1240	1695	0.993625
1250	1577	0.993725
1260	1446	0.993818
1270	1286	0.993900
1280	1154	0.993973
1290	1106	0.994044
1300	1153	0.994117
1310	1136	0.994190
1320	1219	0.994267
1330	1489	0.994362
1340	1753	0.994474
1350	2397	0.994627
1360	3286	0.994837
1370	4221	0.995106
1380	5090	0.995431
1390	5728	0.995796
1400	6028	0.996180
1410	6076	0.996568
1420	5876	0.996943
1430	5562	0.997297
1440	4733	0.997599
1450	3861	0.997845
1460	3311	0.998057
1470	2729	0.998231
1480	2251	0.998374
1490	1864	0.998493
1500	1621	0.998596
1510	1332	0.998681
1520	1288	0.998764
1530	1060	0.998831
1540	977	0.998893
1550	854	0.998948
1560	800	0.998999
1570	762	0.999048
1580	761	0.999096
1590	687	0.999140
1600	685	0.999184
1610	691	0.999228
1620	578	0.999264
1630	495	0.999296
1640	483	0.999327
1650	478	0.999357
1660	455	0.999386
1670	470	0.999416
1680	396	0.999442
1690	392	0.999467
1700	330	0.999488
1710	255	0.999504
1720	240	0.999519
1730	239	0.999534
1740	176	0.999546
1750	137	0.999554
1760	108	0.999561
1770	91	0.999567
1780	87	0.999573
1790	73	0.999577
1800	70	0.999582
1810	80	0.999587
1820	78	0.999592
1830	68	0.999596
1840	67	0.999600
1850	48	0.999604
1860	53	0.999607
1870	38	0.999609
1880	32	0.999611
1890	31	0.999613
1900	30	0.999615
1910	21	0.999617
1920	31	0.999619
1930	27	0.999620
1940	19	0.999622
1950	19	0.999623
1960	21	0.999624
1970	10	0.999625
1980	15	0.999626
1990	26	0.999627
2000	21	0.999629
2010	16	0.999630
2020	29	0.999632
2030	24	0.999633
2040	16	0.999634
2050	37	0.999636
2060	49	0.999640
2070	59	0.999643
2080	33	0.999645
2090	22	0.999647
2100	34	0.999649
2110	9	0.999650
2120	16	0.999651
2130	25	0.999652
2140	32	0.999654
2150	41	0.999657
2160	27	0.999659
2170	19	0.999660
2180	19	0.999661
2190	21	0.999662
2200	33	0.999664
2210	46	0.999667
2220	28	0.999669
2230	29	0.999671
2240	24	0.999673
2250	36	0.999675
2260	27	0.999677
2270	33	0.999679
2280	32	0.999681
2290	27	0.999682
2300	26	0.999684
2310	18	0.999685
2320	20	0.999686
2330	7	0.999687
2340	16	0.999688
2350	15	0.999689
2360	24	0.999690
2370	32	0.999692
2380	22	0.999694
2390	32	0.999696
2400	44	0.999699
2410	44	0.999701
2420	50	0.999705
2430	35	0.999707
2440	32	0.999709
2450	33	0.999711
2460	19	0.999712
2470	20	0.999714
2480	25	0.999715
2490	22	0.999717
2500	25	0.999718
2510	30	0.999720
2520	36	0.999722
2530	42	0.999725
2540	27	0.999727
2550	43	0.999730
2560	39	0.999732
2570	32	0.999734
2580	45	0.999737
2590	51	0.999740
2600	71	0.999745
2610	26	0.999746
2620	25	0.999748
2630	21	0.999749
2640	19	0.999750
2650	19	0.999752
2660	24	0.999753
2670	30	0.999755
2680	27	0.999757
2690	19	0.999758
2700	15	0.999759
2710	21	0.999760
2720	24	0.999762
2730	13	0.999763
2740	10	0.999763
2750	9	0.999764
2760	15	0.999765
2770	31	0.999767
2780	40	0.999769
2790	32	0.999771
2800	21	0.999773
2810	17	0.999774
2820	20	0.999775
2830	29	0.999777
2840	30	0.999779
2850	22	0.999780
2860	32	0.999782
2870	65	0.999787
2880	60	0.999790
2890	40	0.999793
2900	66	0.999797
2910	58	0.999801
2920	33	0.999803
2930	21	0.999804
2940	11	0.999805
2950	15	0.999806
2960	22	0.999807
2970	33	0.999809
2980	13	0.999810
2990	4	0.999811
3000	7	0.999811
3010	13	0.999812
3020	11	0.999812
3030	8	0.999813
3040	8	0.999813
3050	6	0.999814
3060	11	0.999815
3070	5	0.999815
3080	10	0.999816
3090	10	0.999816
3100	15	0.999817
3110	16	0.999818
3120	6	0.999819
3130	19	0.999820
3140	26	0.999821
3150	16	0.999822
3160	22	0.999824
3170	29	0.999826
3180	31	0.999828
3190	31	0.999830
3200	25	0.999831
3210	47	0.999834
3220	52	0.999838
3230	54	0.999841
3240	63	0.999845
3250	47	0.999848
3260	52	0.999851
3270	41	0.999854
3280	36	0.999856
3290	37	0.999859
3300	44	0.999861
3310	54	0.999865
3320	45	0.999868
3330	26	0.999869
3340	16	0.999870
3350	27	0.999872
3360	42	0.999875
3370	41	0.999877
3380	29	0.999879
3390	55	0.999883
3400	47	0.999886
3410	30	0.999888
3420	20	0.999889
3430	21	0.999890
3440	25	0.999892
3450	37	0.999894
3460	17	0.999895
3470	31	0.999897
3480	18	0.999898
3490	17	0.999900
3500	37	0.999902
3510	30	0.999904
3520	48	0.999907
3530	39	0.999909
3540	39	0.999912
3550	29	0.999914
3560	25	0.999915
3570	36	0.999918
3580	33	0.999920
3590	25	0.999921
3600	26	0.999923
3610	28	0.999925
3620	38	0.999927
3630	40	0.999930
3640	37	0.999932
3650	38	0.999934
3660	25	0.999936
3670	18	0.999937
3680	14	0.999938
3690	17	0.999939
3700	21	0.999941
3710	11	0.999941
3720	8	0.999942
3730	18	0.999943
3740	18	0.999944
3750	15	0.999945
3760	9	0.999946
3770	12	0.999946
3780	20	0.999948
3790	13	0.999948
3800	13	0.999949
3810	6	0.999950
3820	3	0.999950
3830	5	0.999950
3840	7	0.999951
3850	5	0.999951
3860	8	0.999951
3870	9	0.999952
3880	10	0.999953
3890	9	0.999953
3900	15	0.999954
3910	15	0.999955
3920	14	0.999956
3930	11	0.999957
3940	12	0.999958
3950	7	0.999958
3960	9	0.999959
3970	7	0.999959
3980	7	0.999959
3990	7	0.999960
4000	8	0.999960
4010	9	0.999961
4020	10	0.999962
4030	16	0.999963
4040	18	0.999964
4050	6	0.999964
4060	10	0.999965
4070	24	0.999966
4080	12	0.999967
4090	27	0.999969
4100	39	0.999971
4110	55	0.999975
4120	26	0.999976
4130	23	0.999978
4140	12	0.999979
4150	8	0.999979
4160	4	0.999979
4200	9	0.999980
4210	4	0.999980
4220	7	0.999981
4290	1	0.999981
4310	2	0.999981
4320	1	0.999981
4330	3	0.999981
4340	2	0.999981
4350	1	0.999981
4360	1	0.999981
4410	1	0.999982
4420	1	0.999982
4430	3	0.999982
4480	3	0.999982
4490	3	0.999982
4500	5	0.999982
4510	2	0.999983
4520	2	0.999983
4530	2	0.999983
4540	2	0.999983
4550	3	0.999983
4560	5	0.999983
4570	3	0.999984
4580	1	0.999984
4600	3	0.999984
4610	4	0.999984
4620	6	0.999985
4630	3	0.999985
4660	1	0.999985
4860	1	0.999985
4870	1	0.999985
4880	8	0.999985
4890	2	0.999986
4900	19	0.999987
4910	24	0.999988
4920	18	0.999989
4930	13	0.999990
4940	21	0.999992
4950	18	0.999993
4960	2	0.999993
5170	1	0.999993
5330	7	0.999993
5340	31	0.999995
5350	16	0.999996
5360	23	0.999998
5370	16	0.999999
5380	14	1.000000
5390	3	1.000000
a_type	l_type	max	min	avg	cnt	percentage
0	0	15	2	8.054	369	0.00235%
1	0	4951	2	467.899	4195329	26.75654%
3	0	5380	11	942.026	11482917	73.23457%
4	0	4325	28	1882.578	1021	0.00651%
6	0	3763	2491	3178.800	5	0.00003%
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
[trim_op]:76528
[WAF, RAF]: 0.000000, 0.000000
[if rw test]: 0.000000(WAF), 0.000000(RAF)
[all write Time]:0.0
[all read Time]:0.0

----summary----
[all_time1]: 102.612217
[all_time2]: 341.991053
[size]: 244994.390625(mb)
[FAIL NUM] 0
[SUCCESS RATIO] 1.000000
[throughput1] 733569.646923(kb/s)
             716.376608(mb/s)
[throughput2] 2444877.065662(kb/s)
             2387.575259(mb/s)
[cache hit cnt,ratio] 0, 0.000000
[READ WRITE CNT] 15679641 15679641
error cnt:0
result of ms:
---
bye bye!
# of gc: 313836
# of translation page gc: 258444
# of data page gc: 55392
# of translation page gc w/ data page gc: 88756
# of translation page gc w/ read op: 5
# of evict: 57424206
# of buf hit: 369
!!! print info !!!
BH: buffer hit, H: hit, R: read, MC: memcpy, CE: clean eviction, DE: dirty eviction, GC: garbage collection
a_type--->>> 0: BH, 1: H
2: R & MC, 3: R & CE & MC
4: R & DE & MC, 5: R & CE & GC & MC
6: R & DE & GC & MC
!!! print info !!!
Cache hit on read: 4195329
Cache miss on read: 11483943
Cache hit on write: 32456516
Cache miss on write: 45941287

Miss ratio: 183.12%
Miss ratio on read : 73.24%
Miss ratio on write: 293.01%

Clean hit on read: 4195112
Dirty hit on read: 217
Clean hit on write: 2
Dirty hit on write: 32456514

# Clean eviction: 11482917
# Dirty eviction: 45941289

Clean eviciton on read: 11482917
Dirty eviction on read: 1026
Clean eviction on write: 0
Dirty eviction on write: 45940263

Dirty eviction ratio: 80.00%
Dirty eviction ratio on read: 0.01%
Dirty eviction ratio on write: 100.00%

WAF: 3.93


num caching: 1024
num_flying: 0

TRIM	313836
TR	57683172
TW	45941289
TGCR	62327991
TGCW	86386087
DR	15679272
DW	19599232
DGCR	20319959
DGCW	12971004

Total Read Traffic : 156010394
Total Write Traffic: 164897612

Total WAF: 8.41

all read time:57.30
write_q_hit:400	read_q_hit:0	retry_hit:0
locality check:0.000000