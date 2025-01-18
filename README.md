# EasyAccess
The system consists of a client and a server. This client can make requests/ commands to the server.
The server will host the 'hub' application (The backend code with api endpoints), Every command will run through firebase (db or realtime)
server_uuid : {
  device1_uuid : { 'api_endpoint' },
  device2_uuid: {},
  device3_uuid: {}
}
