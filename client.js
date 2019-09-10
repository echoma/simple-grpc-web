const {EchoRequest, EchoResponse} = require('./echo_pb.js');
const {EchoClient} = require('./echo_grpc_web_pb.js');

var client = new EchoClient('http://localhost:8080');

var request = new EchoRequest();
request.setName('Fuck U');

client.Echo(request, {}, (err, response) => {
  console.log(response.getMessage());
});
