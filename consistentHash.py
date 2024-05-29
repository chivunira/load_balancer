class ConsistentHashMap:
    def __init__(self, N, M, K):
        self.N = N  # Number of Server Containers managed by the load balancer
        self.M = M  # Total number of slots in the consistent hash map
        self.K = K  # Number of virtual servers for each server container

        # Initialize the hash map with empty lists for virtual servers
        self.hash_map = [[] for _ in range(M)]
        # Initialize a list to keep track of the number of virtual servers in each slot
        self.virtual_servers_count = [0] * M

    def add_server(self, server_id):
        # Add the physical server to the consistent hash map
        for j in range(self.K):
            virtual_server_id = f"{server_id}-{j}"  # Generate virtual server ID
            slot = self.get_slot(virtual_server_id)
            self.hash_map[slot].append(virtual_server_id)  # Add virtual server ID to hash map
            self.virtual_servers_count[slot] += 1  # Increment

    def remove_server(self, server_id):
        # Remove the server from the consistent hash map
        for j in range(self.K):
            virtual_server_id = f"{server_id}-{j}"
            slot = self.get_slot(virtual_server_id)
            if virtual_server_id in self.hash_map[slot]:
                self.hash_map[slot].remove(virtual_server_id)
                self.virtual_servers_count[slot] -= 1  # Decrement the count of virtual servers in the slot

    def get_slot(self, key):
        server_id = key.split('-')[0]
        hashed_value = self.H(server_id)
        slot = hashed_value % self.M
        print(f"Key: {key}, Server ID: {server_id}, Hashed Value: {hashed_value}, Slot: {slot}")
        return slot

    @staticmethod
    def H(i):
        # Hash function for request mapping H(i) = i + 2i + 17
        i = int(i)
        return i + 2 * i + 17

    def Phi(self, i, j):
        return i + j + 2 * j + 25
