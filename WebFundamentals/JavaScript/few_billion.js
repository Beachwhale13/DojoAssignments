function fewBillion(days){
  var sum = .01;
  for (var i = 2; i<=days; i++){
    sum = sum + sum;
  }
  return sum;
}

fewBillion(30);

//answer: 5,368,709.12
