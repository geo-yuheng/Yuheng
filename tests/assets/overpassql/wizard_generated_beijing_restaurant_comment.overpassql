/*
This has been generated by the overpass-turbo wizard.
The original search was:
“amenity=restaurant in Beijing”
*/
[out:json][timeout:25];
// fetch area “Beijing” to search in
{{geocodeArea:Beijing}}->.searchArea;
// gather results
nwr["amenity"="restaurant"/*
这里应该解释一下，食堂和餐馆使用了同样的标注模式因此暂时无法区分
或许未来引入["amenity"="canteen"]之类的tag有主意更好的筛选
*/](area.searchArea);
out geom;// print results