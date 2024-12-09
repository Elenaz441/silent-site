from uuid import UUID
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[UUID, list[WebSocket]] = {}

    async def connect(self, room_id: UUID, websocket: WebSocket):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, room_id, websocket: WebSocket):
        self.active_connections[room_id].remove(websocket)
        if len(self.active_connections[room_id]) == 0:
            del self.active_connections[room_id]

    async def broadcast(self, room_id: UUID, data: dict, self_websocket: WebSocket):
        for connection in self.active_connections[room_id]:
            if connection != self_websocket:
                await connection.send_json(data)


manager = ConnectionManager()
