$(document).ready(function () {
  let $showAllReplies = $("#showAllReplies");

  $showAllReplies.on("click", getReplies);
  
  function getReplies() {
    let elements = []
    //ev.preventDefault();  // To change submit behavior on forms
    for(var i = 0; i <= $(this).parentElement.length(); i++){

    }
    $(this).parentElement
    console.log($(this).parentElement);
    $.post("_getAllReplies",
      {data: $(this).parentElement},
      displayReplies);

  }
  function displayReplies(data){
    let $repliesContainer = $("div#replies-container");
    let html = "";
    console.log(data)
  }

});