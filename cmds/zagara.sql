SELECT
    ability_link, ability_cmd_index, cmd_flags,
    point_x IS NOT NULL AS pointx,
    COUNT(ability_link)
FROM cmd_event
GROUP BY ability_link, ability_cmd_index, pointx, cmd_flags
ORDER BY pointx, ability_link, cmd_flags;
-- zagara ability, target point, count
-- abilty 367 can be both targeted and not!
351|0|258|0|5
352|0|256|0|16
352|0|258|0|9
367|3|256|0|12
392|0|256|0|1
||266|1|0
||1048840|1|0
45|0|256|1|111
367|4|256|1|1
521|0|256|1|5
525|0|256|1|50
527|0|256|1|44
528|0|256|1|94
528|0|258|1|2
529|0|256|1|50

SELECT DISTINCT
    ability_link, ability_cmd_index, cmd_flags, other_unit, player_id, target_unit_flags, snapshot_unit_link, tag,
    point_x IS NOT NULL AS pointx,
    count(*)
FROM cmd_event
GROUP BY ability_link, ability_cmd_index, cmd_flags, other_unit, player_id, target_unit_flags, snapshot_unit_link, tag, pointx
ORDER BY pointx, ability_link, cmd_flags
351|0|258||||||0|5
352|0|256||||||0|16
352|0|258||||||0|9
367|3|256|79429635|||||0|12
392|0|256||||||0|1
||266||||||1|39
||266||0|111|413|64487430|1|4
||266||11|111|544|7602177|1|1
||1048840||||||1|251
||1048840||0|111|413|64487430|1|2
||1048840||7|111|309|51904513|1|3
||1048840||10|111|318|53477377|1|1
||1048840||11|111|544|1572865|1|1
||1048840||11|111|544|7602177|1|1
||1048840||12|111|432|67371049|1|1
||1048840||12|111|608|16252929|1|1
45|0|256||||||1|64
45|0|256||6|111|303|51118081|1|3
45|0|256||7|111|309|51904513|1|5
45|0|256||8|111|903|52428801|1|4
45|0|256||9|111|829|52953089|1|10
45|0|256||10|111|318|53477377|1|1
45|0|256||12|111|538|786433|1|3
45|0|256||12|111|538|2621441|1|1
45|0|256||12|111|538|6553601|1|2
45|0|256||12|111|540|9437185|1|1
45|0|256||12|111|540|9699329|1|1
45|0|256||12|111|544|12320769|1|2
45|0|256||12|111|545|3932161|1|1
45|0|256||12|111|608|16252929|1|5
45|0|256||12|111|670|17563649|1|1
45|0|256||15|111|567|40894482|1|1
45|0|256||15|111|567|71565327|1|2
45|0|256||15|111|568|69730325|1|3
45|0|256||15|111|568|79167533|1|1
367|4|256|61866101|||||1|1
521|0|256||||||1|5
525|0|256||||||1|50
527|0|256||||||1|44
528|0|256||||||1|94
528|0|258||||||1|2
529|0|256||6|111|303|51118081|1|8
529|0|256||7|111|309|51904513|1|6
529|0|256||8|111|903|52428801|1|4
529|0|256||9|111|829|52953089|1|12
529|0|256||10|111|318|53477377|1|7
529|0|256||12|111|514|20971521|1|1
529|0|256||12|111|538|1835009|1|1
529|0|256||12|111|538|2621441|1|1
529|0|256||12|111|538|6553601|1|1
529|0|256||12|111|540|9437185|1|1
529|0|256||12|111|541|43778049|1|1
529|0|256||12|111|544|12320769|1|1
529|0|256||12|111|545|3932161|1|1
529|0|256||12|111|608|16252929|1|2
529|0|256||15|111|567|40894482|1|1
529|0|256||15|111|568|79167533|1|1
529|0|256||15|111|816|51380225|1|1

SELECT
    cmd_flags,
    COUNT(cmd_flags)
FROM cmd_event
GROUP BY cmd_flags
ORDER BY cmd_flags;
256|384
258|16
266|44
1048840|261

SELECT DISTINCT ability_link, cmd_flags FROM cmd_event;

SELECT
    cmd_flags,
    -- other_unit,
    sequence
    -- player_id, target_unit_flags, snapshot_unit_link, tag
FROM cmd_event
WHERE ability_link = 352;
-- 258 or 256 for cmd_flags, unique ascending sequence values

SELECT
    cmd_flags,
    other_unit,
    sequence
    -- player_id, target_unit_flags, snapshot_unit_link, tag
FROM cmd_event
WHERE ability_link = 367;
256|79429635|990
256|79429635|1180
256|79429635|1427
256|79429635|1544
256|79429635|1714
256|79429635|1882
256|79429635|2049
256|79429635|2304
256|79429635|2547
256|79429635|2710
256|79429635|2915
256|79429635|3374
256|61866101|3411

SELECT
    other_unit,
    COUNT(other_unit)
FROM cmd_event
GROUP BY other_unit
ORDER BY other_unit;
61866101|1
79429635|12

SELECT
    player_id,
    COUNT(player_id)
FROM cmd_event
GROUP BY player_id
ORDER BY player_id;
-- players zagara issues commands at                                                 
0|6  
6|11 
7|14 
8|8  
9|22 
10|9 
11|3 
12|29
15|10

SELECT
    target_unit_flags,
    COUNT(target_unit_flags)
FROM cmd_event
GROUP BY target_unit_flags
ORDER BY target_unit_flags;
111|112

SELECT
    snapshot_unit_link,
    COUNT(snapshot_unit_link)
FROM cmd_event
GROUP BY snapshot_unit_link
ORDER BY snapshot_unit_link;
303|11
309|14
318|9
413|6
432|1
514|1
538|9
540|3
541|1
544|6
545|2
567|4
568|5
608|8
670|1
816|1
829|22
903|8

SELECT
    tag,
    COUNT(tag)
FROM cmd_event
GROUP BY tag
ORDER BY tag;
786433|3
1572865|1
1835009|1
2621441|2
3932161|2
6553601|3
7602177|2
9437185|2
9699329|1
12320769|3
16252929|8
17563649|1
20971521|1
40894482|2
43778049|1
51118081|11
51380225|1
51904513|14
52428801|8
52953089|22
53477377|9
64487430|6
67371049|1
69730325|3
71565327|2
79167533|2
