function randomChance(quarters){
  for (var i = 1; i <=quarters; i++){
    var win = Math.floor(Math.random()*101);
    if (win == 1){
      var coins = Math.floor(Math.random()*50)+50   //(max-min)+min ==> 100-50 = 50)
      console.log("Yay!! You Win", coins, "You now have", (coins + (quarters - i)), "Keep playing!");
      break;
    }
    else if (i == quarters && win != 1){
      console.log("So sorry, you have no more quarters left");
    }
    else{
      console.log("Try again!");
    }
  }
}


//user pass the number they are willing to leave with

function randomChance(quarters, leave){
  for (var i = 1; i <=quarters; i++){
    var win = Math.floor(Math.random()*101);
    if (win == 1){
      var coins = Math.floor(Math.random()*50)+50   //(max-min)+min ==> 100-50 = 50)
      var newQuarters = (quarters - i) + coins;
      console.log("Yay!! You Win", coins, "You now have", newQuarters, "Keep playing!");
      if (newQuarters >= leave){
        console.log("You now have", newQuarters, "!!! Thank you for playing");
        break;
      }
    }
    else if (i == quarters && win != 1){
      console.log("So sorry, you have no more quarters left");
    }
    else{
      console.log("Try again!");
    }
  }
}
