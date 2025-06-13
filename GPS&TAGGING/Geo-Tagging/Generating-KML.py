from pykml.factory import KML_ElementMaker as KML
from lxml import etree

doc = KML.kml(
    KML.Document(
        KML.Placemark(
            KML.name("Victim Location"),
            KML.Point(
                KML.coordinates("77.5946,12.9716,35")
            )
        )
    )
)

with open("tagged_location.kml", "wb") as f:
    f.write(etree.tostring(doc, pretty_print=True))