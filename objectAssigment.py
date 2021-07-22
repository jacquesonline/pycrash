import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
        
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for connection in self.connections.keys():
            load = self.connections[connection]
            total += load 
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")
server.add_connection("192.168.1.2")
server.add_connection("192.168.1.3")
server.add_connection("192.168.1.4")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break
           
    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load/total_server

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            print("Adding connection")
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

# Be sure that the load balancer now has an average 
# load more than 0 before proceeding.
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
l.add_connection("fdca:83d2::f20e")
l.add_connection("fdca:83d2::f20f")
print(l.avg_load())

# What if we add a new server?
l.servers.append(Server())
print(l.avg_load())

# Fill in the code of the LoadBalancing
# class to make the load go back to zero once the connection is closed.

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)

print(l)

print(l.avg_load())

