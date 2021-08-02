
import unittest
from endpoint.pages import get_multiple_params

params = "distance description enclosed"
address = "Moscow Ring Road"
response_dict = get_multiple_params(params=params, address=address)

class TestPages(unittest.TestCase):

    """
    This class validate output of Pages methods
    """

    def test_distance_instance(self):

        """
        Test if distance data types of returns {
            "distance": float, 
            "lower_envelope": float, 
            "unit": str, 
            "upper_envelope": float
        }

        """
        distance_params = response_dict["distance"]
        self.assertTrue(isinstance(distance_params["unit"], str))
        self.assertTrue(isinstance(distance_params["distance"], float))
        self.assertTrue(isinstance(distance_params["lower_envelope"], float))
        self.assertTrue(isinstance(distance_params["upper_envelope"], float))
        pass

    def test_enclosed_logic(self):
        
        self.assertEqual(
            first=address,
            second="Moscow Ring Road",
            msg="Reference address if Moscow Ring Road expect distance to be zero"
        )
        self.assertEqual(response_dict["enclosed"], True)
        pass





