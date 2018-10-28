
function myFunct(){
	document.getElementById("myPostCode").innerHTML = "Add your current breakdown location's post code below to check if the area is covered by us.";
}



function myPost(){

	var originalPost = document.getElementById("checkpost").value;
  if (originalPost){
    if(originalPost >= 2000 && originalPost <= 2770){

        document.getElementById("myPostCode").innerHTML = "Your current location is covered call for assistance on 0488602271";
    } else{
      document.getElementById("myPostCode").innerHTML = "Sorry we don't cover that area";
    }
  }else{
    alert("Please put a valid postcode in " );

	  }

}
