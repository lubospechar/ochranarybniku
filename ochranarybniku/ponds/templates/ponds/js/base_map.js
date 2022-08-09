var center = SMap.Coords.fromWGS84({{ pond.area.centroid.x|safe }}, {{ pond.area.centroid.y|safe }});
var m = new SMap(JAK.gel("map"), center, 17);
m.addDefaultLayer(SMap.DEF_OPHOTO).enable();
m.addDefaultControls();

var layer = new SMap.Layer.Geometry();
m.addLayer(layer);
layer.enable();

var coords = [
{% for coord in pond.area.tuple.0 %}
    SMap.Coords.fromWGS84({{ coord.0|safe }}, {{ coord.1|safe }}),
{% endfor %}
]

var options = {
    //border: "#000000"
};

var polygon = new SMap.Geometry(SMap.GEOMETRY_POLYGON, null, coords, options);
layer.addGeometry(polygon);
