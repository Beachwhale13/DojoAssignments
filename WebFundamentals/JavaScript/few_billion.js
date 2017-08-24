function fewBillion(days){
  var sum = .01;
  for (var i = 2; i<=days; i++){
    sum = sum + sum;
  }
  return sum;
}

fewBillion(30);

//answer: 5,368,709.12

//how many days to make 10,000?
function fewBillion(days){
  var sum = .01;
  for (var i = 2; i<=days; i++){
    sum = sum + sum;
    if (sum >= 10000.00){
      console.log(i);
      break;
    }
  }
  return sum;
}

//answer: 21 days, you have $10,485.76
