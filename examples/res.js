// @author: Amey Parundekar //

$(document).ready(function(){
  councilList = [];
  counter = 4;
  $(".councils").on("click",function(){
    if(counter != 0 && !(councilList.includes(this.id))){
      $(this).attr('src',this.id+"1.jpg");
      councilList.push(this.id);
      counter--;
      console.log(councilList);
    }else{
        $(this).attr('src',this.id+".jpg");
        councilList.pop(this.id);
        counter++;
    }

    if(counter == 0){
      window.location.href = "http://localhost/VITCMUN11/examples/#secondPage";
    }
  });
});
