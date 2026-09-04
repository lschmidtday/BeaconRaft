# test_beaconraft.py
"""
Tests for BeaconRaft module.
"""

import unittest
from beaconraft import BeaconRaft

class TestBeaconRaft(unittest.TestCase):
    """Test cases for BeaconRaft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeaconRaft()
        self.assertIsInstance(instance, BeaconRaft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeaconRaft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
