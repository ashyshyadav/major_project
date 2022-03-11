console.log("TEST")
scrollUpBtn = document.getElementById("scroll-up")
// console.log(scrollUpBtn)
mainSection = document.getElementById("main-doc")
console.log(mainSection);

window.onscroll = function(){
    scrollUpBtn.style.display = "block"
    setTimeout(function(){ 
        scrollUpBtn.style.display = "none"
        console.log("Ready")
    }, 8000);
    
}
