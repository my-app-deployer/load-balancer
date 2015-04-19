var mongoose = require('mongoose');

// define our nerd model
// module.exports allows us to pass this to other files when it is called
var AppServerSchema = mongoose.Schema({
 	Load : {type : Number, default: '0'},
    Ip : {type : String, default: ''},
    Port : {type : String, default: '80'},
    Hostname : {type:String,default:''},
    Domaine: {type:String,default:''},
    Cpu_usage: {type:Number,default:''},
    Ram_usage : {type:Number,default:''},
    Requests:{type:Array,default:[]},
    Last_release:{type:Date,default:new Date}
});

module.exports=mongoose.model('AppServer',AppServerSchema);