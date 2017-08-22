function printRange(start, end, skip){
  for (var i = start; i < end; i += skip){
    console.log(i);
  }
}


function printRange(start, end, skip){
  for (var i = start; i < end; i += (skip || 1)){
    console.log(i);
  }
}
