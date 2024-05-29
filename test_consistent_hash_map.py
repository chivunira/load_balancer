import unittest
from consistentHash import ConsistentHashMap


class TestConsistentHashMap(unittest.TestCase):
    def setUp(self):
        self.N = 3
        self.M = 512
        self.K = 9
        self.chm = ConsistentHashMap(self.N, self.M, self.K)

    def test_add_server(self):
        server_ids = ['1', '2', '3']
        for server_id in server_ids:
            self.chm.add_server(server_id)

        # Assert that each server is added to the hash map
        for server_id in server_ids:
            for j in range(self.K):
                virtual_server_id = f"{server_id}-{j}"
                slot = self.chm.get_slot(virtual_server_id)
                self.assertIn(virtual_server_id, self.chm.hash_map[slot])

    def test_remove_server(self):
        server_ids = [1, 2, 3]
        for server_id in server_ids:
            self.chm.add_server(server_id)

        # Remove a server and assert it's no longer in the hash map
        server_id_to_remove = 2
        self.chm.remove_server(server_id_to_remove)
        for j in range(self.K):
            virtual_server_id = f"{server_id_to_remove}-{j}"
            slot = self.chm.get_slot(virtual_server_id)
            self.assertNotIn(virtual_server_id, self.chm.hash_map[slot])

    def test_get_slot(self):
        server_id = 1
        virtual_server_id = f"{server_id}-0"
        expected_slot = self.chm.H(server_id) % self.M
        self.assertEqual(self.chm.get_slot(virtual_server_id), expected_slot)


if __name__ == "__main__":
    unittest.main()
