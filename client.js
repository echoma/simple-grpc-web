const {EchoRequest, EchoResponse} = require('./echo_pb.js');
const {EchoClient} = require('./echo_grpc_web_pb.js');

var client = new EchoClient('http://localhost:8080');

var request = new EchoRequest();
request.setMessage('Fuck U');

client.echo(request, {}, (err, response) => {
  console.log(err, response);
  if(response)
    console.log(response.getMessage())
});
