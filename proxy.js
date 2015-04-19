var ProxyServer=function(opts){
	this.model=opts.model
	this.cache_ttl	= (opts.cache_ttl || 10) * 1000;
	this.cache     	= {};
}
ProxyServer.prototype.lookupHostname = function(hostname,callback) {
	var self=this;
	console.log('{"Load":{"$lt":"60"},"Domaine":hostname,"$or":[{"Load":{"$lt":"60"}},{"Ip":hostname}]}');
	if(!self.cache[hostname]){
		var q=self.model.where({"Load":{"$lte":"60"}},{"Domaine":hostname});
		//{"Load":{"$lt":"60"},"Domaine":hostname,"$or":[{"Load":{"$lt":"60"}},{"Ip":hostname}]}
		q.findOne().exec(function(err,doc){
			if(!err){
				if(doc){
					var target={host:doc.Ip,port:doc.Port};
					self.cache[hostname]=target;
					self.expire_route(hostname,self.cache_ttl);
					console.log(target);
					callback(target);
				}
				else{
					callback(null);
				}
			}
		})
	}
	else{
		callback(this.cache[hostname])
	}
};
ProxyServer.prototype.flush = function() {
	this.cache={};
};
ProxyServer.prototype.flush_route = function(hostname) {
  delete(this.cache[hostname]);
};
ProxyServer.prototype.expire_route = function(hostname, ttl) {
  var self = this;
  setTimeout(function() {
    self.flush_route(hostname);
  }, ttl);
};
module.exports=ProxyServer;