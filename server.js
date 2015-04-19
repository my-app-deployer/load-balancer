var net=require('net'),
	http = require('http'),
    httpProxy = require('http-proxy'),
    mongoose=require('mongoose'),
    assert = require('assert'),
    proxyServer=require('./proxy'),
    fs=require('fs');
port=5050

// Connect to the db
mongoose.connect('mongodb://127.0.0.1/servers');
var AppServers=require('./schema/AppServer');

var proxyRouter = new proxyServer({
	model:AppServers,
  	cache_ttl: 5
});

var proxy=httpProxy.createServer({});
var server=http.createServer(function(req,res){
	
	var hostname = req.headers.host.split(':')[0];
	console.log(req);
	proxyRouter.lookupHostname(hostname,function(route){
		if(route){
			var target="http"+"://"+route.host+":"+route.port/*+req.url*/;
				console.log(route);
				console.log("http"+"://"+route.host+":"+route.port+req.url);
				proxy.web(req,res,{target:target});

		}
		else{
			console.log("Error, 404");
      		try {
		        res.writeHead(404);
		        res.end();
		      } 
		      catch (er) {
		        console.error("res.writeHead/res.end error: %s", er.message);
		      }
			}
	});
}).listen(port);
console.log("listening on port ",port)