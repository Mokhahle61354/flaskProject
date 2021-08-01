from dataclasses import dataclass
from typing import Mapping, Union
from haversine import haversine, Unit
from typing import Tuple
import numpy as np

@dataclass
class GeoObject:
    data_property: dict
    name: str
    description: str
    lower_corner: Tuple[float, float]
    upper_corner: Tuple[float, float]
    point: Tuple[float, float]
    """
    Data class thata hold geo object for the city.

    Attributes
    ----------
    Name : str
        Name of the place.
    description: str
        discription of the place
    point: Tuple
        location as (latitude, longitude)
    envelope: Mapping(str, Mapping(str, str))
        boundries of the place, in a format of:
        `
            {
                "lowerCorner": "37.597899 55.744374",
                "upperCorner": "37.648753 55.768339"
            }
        `
    """

    pass

@dataclass
class ComputeGeoObject:
    reference_city: GeoObject
    selected_city: GeoObject
    # discription: str

    def _havasine_distance(address1:Tuple[float, float], address2:Tuple[float, float])->float:
        """
        Gets the distance from address1 to address2 in Kilometers.

        Args:
            address1 (Tuple[float, float]): (latitude, longitude)
            address2 (Tuple[float, float]): (latitude, longitude)

        Returns:
            float: distance in kilometeres
        """    
        return haversine(address1, address2, unit=Unit.KILOMETERS)

    def get_point_distance(self):
        # ___rprt_
        position_point1 = self.reference_city.point
        position_point2 = self.selected_city.point
        distance = haversine(position_point1, position_point2, unit=Unit.KILOMETERS)
        return {'distance':distance, 'unit':"km"}
    
    def get_envelope_distances(self):
        ref_city_upper_corner = self.reference_city.upper_corner
        ref_city_lower_corner = self.reference_city.lower_corner
        selected_city_upper_corner = self.selected_city.upper_corner
        selected_city_lower_corner = self.selected_city.lower_corner

        """
        This method will calculate distace from (upper or lower) enelope of reference city
        to selected city/location by using haversine.
        """

        upper_envelope_distance = haversine(
            point1 = ref_city_upper_corner,
            point2 = selected_city_upper_corner,
            unit=Unit.KILOMETERS
        )
        lower_envelope_distance = haversine(
            point1 = ref_city_lower_corner,
            point2 = selected_city_lower_corner,
            unit=Unit.KILOMETERS
        )
        return {
            'upper_envelope': upper_envelope_distance,
            'lower_envelope': lower_envelope_distance
        }

    def is_inside_evelope(self)-> bool:
        """
        Enclose area is a circle radius of lower and upper evelope.
        To check is selected city in enclosed by reference city will use arithmetic logic:
        for (u1, l1) (u2, l2):
            - if (l1<u2 and u2<u1) or (u1>l2 and l2>l1) then enclosed.
        Returns:
            bool: Returns True if reference city encloses selected city.
        """
        ref_upper_corner = self.reference_city.upper_corner
        ref_lower_corner = self.reference_city.lower_corner
        upper_corner = self.selected_city.upper_corner
        lower_corner = self.selected_city.lower_corner
        
        condition1 = (ref_lower_corner[0] < upper_corner[0]) and (ref_lower_corner[1] > upper_corner[1])
        condition2 = ref_upper_corner[0] > upper_corner[1] and ref_upper_corner[1] < lower_corner[1]
        final_result = bool(condition1 and condition2)
        return final_result
        pass

    
