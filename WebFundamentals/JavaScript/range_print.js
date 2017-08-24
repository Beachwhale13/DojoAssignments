function printRange(start, end, skip){
  for (var i = start; i < end; i += skip){
    console.log(i);
  }
}


//if user doesn't pass a skip amount, default to 1

function printRange(start, end, skip){
  for (var i = start; i < end; i += (skip || 1)){
    console.log(i);
  }
}

//if user doesn't pass and end point, make it start at 0 and end at the first
function printRange(start, end, skip){
	if (typeof start = "number" && typeof end = "number"){
		for (var i = start; i < end; i += (skip || 1)){
    		console.log(i);
		}
  	}
  	else {
  		for (var i = 0; i < start; i += (skip || 1)){
  			console.log(i);
  		}
  	}