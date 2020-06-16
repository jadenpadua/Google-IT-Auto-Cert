import random

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = []

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        if server not in self.connections:
            self.connections[server] = [connection_id]
            server.add_connection(connection_id)
        else:
            self.connections[server].append(connection_id)
            server.add_connection(connection_id)
        

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        for key in self.connections:
            if connection_id in self.connections[key]:
                key.close_connection(connection_id)
                self.connections[key].remove(connection_id)

    def avg_load(self):
        """Calculates the average load of all servers"""
        avg_load = 0
        for server in self.connections:
            avg_load += server.load()

        return avg_load / len(self.connections)

    def ensure_availability(self):
        if avg_load() > 50:
            newServer = Server()
            self.servers.append(newServer)

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
